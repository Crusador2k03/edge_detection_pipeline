import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from tkinter import Tk, Label, Frame
from tkinterdnd2 import DND_FILES, TkinterDnD
from datetime import datetime

"""
Industrial Edge Detection Pipeline
-----------------------------------
Detects structural boundaries in industrial component images
using Gaussian blur preprocessing + Canny edge detection.
Demonstrates the effect of preprocessing on edge quality.

Author: Siddharth Kar
"""

# Tunable parameters
LOW_THRESHOLD = 100
HIGH_THRESHOLD = 200

def process_image(image_path):
    """Full edge detection pipeline on the given image path."""

    # Path Cleanup
    image_path = image_path.strip().strip('{}')

    # Extension validation
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    ext = os.path.splitext(image_path)[1].lower()
    if ext not in valid_extensions:
        label.config(
            text=f"Unsupported format: {ext}\nSupported: {valid_extensions}",
            fg="red"
        )
        return
    # Image loading
    image = cv2.imread(image_path)
    if image is None:
        label.config(text=f"Failed to load image: {image_path}", fg="red")
        return

    # BGR --> RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # BGR --> Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    # Adding synthetic noise to simulate real-world conditions
    noise = cv2.randn(np.zeros_like(gray_image), 0, 25)  # Gaussian noise, mean=0, std=25
    noisy_gray = cv2.add(gray_image, noise)

    # Gaussian Blur on noisy image
    blur = cv2.GaussianBlur(noisy_gray, (5, 5), 0)



    # --- Three versions of edge detection ---

    # 1. Edges on NOISY image (no blur) - worst case
    edges_noisy = cv2.Canny(noisy_gray, LOW_THRESHOLD, HIGH_THRESHOLD)

    # 2. Edges WITH blur but WITHOUT morphological cleaning
    edges_blurred = cv2.Canny(blur, LOW_THRESHOLD, HIGH_THRESHOLD)

    # 3. Edges WITH blur AND morphological cleaning - best case
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    edges_clean = cv2.morphologyEx(edges_blurred, cv2.MORPH_CLOSE, kernel)

    # --- Displaying results ---
    plt.figure(figsize=(20, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(edges_noisy, cmap="gray")
    plt.title("Edges — Noisy (No Blur)")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(edges_blurred, cmap="gray")
    plt.title("Edges — Blur Only")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(edges_clean, cmap="gray")
    plt.title("Edges — Blur + Cleaned")
    plt.axis("off")

    plt.suptitle(
        f"Edge Detection — {os.path.basename(image_path)}",
        fontsize=14,
        fontweight='bold'
    )
    plt.tight_layout()

    # Saving output
    os.makedirs("outputs", exist_ok=True)

    # Generate unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f"outputs/{base_name}_{timestamp}.png"

    plt.savefig(output_path, dpi=150, bbox_inches='tight')

    label.config(
        text=f"   Done! Output saved to {output_path}\n\nDrop another image to process again.",
        fg="green"
    )

    plt.show()


def on_drop(event):
    """Called when user drops a file onto the window."""
    image_path = event.data
    process_image(image_path)


# --- GUI ---
root = TkinterDnD.Tk()
root.title("Industrial Edge Detection")
root.geometry("500x250")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Drop zone frame
frame = Frame(
    root,
    bg="#2d2d2d",
    highlightbackground="#555",
    highlightthickness=2,
    relief="flat"
)
frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

# Instructions label
label = Label(
    frame,
    text="Drag & Drop an Image Here\n\nSupported: JPG, PNG, BMP, TIFF",
    font=("Helvetica", 13),
    bg="#2d2d2d",
    fg="#aaaaaa",
    justify="center"
)
label.pack(expand=True)

# Register drop target
frame.drop_target_register(DND_FILES)
frame.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
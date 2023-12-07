import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import rembg
import numpy as np
import sys
import os

def remove_background():
    # Open a dialog to select an image
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            # Load the image using the PIL library
            image = Image.open(file_path)

            # Convert the image to a format accepted by rembg
            image_array = np.array(image)
            output = rembg.remove(image_array)

            # Convert the rembg output back to a PIL image
            output_image = Image.fromarray(output)

            # Save the image with the removed background
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                output_image.save(save_path)

            # Update the image displayed in the interface
            update_display(output_image)

        except Exception as e:
            # Handle errors, e.g., when the selected file is not an image
            print(f"Error: {e}")

def update_display(image):
    # Update the displayed image in the interface
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def restart_program(event):
    # Restart the program
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Create the main window
root = tk.Tk()
root.title("Remove Background")

# Create a label to display the image
label = tk.Label(root)
label.pack(padx=10, pady=10)

# Create a button to initiate background removal and image saving
remove_button = tk.Button(root, text="Start Here", command=remove_background)
remove_button.pack(pady=10)

# Associate the F5 keypress event with the program restart function
root.bind("<F5>", restart_program)

# Start the main GUI loop
root.mainloop()

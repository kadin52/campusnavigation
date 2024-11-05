import tkinter as tk
from tkinter import Button


# Function to zoom in
def zoom_in():
    print("Zooming In")


# Function to zoom out
def zoom_out():
    print("Zooming Out")


def main():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Simple Tkinter Window with Buttons")

    # Add buttons to zoom in and zoom out
    Button(root, text="Zoom In", command=zoom_in).pack(side='left')
    Button(root, text="Zoom Out", command=zoom_out).pack(side='left')

    # Start the Tkinter loop
    root.mainloop()


if __name__ == '__main__':
    main()
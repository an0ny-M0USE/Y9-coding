import os
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("GIF Image Import with PIL and Tkinter")

# Build a path relative to this script so the GIF is found regardless of cwd
base_dir = os.path.dirname(__file__)
gif_path = os.path.join(base_dir, "superhero.gif")

try:
	pil_image = Image.open(gif_path)
except FileNotFoundError:
	print("superhero.gif not found at:", gif_path)
	print("Files in directory:", os.listdir(base_dir))
	raise

tkinter_image = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(root, image=tkinter_image)
image_label.pack()

image_label.image = tkinter_image

root.mainloop()

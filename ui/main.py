import tkinter as tk
from PIL import Image, ImageTk  # Import de Pillow

root = tk.Tk()
root.title("Petit Robert") 

# Centrage de la fenêtre
width = 600
height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Redimensionnement de l'image de fond
original_bg = Image.open('assets/bg.png')
resized_bg = original_bg.resize((width, height), Image.ANTIALIAS)  # Redimensionne l'image
bg = ImageTk.PhotoImage(resized_bg)

bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

root.iconbitmap("assets/dictionary_icon.ico")

root.mainloop()
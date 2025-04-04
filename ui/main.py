import tkinter as tk
from tkinter import ttk
from tracemalloc import start
from PIL import Image, ImageTk  # Import de Pillow
import start
import sys
import os
from PIL import Image
from start import main

root = tk.Tk()
root.title("Petit Robert") 

def resource_path(relative_path):
    """Cherche d'abord le fichier à la racine, sinon utilise le dossier temporaire de PyInstaller."""
    if os.path.exists(relative_path):  
        return os.path.abspath(relative_path)  

    try:
        base_path = sys._MEIPASS  # Quand exécuté en .exe
    except AttributeError:
        base_path = os.path.abspath(".")  # Mode script

    return os.path.join(base_path, relative_path)
# Centrage de la fenêtre
width = 600
height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Redimensionnement de l'image de fond
bg_image_path = resource_path("assets/bg.png")
original_bg = Image.open(bg_image_path)
resized_bg = original_bg.resize((width, height), Image.Resampling.LANCZOS)  # Redimensionne l'image
bg = ImageTk.PhotoImage(resized_bg)

bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

root.resizable(False, False)

root.iconbitmap(resource_path("assets/dictionary_icon.ico"))


def suite():
    root.destroy()
    start.main()

start_button = tk.Button(root, text="Start", width=20, height=2,command=suite)
start_button.place(x=230, y=500)

exit_button = tk.Button(root, text="Exit", width=20, height=2, command=root.quit)
exit_button.place(x=230, y=550)

root.mainloop()

if __name__ == "__main__":
    main()
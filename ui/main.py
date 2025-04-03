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
resized_bg = original_bg.resize((width, height), Image.Resampling.LANCZOS)  # Redimensionne l'image
bg = ImageTk.PhotoImage(resized_bg)

bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

root.resizable(False, False)

root.iconbitmap("assets/dictionary_icon.ico")

start_button = tk.Button(
    root,
    text="Start",
    command = main()
)
exit_button = tk.Button(
    root,
    text="Exit",
    command = root.quit()
)

start_button = tk.Button(root, text="Start", width=20, height=2)
start_button.place(x=230, y=500)

exit_button = tk.Button(root, text="Exit", width=20, height=2)
exit_button.place(x=230, y=550)

root.mainloop()

def main():
    exit
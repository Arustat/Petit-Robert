import tkinter as tk


root = tk.Tk()
root.title("Petit Robert") 

#Centrage de la fenetre

width = 600
height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

root.iconbitmap("assets\le_petit_robert.ico")


root.mainloop()

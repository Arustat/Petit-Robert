import tkinter as tk
from tkinter import messagebox
import os
import re

def ajouter_mot():
    mot = entry_mot.get().strip()
    description = entry_description.get().strip()
    
    if not mot or not description:
        messagebox.showerror("Erreur", "Veuillez entrer un mot et une description.")
        return
    
    with open("mot_dico.txt", "r", encoding="utf-8") as f:
        contenu = f.readlines()
    
    for ligne in contenu:
        if mot.lower() == ligne.split(":")[0].strip().lower():
            messagebox.showinfo("Info", "Le mot existe déjà.")
            return
    
    with open("mot_dico.txt", "a", encoding="utf-8") as f:
        f.write(mot + ": " + description + "\n")
    trier_par_ordre_alpha()
    
    messagebox.showinfo("Succès", "Mot ajouté avec succès !")
    entry_mot.delete(0, tk.END)
    entry_description.delete(0, tk.END)

def trier_par_ordre_alpha():
    with open("mot_dico.txt", "r", encoding="utf-8") as f:
        contenu = f.readlines()
    contenu.sort()
    with open("mot_dico.txt", "w", encoding="utf-8") as f:
        f.writelines(contenu)

def afficher_dictionnaire():
    try:
        with open("mot_dico.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
        messagebox.showinfo("Dictionnaire", contenu if contenu else "Le dictionnaire est vide.")
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier dictionnaire introuvable.")

def supprimer_mot():
    mot = entry_mot.get().strip()
    if not mot:
        messagebox.showerror("Erreur", "Veuillez entrer un mot à supprimer.")
        return
    
    with open("mot_dico.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = [line for line in lines if not re.search(rf'\b{re.escape(mot)}\b', line)]
    
    if len(new_lines) == len(lines):
        messagebox.showinfo("Info", "Mot non trouvé dans le dictionnaire.")
        return
    
    with open("mot_dico.txt", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    
    messagebox.showinfo("Succès", "Mot supprimé avec succès !")
    entry_mot.delete(0, tk.END)

def main():
    global root, entry_mot, entry_description
    root = tk.Tk()
    root.title("Petit Robert") 

    # Centrage de la fenêtre
    width = 600
    height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")

    root.resizable(False, False)

    root.iconbitmap("assets/dictionary_icon.ico")

    tk.Label(root, text="Mot :").pack(pady=5)
    entry_mot = tk.Entry(root, width=50)
    entry_mot.pack(pady=5)

    tk.Label(root, text="Description :").pack(pady=5)
    entry_description = tk.Entry(root, width=50)
    entry_description.pack(pady=5)

    tk.Button(root, text="Ajouter un mot", command=ajouter_mot).pack(pady=10)
    tk.Button(root, text="Supprimer un mot", command=supprimer_mot).pack(pady=10)
    tk.Button(root, text="Afficher tout le dictionnaire", command=afficher_dictionnaire).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

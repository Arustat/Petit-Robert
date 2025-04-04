import tkinter as tk
from tkinter import messagebox
import os
import re
from tkinter import ttk

# Définir le chemin absolu vers mot_dico.txt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Répertoire du script actuel
DICTIONARY_FILE = os.path.join(BASE_DIR, "../mot_dico.txt")  # Chemin vers mot_dico.txt

def ajouter_mot():
    mot = entry_mot.get().strip()
    description = entry_description.get().strip()

    if not mot or not description:
        messagebox.showerror("Erreur", "Veuillez entrer un mot et une description.")
        return

    with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
        contenu = f.readlines()

    for ligne in contenu:
        if mot.lower() == ligne.split(":")[0].strip().lower():
            messagebox.showinfo("Info", "Le mot existe déjà.")
            return

    with open(DICTIONARY_FILE, "a", encoding="utf-8") as f:
        f.write(mot + ": " + description + "\n")
    trier_par_ordre_alpha()

    messagebox.showinfo("Succès", "Mot ajouté avec succès !")
    entry_mot.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    app.afficher_dictionnaire()

def trier_par_ordre_alpha():
    with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
        contenu = f.readlines()
    contenu.sort()
    with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
        f.writelines(contenu)

class DictionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionnaire")

        # Barre de recherche
        self.search_var = tk.StringVar()
        search_frame = tk.Frame(root)
        search_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(search_frame, text="Rechercher :").pack(side="left")
        tk.Entry(search_frame, textvariable=self.search_var).pack(side="left", fill="x", expand=True)
        tk.Button(search_frame, text="Rechercher", command=self.rechercher).pack(side="left", padx=5)
        tk.Button(search_frame, text="Réinitialiser", command=self.afficher_dictionnaire).pack(side="left")

        # Table (Treeview)
        self.tree = ttk.Treeview(root, columns=("Mot", "Action"), show="headings")
        self.tree.heading("Mot", text="Mot", command=self.trier_alphabetiquement)
        self.tree.heading("Action", text="Action")
        self.tree.column("Mot", width=200)
        self.tree.column("Action", width=100)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        if not os.path.exists(DICTIONARY_FILE):
            messagebox.showerror("Erreur", "Fichier dictionnaire introuvable.")

        self.tree.bind("<ButtonRelease-1>", self.gestion_click)

    def afficher_dictionnaire(self):
        self.tree.delete(*self.tree.get_children())
        dictionnaire = self.charger_dictionnaire()
        for mot in sorted(dictionnaire.keys()):
            self.tree.insert("", "end", values=(mot, "🗑 Supprimer"))

    def charger_dictionnaire(self):
        dictionnaire = {}
        if os.path.exists(DICTIONARY_FILE):
            with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
                for ligne in f:
                    if ": " in ligne:
                        mot, description = ligne.strip().split(": ", 1)
                        dictionnaire[mot] = description
        return dictionnaire

    def gestion_click(self, event):
        item = self.tree.identify("item", event.x, event.y)
        col = self.tree.identify_column(event.x)
        if not item:
            return
        if col == "#2":
            mot = self.tree.item(item, "values")[0]
            self.supprimer_mot(mot)

    def supprimer_mot(self, mot):
        if messagebox.askyesno("Confirmation", f"Supprimer le mot '{mot}' ?"):
            dictionnaire = self.charger_dictionnaire()
            dictionnaire.pop(mot, None)
            with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
                for mot, description in dictionnaire.items():
                    f.write(f"{mot}: {description}\n")
            self.afficher_dictionnaire()

    def trier_alphabetiquement(self):
        trier_par_ordre_alpha()
        self.afficher_dictionnaire()

    def rechercher(self):
        query = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        dictionnaire = self.charger_dictionnaire()
        for mot in sorted(dictionnaire.keys()):
            if query in mot.lower():
                self.tree.insert("", "end", values=(mot, "🗑 Supprimer"))

def afficher_graphique():
    # En attente
    return None

def main():
    global root, entry_mot, entry_description, app
    root = tk.Tk()
    root.title("Petit Robert")

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
    tk.Button(root, text="Afficher le graphique du dico !", command=afficher_graphique).pack(pady=10)

    app = DictionnaireApp(root)
    app.afficher_dictionnaire()

    root.mainloop()

if __name__ == "__main__":
    main()

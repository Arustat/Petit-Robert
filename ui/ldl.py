import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

DICTIONARY_FILE = "dictionnaire.json"

def charger_dictionnaire():
    if not os.path.exists(DICTIONARY_FILE):
        return {}
    with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_dictionnaire(data):
    with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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

        # Ajouter une scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.dictionnaire = charger_dictionnaire()
        self.afficher_dictionnaire()

    def afficher_dictionnaire(self):
        self.tree.delete(*self.tree.get_children())
        for mot in sorted(self.dictionnaire.keys()):
            self.tree.insert("", "end", values=(mot, "🗑 Supprimer"))

        # Attacher l'action à un clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.gestion_click)

    def gestion_click(self, event):
        item = self.tree.identify("item", event.x, event.y)
        col = self.tree.identify_column(event.x)
        if not item:
            return
        if col == "#2":  # colonne Action
            mot = self.tree.item(item, "values")[0]
            self.supprimer_mot(mot)

    def supprimer_mot(self, mot):
        if messagebox.askyesno("Confirmation", f"Supprimer le mot '{mot}' ?"):
            self.dictionnaire.pop(mot, None)
            sauvegarder_dictionnaire(self.dictionnaire)
            self.afficher_dictionnaire()

    def trier_alphabetiquement(self):
        self.dictionnaire = dict(sorted(self.dictionnaire.items()))
        self.afficher_dictionnaire()

    def rechercher(self):
        query = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        for mot in sorted(self.dictionnaire.keys()):
            if query in mot.lower():
                self.tree.insert("", "end", values=(mot, "🗑 Supprimer"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DictionnaireApp(root)
    root.mainloop()

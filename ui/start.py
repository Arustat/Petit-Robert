import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os
import matplotlib.pyplot as plt

# Chemin absolu vers le fichier du dictionnaire
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_FILE = os.path.join(BASE_DIR, "../mot_dico.txt")

# --- Fonction pour ajouter un mot au fichier dictionnaire ---
def ajouter_mot():
    mot = entry_mot.get().strip()
    description = entry_description.get().strip()

    if not mot or not description:
        messagebox.showerror("Erreur", "Veuillez entrer un mot et une description.")
        return

    if not os.path.exists(DICTIONARY_FILE):
        open(DICTIONARY_FILE, "w", encoding="utf-8").close()

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

# --- Fonction pour trier le fichier par ordre alphabétique ---
def trier_par_ordre_alpha():
    with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
        contenu = f.readlines()
    contenu.sort()
    with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
        f.writelines(contenu)

# --- Bouton "Graphique" (placeholder) ---
def afficher_graphique():
    nbMot = 0
    # Lecture du fichier ligne par ligne
    with open(DICTIONARY_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            label = line.split(":")[0].strip()
            nbMot = len(line.split(":", 1)[1].strip().split())
            plt.bar(label, nbMot)
            plt.xticks(rotation=70)
    plt.ylabel("Nombre de mots dans la définition")
    plt.title("Mots du dictionnaire")
    plt.show()


# --- Classe principale de l'application ---
class DictionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Petit Robert")
        self.root.geometry("600x600")

        # Variable de recherche
        self.search_var = tk.StringVar()

        # === Barre de recherche + boutons ===
        search_frame = tk.Frame(root)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Rechercher :").pack(side="left")
        tk.Entry(search_frame, textvariable=self.search_var).pack(side="left", fill="x", expand=True)
        tk.Button(search_frame, text="Rechercher", command=self.rechercher).pack(side="left", padx=5)
        tk.Button(search_frame, text="Réinitialiser", command=self.afficher_dictionnaire).pack(side="left", padx=5)
        tk.Button(search_frame, text="Trier", command=self.trier_popup).pack(side="left", padx=5)

        # === Frame pour Treeview + Scrollbar ===
        tree_frame = tk.Frame(root)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # === Tableau principal ===
        self.tree = ttk.Treeview(tree_frame, columns=("Mot", "Description", "Action"), show="headings")
        self.tree.heading("Mot", text="Mot", command=self.trier_par_mot)
        self.tree.heading("Description", text="Description", command=self.trier_par_description)
        self.tree.heading("Action", text="Action")

        self.tree.column("Mot", width=150)
        self.tree.column("Description", width=300)
        self.tree.column("Action", width=100)

        self.tree.pack(side="left", fill="both", expand=True)

        # === Scrollbar à droite du tableau ===
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Liens entre actions et événements souris
        self.tree.bind("<ButtonRelease-1>", self.gestion_click)
        self.tree.bind("<Double-1>", self.modifier_description)

        # Création du fichier dictionnaire s’il n’existe pas
        if not os.path.exists(DICTIONARY_FILE):
            open(DICTIONARY_FILE, "w", encoding="utf-8").close()

    # Affiche tous les mots dans le tableau
    def afficher_dictionnaire(self):
        self.tree.delete(*self.tree.get_children())
        dictionnaire = self.charger_dictionnaire()
        for mot in sorted(dictionnaire.keys()):
            self.tree.insert("", "end", values=(mot, dictionnaire[mot], "🗑 Supprimer"))

    # Lit le dictionnaire depuis le fichier
    def charger_dictionnaire(self):
        dictionnaire = {}
        if os.path.exists(DICTIONARY_FILE):
            with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
                for ligne in f:
                    if ": " in ligne:
                        mot, description = ligne.strip().split(": ", 1)
                        dictionnaire[mot] = description
        return dictionnaire

    # Gère le clic sur le bouton "Supprimer"
    def gestion_click(self, event):
        item = self.tree.identify("item", event.x, event.y)
        col = self.tree.identify_column(event.x)
        if not item:
            return
        mot, description, _ = self.tree.item(item, "values")
        if col == "#3":  # colonne "Action"
            self.supprimer_mot(mot)

    # Supprime un mot du fichier et rafraîchit l'affichage
    def supprimer_mot(self, mot):
        if messagebox.askyesno("Confirmation", f"Supprimer le mot '{mot}' ?"):
            dictionnaire = self.charger_dictionnaire()
            dictionnaire.pop(mot, None)
            with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
                for m, d in dictionnaire.items():
                    f.write(f"{m}: {d}\n")
            self.afficher_dictionnaire()

    # Recherche un mot dans le dictionnaire
    def rechercher(self):
        query = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        dictionnaire = self.charger_dictionnaire()
        for mot, desc in dictionnaire.items():
            if query in mot.lower():
                self.tree.insert("", "end", values=(mot, desc, "🗑 Supprimer"))

    # Gère les doubles clics : affichage ou modification
    def modifier_description(self, event):
        item = self.tree.identify("item", event.x, event.y)
        col = self.tree.identify_column(event.x)

        if not item:
            return

        values = self.tree.item(item, "values")
        mot, description = values[0], values[1]

        if col == "#1":  # Double clic sur le mot → afficher info
            messagebox.showinfo("Détail du mot", f"Mot : {mot}\nDéfinition : {description}")
        elif col == "#2":  # Double clic sur description → édition
            nouvelle_description = simpledialog.askstring("Modifier la description", f"Modifier la description de '{mot}' :", initialvalue=description)
            if nouvelle_description is not None:
                dictionnaire = self.charger_dictionnaire()
                dictionnaire[mot] = nouvelle_description.strip()
                with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
                    for m, d in dictionnaire.items():
                        f.write(f"{m}: {d}\n")
                self.afficher_dictionnaire()

    # Trie par mot (A→Z)
    def trier_par_mot(self):
        self.tri_dictionnaire(cle="mot")

    # Trie par description (A→Z)
    def trier_par_description(self):
        self.tri_dictionnaire(cle="description")

    # Fonction de tri générique
    def tri_dictionnaire(self, cle="mot"):
        dictionnaire = self.charger_dictionnaire()
        items = list(dictionnaire.items())
        items.sort(key=lambda x: x[0].lower() if cle == "mot" else x[1].lower())
        self.tree.delete(*self.tree.get_children())
        for mot, desc in items:
            self.tree.insert("", "end", values=(mot, desc, "🗑 Supprimer"))

    # Affiche une popup pour choisir le type de tri
    def trier_popup(self):
        options = [
            "Mot (A → Z)",
            "Mot (Z → A)",
            "Description (A → Z)",
            "Description (Z → A)"
        ]
        choix = simpledialog.askstring(
            "Tri", 
            "Choisissez un type de tri :\n- Mot (A → Z)\n- Mot (Z → A)\n- Description (A → Z)\n- Description (Z → A)",
            initialvalue=options[0]
        )
        if not choix:
            return

        dictionnaire = self.charger_dictionnaire()
        items = list(dictionnaire.items())

        if choix == "Mot (A → Z)":
            items.sort(key=lambda x: x[0].lower())
        elif choix == "Mot (Z → A)":
            items.sort(key=lambda x: x[0].lower(), reverse=True)
        elif choix == "Description (A → Z)":
            items.sort(key=lambda x: x[1].lower())
        elif choix == "Description (Z → A)":
            items.sort(key=lambda x: x[1].lower(), reverse=True)
        else:
            messagebox.showerror("Erreur", "Option de tri invalide.")
            return

        self.tree.delete(*self.tree.get_children())
        for mot, desc in items:
            self.tree.insert("", "end", values=(mot, desc, "🗑 Supprimer"))

# --- Fonction principale ---
def main():
    global root, entry_mot, entry_description, app
    root = tk.Tk()
    root.title("Petit Robert")

    # Centrer la fenêtre
    width, height = 600, 600
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)

    # Icone personnalisée (si dispo)
    try:
        root.iconbitmap("assets/dictionary_icon.ico")
    except:
        pass  # pas grave si le fichier manque

    # Champs de saisie
    tk.Label(root, text="Mot :").pack(pady=5)
    entry_mot = tk.Entry(root, width=50)
    entry_mot.pack(pady=5)

    tk.Label(root, text="Description :").pack(pady=5)
    entry_description = tk.Entry(root, width=50)
    entry_description.pack(pady=5)

    # Boutons principaux
    tk.Button(root, text="Ajouter un mot", command=ajouter_mot).pack(pady=10)
    tk.Button(root, text="Afficher le graphique du dico !", command=afficher_graphique).pack(pady=10)

    # Lancer l’app
    app = DictionnaireApp(root)
    app.afficher_dictionnaire()

    root.mainloop()

if __name__ == "__main__":
    main()

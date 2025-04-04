import os

# Définir le chemin absolu vers la racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Remonte d'un niveau
DICTIONARY_FILE = os.path.join(BASE_DIR, "mot_dico.txt")  # Chemin absolu vers mot_dico.txt
import os
import sys

def get_base_dir():
    """Retourne le bon répertoire de base, que ce soit en mode dev ou après compilation."""
    try:
        # Lorsqu'on exécute un .exe avec PyInstaller
        base_dir = sys._MEIPASS
    except AttributeError:
        # En mode développement (.py)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return base_dir

BASE_DIR = get_base_dir()
DICTIONARY_FILE = os.path.join(BASE_DIR, "mot_dico.txt")

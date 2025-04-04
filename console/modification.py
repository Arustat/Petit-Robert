import os
from load_data import load_dictionary
import config


def menu_modif():
        while True:
            # Affichage du menu
            print(".{}".format("".ljust(48, ".")))
            print(".               Menu : Modification d'un mot".ljust(49) + ".")
            print("." * 50)
            print("".rjust(5) + "Modifier un mot".ljust(40, "_") + "1")
            print("".rjust(5) + "Retourner au menu principal".ljust(40, "_") + "2")
            print("." * 50)
            choix = input("Quel est votre choix ? : ")
            if choix == "1":
                os.system("cls" if os.name == "nt" else "clear")
                modification()
            elif choix == "2":
                os.system("cls" if os.name == "nt" else "clear")
                return
            else:
                print("Erreur de saisie !")
                menu_modif()


def modification():
    mot = input("Quel mot voulez-vous modifier ? : ").strip()
    if not mot:
        print("Erreur : Vous n'avez pas entré de mot.")
        return

    try:
        # Lire le contenu du fichier avec un encodage permissif
        with open(config.DICTIONARY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Vérifier si le mot existe dans le dictionnaire
        if not any(line.split(":")[0].strip().lower() == mot.lower() for line in lines):
            print(f"Erreur : Le mot '{mot}' n'existe pas dans le dictionnaire.")
            return
        
        
        modif = input("Modifier la définition : ").strip()
        if not modif:
            print("Erreur : Vous n'avez pas entré de nouvelle définition.")
            return

        # Réécrire le fichier avec la modification
        with open(config.DICTIONARY_FILE, "w", encoding="utf-8") as file:
            for line in lines:
                word = line.split(":")[0].strip()
                if word.lower() == mot.lower():
                    file.write(f"{word}: {modif}\n")
                else:
                    file.write(line)

        print(f"Le terme '{mot}' a été modifié avec succès.")
        print("Le dictionnaire a été mis à jour avec la nouvelle définition.")
    except FileNotFoundError:
        print("Erreur : Le fichier dictionnaire est introuvable.")
    except UnicodeDecodeError as e:
        print(f"Erreur d'encodage : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
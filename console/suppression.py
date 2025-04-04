import os
import re
import config


def menu_supp():
    while True:  # Boucle infinie pour gérer le menu
        print(".{}".format("".ljust(48, ".")))
        print(".               Menu : Supprimer un mot".ljust(49) + ".")
        print("." * 50)
        print("".rjust(5) + "Supprimer un mot".ljust(40, "_") + "1")
        print("".rjust(5) + "Retourner au menu principal".ljust(40, "_") + "2")
        print("." * 50)

        choix = input("Votre choix : ")

        if choix == "1":
            os.system("cls" if os.name == "nt" else "clear")
            suppression()  # La fonction pour supprimer un mot
        elif choix == "2":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("Erreur : Choix invalide, veuillez réessayer.")


def suppression():
    sup_request = input("Quel mot voulez-vous supprimer du dictionnaire ? ").strip()

    # Lecture du contenu du fichier
    with open(config.DICTIONARY_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Vérifier si le mot existe dans le fichier
    if not any(re.search(rf'\b{re.escape(sup_request)}\b', line) for line in lines):
        print(f"Le mot '{sup_request}' n'existe pas dans le dictionnaire.")
        rep = input("Voulez-vous supprimer un autre mot ? (Oui/Non) : ").strip().lower()
        if rep in ["non", "n", "no"]:
            return
        else:
            os.system("cls" if os.name == "nt" else "clear")
            return

    # Suppression du mot en réécrivant le fichier sans la ligne contenant ce mot
    with open(config.DICTIONARY_FILE, "w", encoding="utf-8") as file:
        for line in lines:
            # On garde la ligne si le mot n'est pas trouvé
            if not re.search(rf'\b{re.escape(sup_request)}\b', line):
                file.write(line)

    print(f"Le mot '{sup_request}' a bien été supprimé.")

    # Demander si l'utilisateur souhaite supprimer un autre mot
    rep = input("Voulez-vous supprimer un autre mot ? (Oui/Non) : ").strip().lower()
    if rep in ["non", "n", "no"]:
        return
    else:
        os.system("cls" if os.name == "nt" else "clear")
        suppression()  # Relancer la suppression d'un autre mot

#Fonction Suppression d'un mot
import os
import re
import main


def suppression():
    sup_request = input("Quel mot voulez-vous supprimer du dictionnaire ? ")

    with open("mot_dico.txt", "r") as file:
        lines = file.readlines()
        if not any(re.search(rf'\b{re.escape(sup_request)}\b', line) for line in lines):
            print("Le mot n'existe pas dans le dictionnaire.")
            rep = input("Vous voulez revenir au menu principal ? (Oui/Non) : ").strip().lower()
            if rep in ["non", "n", "no"]:
                
                print("Merci d'avoir utilisé le Petit Robert de la nouvelle génération")
                return
            else:
                os.system("cls" if os.name == "nt" else "clear")
                main()
                return

    with open("mot_dico.txt", "w") as file:
        for line in lines:
            # Supprimer toute la ligne si le mot exact est présent
            if not re.search(rf'\b{re.escape(sup_request)}\b', line):
                file.write(line)
    rep = input("Vous voulez revenir au menu principal ? (Oui/Non) : ").strip().lower()
    if rep in ["non", "n", "no"]:
        print("Merci d'avoir utilisé le Petit Robert de la nouvelle génération")
        return
    else:
        os.system("cls" if os.name == "nt" else "clear")
        main()


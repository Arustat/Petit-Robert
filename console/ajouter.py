import os
import config  


def menu_ajout():
    while True:  # Boucle infinie pour gérer le menu
        print(".{}".format("".ljust(48, ".")))
        print(".               Menu : Ajout d'un mot".ljust(49) + ".")
        print("." * 50)
        print("".rjust(5) + "Ajouter un mot".ljust(40, "_") + "1")
        print("".rjust(5) + "Retourner au menu principal".ljust(40, "_") + "2")
        print("." * 50)

        choix = input("Votre choix : ")

        if choix == "1":
            os.system("cls" if os.name == "nt" else "clear")
            ajouter_mot()  # La fonction pour ajouter un mot
        elif choix == "2":
            os.system("cls" if os.name == "nt" else "clear")
            return
        else:
            print("Erreur : Choix invalide, veuillez réessayer.")


def ajouter_mot():
    print("Vous voulez ajouter un mot !")
    mot = input("Veuillez entrer votre mot : ")

    # Vérifier si le fichier existe, sinon le créer
    if not os.path.exists(config.DICTIONARY_FILE):
        open(config.DICTIONARY_FILE, "w", encoding="utf-8").close()

    # Ouverture du fichier en mode lecture avec UTF-8
    with open(config.DICTIONARY_FILE, "r", encoding="utf-8") as f:
        contenu = f.readlines()

    for ligne in contenu:
        # On vérifie si le mot existe déjà
        if mot.lower() == ligne.split(":")[0].strip().lower():
            print("Le mot existe déjà.")
            reponse = input("Voulez-vous ajouter un autre mot ? (Oui/Non) : ").strip().lower()
            if reponse in ["non", "n", "no"]:
                os.system("cls" if os.name == "nt" else "clear")
                return
            else:
                os.system("cls" if os.name == "nt" else "clear")
                ajouter_mot()  # Relancer la fonction pour ajouter un autre mot
                return

    description = input("Veuillez entrer la description du mot : ")

    # Ajout du mot et de sa description dans le fichier
    with open(config.DICTIONARY_FILE, "a", encoding="utf-8") as w:
        w.write(mot + ": " + description + "\n")

    # Trier les mots par ordre alphabétique
    trier_par_ordre_alpha()

    print("Le mot a bien été ajouté.")
    
    reponse = input("Voulez-vous ajouter un autre mot ? (Oui/Non) : ").strip().lower()
    if reponse in ["non", "n", "no"]:
        return
    else:
        ajouter_mot()  # Relancer pour ajouter un autre mot


# Fonction pour trier les mots par ordre alphabétique
def trier_par_ordre_alpha():
    with open(config.DICTIONARY_FILE, "r", encoding="utf-8") as f:
        contenu = f.readlines()

    # Trier le contenu par ordre alphabétique
    contenu.sort()

    # Réécrire le fichier avec les mots triés
    with open(config.DICTIONARY_FILE, "w", encoding="utf-8") as f:
        f.writelines(contenu)


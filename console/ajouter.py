import re 
import os
import config

def ajouter_mot():
    print("Vous voulez ajouter un mot !")
    
    # Demander le mot à ajouter
    while True:
        mot = input("Veuillez entrer votre mot : ").strip()
        if not mot:
            print("Erreur : Le mot ne peut pas être vide.")
            continue
        if not re.match("^[a-zA-ZÀ-ÿ '-]+$", mot):
            print("Erreur : Le mot contient des caractères non valides. Utilisez uniquement des lettres, espaces, apostrophes ou tirets.")
            continue
        break

    # Vérifier si le fichier existe, sinon le créer
    if not os.path.exists(config.DICTIONARY_FILE):
        open(config.DICTIONARY_FILE, "w", encoding="utf-8").close()

    # Ouverture du fichier en mode lecture avec UTF-8
    with open(config.DICTIONARY_FILE, "r", encoding="utf-8") as f:
        contenu = f.readlines()

    # Vérifier si le mot existe déjà
    for ligne in contenu:
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

    # Demander la description
    while True:
        description = input("Veuillez entrer la description du mot : ").strip()
        if not description:
            print("Erreur : La description ne peut pas être vide.")
            continue
        if not re.match("^[a-zA-ZÀ-ÿ0-9 ',.!?-]+$", description):
            print("Erreur : La description contient des caractères non valides.")
            continue
        break

    # Ajout du mot et de sa description dans le fichier
    with open(config.DICTIONARY_FILE, "a", encoding="utf-8") as w:
        w.write(mot + ": " + description + "\n")

    # Trier les mots par ordre alphabétique
    trier_par_ordre_alpha()

    print("Le mot a bien été ajouté.")
    
    # Demander si l'utilisateur veut ajouter un autre mot
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
# Description: Programme principale du jeu 
# Auteur: Mayssa / Antonin / Raphael
# Date: 07/10/2020
# Licence: GNU GPL v3

import os
import re
from search import search_term
from read import display_all

#Fonction principale
def main():
    print("." * 50)
    print(".".ljust(49) + ".")
    print(".           Gestion d'un dictionnaire".ljust(49) + ".")
    print(".    Le Petit Robert de la nouvelle génération".ljust(49) + ".")
    print(".".ljust(49) + ".")
    print("." * 50)
    
    print("".rjust(5) + "Ajout d'un mot".ljust(40, "_") + "1")
    print("".rjust(5) + "Suppression d'un mot".ljust(40, "_") + "2")
    print("".rjust(5) + "Rechercher un mot".ljust(40, "_") + "3")
    print("".rjust(5) + "Affichage de tout le dictionnaire".ljust(40, "_") + "4")
    print("".rjust(5) + "Fin du programme".ljust(40, "_") + "0")
    print("." * 50)
    choix = (input("Quel est votre choix ? : "))
    if (choix == "1"):
        ajouter_mot()
    elif(choix == "2"):
        suppression()
    elif(choix == "3"):
        clear = os.system("cls" if os.name == "nt" else "clear")
        search_term(input("Quel mot voulez-vous rechercher ? : "))
        print("")
        main()
    elif(choix == "4"):
        clear = os.system("cls" if os.name == "nt" else "clear")
        display_all()
        print("")
        main()
    elif(choix == "0"):
        print("Merci d'avoir utilisé le Petit Robert de la nouvelle génération\n0")
        return
    else:
        print("Erreur de saisie !")
        main()



#Fonction Suppression d'un mot


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


def ajouter_mot():
    print("Vous voulez ajouter un mot !")
    mot = input("Veuillez entrer votre mot : ")

    # Ouverture du fichier en mode lecture avec UTF-8
    with open("mot_dico.txt", "r", encoding="utf-8") as f:
        contenu = f.readlines()

    for ligne in contenu:
        # On vérifie si le mot existe déjà
        if mot.lower() == ligne.split(":")[0].strip().lower():
            print("Le mot existe déjà")
            reponse = input("Voulez-vous ajouter un autre mot ? (Oui/Non) : ").strip().lower()
            if reponse in ["non", "n", "no"]:
                rep = input("Vous voulez revenir au menu principal ? (Oui/Non) : ").strip().lower()
                if rep in ["non", "n", "no"]:
                    print("Merci d'avoir utilisé le Petit Robert de la nouvelle génération")
                    return
                else:
                    os.system("cls" if os.name == "nt" else "clear")  # Efface la console
                    main()
                    return
            else:
                ajouter_mot()
                return

    description = input("Veuillez entrer la description du mot : ")

    with open("mot_dico.txt", "a", encoding="utf-8") as w:
        w.write(mot + ": " + description + "\n")    
        trier_par_odre_alpha()

    print("Le mot a bien été ajouté")
    
    reponse = input("Voulez-vous ajouter un autre mot ? (Oui/Non) : ").strip().lower()
    if reponse in ["non", "n", "no"]:
        rep = input("Vous voulez revenir au menu principal ? (Oui/Non) : ").strip().lower()
        if rep in ["non", "n", "no"]:
            print("Merci d'avoir utilisé le Petit Robert de la nouvelle génération")
            return
        else:
            os.system("cls" if os.name == "nt" else "clear")  # Efface la console
            main()
    else:
        ajouter_mot()


#Fonction pour trier les mots par ordre alphabétique
def trier_par_odre_alpha():
    with open("mot_dico.txt","r", encoding="utf-8") as f:
        contenu = f.readlines()
    #Trier le contenu
    contenu.sort()
    with open("mot_dico.txt","w", encoding="utf-8") as f:
        for ligne in contenu:
            f.write(ligne)

#Lancement du programme
main()
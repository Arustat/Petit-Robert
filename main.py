# Description: Programme principale du jeu 
# Auteur: Mayssa / Antonin / Raphael
# Date: 07/10/2020
# Licence: GNU GPL v3
# Fonction Ajouter un mot
import os

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
    choix = int(input("Quel est votre choix ? : "))
    if (choix == 1):
        ajouter_mot()
    elif(choix == 2):
        suppression()
    elif(choix == 3):
        return None
    elif(choix == 4):
        return None
    elif(choix == 0):
        return "Merci d'avoir utilisé le Petit Robert de la nouvelle génération"
    else:
        print("Erreur de saisie !")
        return main()


#Fonction Suppression d'un mot
def suppression():
    sup_request = input("quel mots voulez vous suprimez du dictionnaire : ")
    x = list()
    y = list()
    with open("mot_dico.txt","r") as dico:
        for line in dico:
            if "#" in line:
                # on saute la ligne 
                continue
            data=line.split(":")
            x.append(data[0])
    print(x)
    print(y)             

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
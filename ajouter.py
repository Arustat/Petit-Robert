import os
import main

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
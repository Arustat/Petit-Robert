#Fonction Ajouter un mot
def ajouter_mot():
    print("Vous voulez ajouter un mot !")
    mot = input("Veuillez entrer votre mot : ")

    #Ouverture du fichier en mode lecture avec UTF-8
    with open("mot_dico.txt","r", encoding="utf-8") as f:
        contenu = f.readlines()

    for ligne in contenu:
        #On vérifie si le mot existe déjà
        if mot.lower() == ligne.split(":")[0].lower():
            print("Le mot existe déjà")
            print("Voulez-vous ajouter un autre mot ?")
            reponse = input("Oui/Non : ")
            if reponse.lower() == "non" or reponse.lower() == "n" or reponse.lower() == "no":
                return
            else:
                return ajouter_mot()
    description = input("Veuillez entrer la description du mot : ")

    with open("mot_dico.txt", "a", encoding="utf-8") as w:
        w.write(mot + ": " + description + "\n")    
        trier_par_odre_alpha()    
    print("Le mot a bien été ajouté")

#Fonction pour trier les mots par ordre alphabétique
def trier_par_odre_alpha():
    with open("mot_dico.txt","r", encoding="utf-8") as f:
        contenu = f.readlines()
    #Trier le contenu
    contenu.sort()
    with open("mot_dico.txt","w", encoding="utf-8") as f:
        for ligne in contenu:
            f.write(ligne)

ajouter_mot()
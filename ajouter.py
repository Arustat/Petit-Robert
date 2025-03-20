#Fonction Ajouter un mot
def ajouter_mot():
    print("Vous voulez ajouter un mot !")
    mot = input("Veuillez entrer votre mot : ")
    f = open("mot_disco.json","r")
    contenu = f.read()
    for i in contenu:
        if i == mot:
            return "Le mot existe déjà"
            ajouter_mot()
    description = input("Veuillez entrer une description : ")


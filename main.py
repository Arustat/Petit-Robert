import json

#Programme principale
def main():
    

#Fonction Ajouter un mot
def ajouter_mot():
    print("Vous voulez ajouter un mot !")
    mot = input("Veuillez entrer votre mot : ")
    f = open("mot_disco.json","r")
    contenu = f.read()
    for i in 
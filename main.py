# Description: Programme principale du jeu 
# Auteur: Mayssa / Antonin / Raphael
# Date: 07/10/2020
# Licence: GNU GPL v3
# Fonction Ajouter un mot
import os

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
            

suppression()


# Description: Programme principale du jeu 
# Auteur: Mayssa / Antonin / Raphael
# Date: 07/10/2020
# Licence: GNU GPL v3
# Fonction Ajouter un mot
import os
import json

def suppression():
    sup_request = input("quel mots voulez vous suprimez du dictionnaire : ")
    x = list()
    y = list()
    with open("mot_dico.csv","r") as dico:
        for line in dico:
            if "#" in line:
                # on saute la ligne continue
                continue
            data=line.split()
            x.append(data[0])
            y.append(data[1])
    print(x)
    print(y)
        
                
            

suppression()


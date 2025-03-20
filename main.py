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


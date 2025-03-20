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


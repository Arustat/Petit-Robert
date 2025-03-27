# Description: Programme principale du jeu 
# Auteur: Mayssa / Antonin / Raphael
# Date: 07/10/2020
# Licence: GNU GPL v3
# Fonction Ajouter un mot

import re



def suppression():
    sup_request = input("Quel mot voulez-vous supprimer du dictionnaire ? ")

    # Lire toutes les lignes du fichier
    with open("mot_dico.txt", "r") as file:
        lines = file.readlines()

    # Ouvrir le fichier en écriture après la lecture
    with open("mot_dico.txt", "w") as file:
        for line in lines:
            if not re.search(rf'\b{re.escape(sup_request)}\b', line):
                file.write(line)


suppression()

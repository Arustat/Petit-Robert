# Description: Programme principale du jeu 
# Auteur: Mayssa / Antonin / Raphael
# Date: 07/10/2020
# Licence: GNU GPL v3

import os
import re
from modification import modification
from graphique import graphique
from search import search_term
from read import display_all
import ajouter
import suppression


def main():
    while True:  # Boucle infinie pour gérer le menu
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
        print("".rjust(5) + "Modifier un mot".ljust(40, "_") + "5")
        print("".rjust(5) + "Affichage du graphique".ljust(40, "_") + "6")
        print("".rjust(5) + "Fin du programme".ljust(40, "_") + "0")
        print("." * 50)
        choix = input("Quel est votre choix ? : ")

        if choix == "1":
            ajouter.ajouter_mot()
        elif choix == "2":
            suppression.suppression()
        elif choix == "3":
            os.system("cls" if os.name == "nt" else "clear")
            search_term(input("Quel mot voulez-vous rechercher ? : "))
            print("")
        elif choix == "4":
            os.system("cls" if os.name == "nt" else "clear")
            display_all()
            print("")
        elif choix == "5":
            os.system("cls" if os.name == "nt" else "clear")
            mot = input("Quel mot voulez-vous modifier ? : ")
            modification(mot)
            print("")
        elif choix == "6":
            os.system("cls" if os.name == "nt" else "clear")
            graphique()
            print("")
        elif choix == "0":
            print("Merci d'avoir utilisé le Petit Robert de la nouvelle génération\n0")
            break  # Quitte la boucle et termine le programme
        else:
            print("Erreur de saisie !")

#Lancement du programme
main()
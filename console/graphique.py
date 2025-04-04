import matplotlib.pyplot as plt
import config

def graphique():
    nbMot = 0
    with open(config.DICTIONARY_FILE,"r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            label = line.split(":")[0].strip()
            nbMot = len(line.split(":", 1)[1].strip().split())
            plt.bar(label, nbMot)
            plt.xticks(rotation=70)
    plt.ylabel("Nombre de mots dans la définition")
    plt.title("Mots du dictionnaire")
    plt.show()

import matplotlib.pyplot as plt

def graphique():
    nbMot = 0
    with open("mot_dico.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            label = line.split(":")[0].strip()
            nbMot = len(line.split(":", 1)[1].strip().split())
            plt.bar(label, nbMot)
            plt.xticks(rotation=70)
    plt.ylabel("Nombre de mots dans la définition")
    plt.title("Mots du dictionnaire")
    plt.show()

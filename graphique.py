import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go

def graphique():
    nbMot = 0
    with open("mot_dico.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            label = line.split(":")[0].strip()
            nbMot = len(line.split(":", 1)[1].strip().split())
            plt.bar(label, nbMot)
    plt.show()

graphique()
import json

def search(mot):
    # Ouvrir le JSON
    with open('mot_dico.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

        # Chercher le mot
        if mot in data:
            return data[mot]
        else:
            return "Mot introuvable"
        
search("Cuck")
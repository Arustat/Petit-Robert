import json

def display_all():

    # Ouvrir le JSON
    with open('mot_dico.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

        print(len(data), "mots trouvés dans le dictionnaire", "\n")

        # Lire et afficher chaque mot et sa définition
        for term, definition in data.items():
            print(f"{term} -> Definition: {definition}")

display_all()


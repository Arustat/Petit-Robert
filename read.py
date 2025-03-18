import csv

def display_all():

    # Ouvrir le CSV
    with open('mot_dico.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file) #Lecture en colonnes

        print(len(list(reader)), "mots trouvés dans le dictionnaire", "\n")
        file.seek(0) # Retourner au début du fichier

        # Lire chaque ligne
        for row in reader:
            print(f"{row['Term']} ->  Definition: {row['Definition']}")


display_all()
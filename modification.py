from load_data import load_dictionary

def modification(mot):
    dictionary = load_dictionary()
    term = mot.strip()  # Nettoyer les espaces autour
    definition = dictionary.get(term)
    
    modif = input("modifier la définition: ")
        
    with open("mot_dico.txt","r") as file:
        lines = file.readlines()
    with open("mot_dico.txt","w") as file:
        for line in lines:
            if line.startswith(term):
                file.write(f"{term}: {modif}\n")
            else:
                file.write(line)
    print(f"Le terme '{term}' a été modifié avec succès.")



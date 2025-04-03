def load_dictionary():
    """Charge le fichier texte et retourne un dictionnaire de termes et définitions."""
    dictionary = {}

    with open('mot_dico.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                term, definition = line.split(':', 1) 
                dictionary[term.strip()] = definition.strip() 

    return dictionary

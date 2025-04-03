def load_dictionary(filename):
    """Charge le fichier texte et retourne un dictionnaire de termes et définitions."""
    dictionary = {}

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            # Vérifie qu'il y a bien une séparation entre mot et définition
            if ':' in line:
                term, definition = line.split(':', 1)  # Séparer uniquement sur la première occurrence de ':'
                dictionary[term.strip()] = definition.strip()  # Nettoyer les espaces
    
    return dictionary


def display_all(dictionary):
    """Affiche tous les mots du dictionnaire avec leur définition."""
    print(f"{len(dictionary)} mots trouvés dans le dictionnaire\n")
    for term, definition in dictionary.items():
        print(f"{term} -> {definition}")


def search_term(dictionary, term):
    """Recherche un mot dans le dictionnaire et affiche sa définition."""
    term = term.strip()  # Nettoyer les espaces autour
    definition = dictionary.get(term)

    if definition:
        print(f"{term} -> {definition}")
    else:
        print(f"❌ Le mot '{term}' n'est pas trouvé dans le dictionnaire.")


# Exemple d'utilisation
filename = 'mot_dico.txt'
dico = load_dictionary(filename)

# Afficher tout le dictionnaire
display_all(dico)

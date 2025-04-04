from load_data import load_dictionary

def display_all():
    """Affiche tous les mots du dictionnaire avec leur définition."""
    dictionary = load_dictionary()
    
    print(f"{len(dictionary)} mots trouvés dans le dictionnaire\n")
    for term, definition in dictionary.items():
        print(f"{term} -> {definition}")


# Exécution du script
if __name__ == "__main__":
    display_all()

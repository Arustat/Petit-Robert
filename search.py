from load_data import load_dictionary

def search_term(term):
    """Recherche un mot dans le dictionnaire et affiche sa définition."""
    dictionary = load_dictionary()
    term = term.strip()  # Nettoyer les espaces autour
    definition = dictionary.get(term)

    if definition:
        print(f"{term} -> {definition}")
    else:
        print(f"❌ Le mot '{term}' n'est pas trouvé dans le dictionnaire.")


# Exemple d'utilisation
if __name__ == "__main__":
    mot = input("Entrez un mot à rechercher : ")
    search_term(mot)

from load_data import load_dictionary

def search_term(term):
    """Recherche un mot dans le dictionnaire et affiche sa définition (insensible à la casse)."""
    dictionary = load_dictionary()

    # Convertir toutes les clés du dictionnaire en minuscules
    dictionary_lower = {key.lower(): value for key, value in dictionary.items()}

    # Convertir le mot recherché en minuscule
    term_lower = term.strip().lower()
    definition = dictionary_lower.get(term_lower)

    if definition:
        print(f"{term} -> {definition}")
    else:
        print(f"❌ Le mot '{term}' n'est pas trouvé dans le dictionnaire.")


# Exemple d'utilisation
if __name__ == "__main__":
    mot = input("Entrez un mot à rechercher : ")
    search_term(mot)


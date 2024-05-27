


syllabes_frequentes_francais = [
    "ba", "be", "bi", "bo", "bu",
    "ca", "ce", "ci", "co", "cu",
    "da", "de", "di", "do", "du",
    "fa", "fe", "fi", "fo", "fu",
    "ga", "ge", "gi", "go", "gu",
    "ja", "je", "ji", "jo", "ju",
    "la", "le", "li", "lo", "lu",
    "ma", "me", "mi", "mo", "mu",
    "na", "ne", "ni", "no", "nu",
    "pa", "pe", "pi", "po", "pu",
    "ra", "re", "ri", "ro", "ru",
    "sa", "se", "si", "so", "su",
    "ta", "te", "ti", "to", "tu",
    "va", "ve", "vi", "vo", "vu"
]

frequent_syllables_english = [
    "ba", "be", "bi", "bo", "bu",
    "ca", "ce", "ci", "co", "cu",
    "da", "de", "di", "do", "du",
    "fa", "fe", "fi", "fo", "fu",
    "ga", "ge", "gi", "go", "gu",
    "ha", "he", "hi", "ho", "hu",
    "ja", "je", "ji", "jo", "ju",
    "ka", "ke", "ki", "ko", "ku",
    "la", "le", "li", "lo", "lu",
    "ma", "me", "mi", "mo", "mu",
    "na", "ne", "ni", "no", "nu",
    "pa", "pe", "pi", "po", "pu",
    "ra", "re", "ri", "ro", "ru",
    "sa", "se", "si", "so", "su",
    "ta", "te", "ti", "to", "tu",
    "va", "ve", "vi", "vo", "vu",
    "wa", "we", "wi", "wo", "wu",
    "ya", "ye", "yi", "yo", "yu",
    "za", "ze", "zi", "zo", "zu"
]

def create_identifiant(langue="francais"):
    """
    Crée un identifiant aléatoire composé de deux syllabes fréquentes du français.
    """
    import random
    if langue == "francais":
        syllabes = syllabes_frequentes_francais
    else:
        syllabes = frequent_syllables_english
    id = random.choice(syllabes) + random.choice(syllabes)
    if random.random() < 0.5:
        id += random.choice(syllabes)
    if random.random() < 0.5:
        id = id.capitalize()
    return id


def id_int(l=['i','j','k','l','n','p','o','q']):
    """
    Crée un identifiant aléatoir d'entier 
    """
    import random
    id = random.choice(l) + str(random.randint(0, 1000))
    return id

def id_float(l=['f','g','h','t','u','v','w','x','y','z']):
    """
    Crée un identifiant aléatoir de float 
    """
    return id_int(l)

def id_choix(l=['next','suiv','suivant','link','lien','_next','_suiv','_suivant','_link','_lien']):
    """
    Crée un identifiant aléatoir dans la liste passé en paramètre
    """
    import random
    return random.choice(l)



if __name__ == "__main__":
    for i in range(10):
        print(create_identifiant())
    for i in range(10):
        print(create_identifiant(langue="english"))

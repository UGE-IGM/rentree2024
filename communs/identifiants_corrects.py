import re
import random
import string

def est_identifiant_valide(identifiant):
    """
    Vérifie si l'identifiant est valide selon l'expression régulière [a-zA-Z][a-zA-Z0-9]*.
    
    :param identifiant: La chaîne à vérifier.
    :return: True si l'identifiant est valide, False sinon.
    """
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*$'
    return re.fullmatch(pattern, identifiant) is not None

def generer_identifiant_correct(longueur):
    """
    Génère un identifiant aléatoire valide de la longueur spécifiée.
    
    :param longueur: La longueur de l'identifiant à générer.
    :return: Un identifiant valide.
    """
    premier_caractere = random.choice(string.ascii_letters)
    autres_caracteres = ''.join(random.choices(string.ascii_letters + string.digits, k=longueur-1))
    return premier_caractere + autres_caracteres

def generer_identifiant_incorrect(longueur):
    """
    Génère un identifiant aléatoire invalide de la longueur spécifiée.
    
    :param longueur: La longueur de l'identifiant à générer.
    :return: Un identifiant invalide.
    """
    # Possibilités d'identifiants incorrects
    premiers_caracteres_possibles = string.digits + string.punctuation
    autres_caracteres_possibles = string.ascii_letters + string.digits + string.punctuation
    
    premier_caractere = random.choice(premiers_caracteres_possibles)
    autres_caracteres = ''.join(random.choices(autres_caracteres_possibles, k=longueur-1))
    return premier_caractere + autres_caracteres

def generer_identifiants_melanges(nombre_corrects, nombre_incorrects, longueur_min, longueur_max):
    """
    Génère des identifiants corrects et incorrects mélangés.
    
    :param nombre_corrects: Le nombre d'identifiants corrects à générer.
    :param nombre_incorrects: Le nombre d'identifiants incorrects à générer.
    :param longueur_min: La longueur minimale des identifiants.
    :param longueur_max: La longueur maximale des identifiants.
    :return: Une liste d'identifiants générés, mélangés aléatoirement.
    """
    identifiants_corrects = [generer_identifiant_correct(random.randint(longueur_min, longueur_max)) for _ in range(nombre_corrects)]
    identifiants_incorrects = [generer_identifiant_incorrect(random.randint(longueur_min, longueur_max)) for _ in range(nombre_incorrects)]
    
    identifiants = identifiants_corrects + identifiants_incorrects
    random.shuffle(identifiants)
    
    return identifiants

# Exemple d'utilisation
if __name__ == "__main__":
    nombre_corrects = random.randint(1, 10)
    nombre_incorrects = 10 - nombre_corrects
    longueur_min = 5
    longueur_max = 10

    identifiants_melanges = generer_identifiants_melanges(nombre_corrects, nombre_incorrects, longueur_min, longueur_max)
    
    print("Identifiants mélangés générés :")
    for identifiant in identifiants_melanges:
        print(identifiant)
    
    identifiants_validite = [(identifiant, est_identifiant_valide(identifiant)) for identifiant in identifiants_melanges]
    
    print("\nListe des identifiants avec leur validité :")
    for identifiant, validite in identifiants_validite:
        print(f"{identifiant}: {'Valide' if validite else 'Invalide'}")
    
    # Optionnel : renvoyer la liste des tuples (identifiant, validité)
    print(identifiants_validite)

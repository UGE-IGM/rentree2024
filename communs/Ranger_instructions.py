import random

def expression_aleatoire():
    operations = ['+=', '-=', '*=', '/=', '//=', '%=']  # Liste des opérations d'assignation
    x = random.randint(1, 10)  # Définir x comme un nombre aléatoire
    
    operation = random.choice(operations)  # Choix aléatoire d'une opération d'assignation
    y = random.randint(1, 10)  # Définir y comme un nombre aléatoire
    x_init = x
    # Appliquer l'opération d'assignation choisie à x
    if operation == '+=':
        x += y
    elif operation == '-=':
        x -= y
    elif operation == '*=':
        x *= y
    elif operation == '/=':
        if y != 0:  # Éviter la division par zéro
            x /= y
    elif operation == '//=':
        if y != 0:  # Éviter la division par zéro
            x //= y
    elif operation == '%=':
        if y != 0:  # Éviter la division par zéro
            x %= y
    
    return [x_init, f"x {operation} {y}", x]

def expr():
    r = random.randint(1, 4)
    y = random.randint(0, 10)
    x = y
    r_to_ex = {1 : 'int', 2 : 'float', 3 : 'bool', 4 : 'str'}
    if r == 1:
        x = int(x)
    elif r == 2:
        x = float(x)
    elif r == 3:
        x = bool(x)
    else:
        x = str(x)
    return [y, f'{r_to_ex[r]}(x)', x]

def float_err():
    x = 0
    expression = 'x += 0.1 + 0.2'  # Utilisation de x défini localement
    resultat = eval('0.1 + 0.2')
    return [x, expression, resultat]

def rdm():
    n = random.randint(1, 9)
    if 1 <= n <= 4:
        return expression_aleatoire()
    elif 5 <= n <= 8:
        return expr()
    else:
        return float_err()

# Utilisation de la fonction
def alternative_options(expression):
    # Obtenir le résultat correct de l'expression
    correct_result = eval(expression)
    
    # Générer des options alternatives
    alternatives = [correct_result]

    # Si le résultat est un nombre entier, ajouter une chaîne représentant ce nombre en tant que flottant
    if isinstance(correct_result, int):
        alternatives.append(float(correct_result))

    # Si le résultat est un flottant, ajouter une chaîne représentant ce nombre en tant qu'entier
    if isinstance(correct_result, float):
        alternatives.append(int(correct_result))

    # Si le résultat est un nombre, ajouter une chaîne représentant le résultat correct en majuscules
    if isinstance(correct_result, (int, float)):
        alternatives.append(str(correct_result).upper())

        # Ajouter un nombre aléatoire proche du résultat correct comme alternative
        random_offset = random.uniform(-1, 1) * 0.1 * correct_result
        alternatives.append(correct_result + random_offset)

    # Ajouter une chaîne "Erreur" comme option alternative
    alternatives.append("Erreur")

    # Mélanger les options alternatives
    random.shuffle(alternatives)

    return alternatives

# Utilisation de la fonction
def main():
    expression = rdm()
    print(f"Expression aléatoire x = {expression[0]}, {expression[1]} = {expression[2]}:")

if __name__ == "__main__":
    main()

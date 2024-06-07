import random

# Opérations possibles
operations = ['+', '-', '*', '/', '**', '//', '%']

def generer_expression_aleatoire(operations_utilisees):
    while True:
        operation = random.choice(operations)
        if operation not in operations_utilisees:
            operations_utilisees.add(operation)
            if operation == '**':
                operande = random.randint(1, 3)
            else:
                operande = random.randint(1, 10)  # On prend un opérande aléatoire entre 1 et 10
            expression = f"x {operation} {operande}"
            return expression

def all_rep(value):
    # Génère trois variations de la valeur
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    while y == x:
        y = random.randint(1, 3)
    r = [int(value), int(value) - x, int(value) - y, float(value), float(value) + x, float(value) - y, int(value) + x, int(value) + y]
    random.shuffle(r)
    return r

# Fonction principale
def main():
    # Initialiser x
    x = random.randint(1, 10)
    x_initial = x
    
    # Tirer 3 expressions aléatoires différentes
    operations_utilisees = set()
    expressions_appliquees = [generer_expression_aleatoire(operations_utilisees) for _ in range(3)]
    
    # Appliquer les expressions à x
    for expression in expressions_appliquees:
        x = eval(expression)

    # Générer les variations de x
    l = all_rep(x)
    res = [x == val and type(x) == type(val) for val in l]
    
    # Retourner la variable x initiale, les expressions et le résultat
    return x_initial, expressions_appliquees, x, l, res


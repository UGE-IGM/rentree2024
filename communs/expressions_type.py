import random

# Génération d'un nombre entier aléatoire
def generate_random_int():
    return random.randint(1, 100)

# Génération d'un nombre flottant aléatoire
def generate_random_float():
    return random.uniform(1.0, 100.0)

# Génération d'une chaîne de caractères aléatoire
def generate_random_string():
    strings = ["Hello", "world", "Python", "random", "string"]
    return random.choice(strings)

# Génération d'une expression arithmétique aléatoire
def generate_random_arithmetic_expression():
    operators = ['+', '-', '*', '/', '//', '%', '**']
    op = random.choice(operators)
    left = generate_random_int()
    right = generate_random_int()
    return f"{left} {op} {right}"

# Génération d'une expression de comparaison aléatoire
def generate_random_comparison_expression():
    operators = ['>', '<', '>=', '<=', '==', '!=']
    op = random.choice(operators)
    left = generate_random_int()
    right = generate_random_int()
    return f"{left} {op} {right}"

# Génération d'une expression de fonction intégrée aléatoire
def generate_random_function_expression():
    functions = [
        f"len('{generate_random_string()}')",
        f"abs({generate_random_int() * (-1)})",
        f"round({generate_random_float()}, 2)",
        f"sum([{generate_random_int()}, {generate_random_int()}, {generate_random_int()}])",
        f"max({generate_random_int()}, {generate_random_int()}, {generate_random_int()})",
        f"min({generate_random_int()}, {generate_random_int()}, {generate_random_int()})"
    ]
    return random.choice(functions)

# Génération d'une expression d'accès à une liste ou dictionnaire aléatoire
def generate_random_access_expression():
    list_access = "['a', 'b', 'c'][1]"
    dict_access = "{'key': 'value'}['key']"
    return random.choice([list_access, dict_access])

# Génération d'une expression booléenne aléatoire
def generate_random_boolean_expression():
    expressions = ["True", "False", "not False", "all([True, False, True])", "any([False, False, True])"]
    return random.choice(expressions)

# Fonction pour générer une expression aléatoire
def generate_random_expression():
    expression_generators = [
        generate_random_arithmetic_expression,
        generate_random_comparison_expression,
        generate_random_function_expression,
        generate_random_access_expression,
        generate_random_boolean_expression
    ]
    generator = random.choice(expression_generators)
    return generator()

# Fonction pour obtenir le type de l'expression
def get_expression_type(expr):
    try:
        result = eval(expr)
        return type(result).__name__
    except Exception as e:
        return str(e)

# Exemple d'utilisation

def lst(n):
    l = []
    for i in range(n):
        expression = generate_random_expression() 
        l.append((expression, get_expression_type(expression)))
    return l

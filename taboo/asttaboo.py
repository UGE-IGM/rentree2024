

# objectif tester la présence d'éléments syntaxiques dans un code source 
# Fournir une api simple pour définir la liste des éléments syntaxiques à rechercher
# Avec une blacklist

# Exemple d'utilisation 

import ast

def has_taboo(code,black,functions):
    """
    code : le code source à analyser
    black : liste des éléments syntaxiques standard interdits
    functions : liste des fonctions interdites
    Retourne True si aucun élément syntaxique interdit n'est trouvé
    """

    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.AST):
            if node.__class__.__name__ in black:
                return True
        if isinstance(node, ast.Call):
            print(node.__class__.__name__)
            print(node.__dict__['func'].id)
            if node.__dict__['func'].id in functions:
                return True
        if isinstance(node, ast.Attribute):
            print(str(node.__dict__['attr']))
            if node.__dict__['attr'] in functions:
                return True
    return False


def printast(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.AST):
            print(node.__class__.__name__)
        if isinstance(node, ast.Attribute):
            print(node.__class__.__name__)
        


# Exemple d'utilisation



if __name__ == "__main__":
    import sys
    print("taboo ok =",has_taboo("a if b else c",["IfExp"],["append"]))
    print("taboo not ok =",has_taboo("a=f()",[],["g"]))


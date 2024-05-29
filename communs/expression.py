


# Retourne une expresions constante avecaléatoireement 2 ou trois opérandes 
# Construire avec les operateurs de la liste op
# les constantes sont dans la liste args 

from random import choice,  randint
from evalC import evalC

def expressionC(op, *args):
    nbop = randint(2, 3)
    if nbop == 2:
        exp  =str(choice(args))+choice(op)+str(choice(args))
    else:
        exp = str(choice(args))+choice(op)+str(choice(args))+choice(op)+str(choice(args))
    return exp,evalC(exp)


def expression(op, *args):
    nbop = randint(2, 3)
    if nbop == 2:
        exp  =str(choice(args))+choice(op)+str(choice(args))
    else:
        exp = str(choice(args))+choice(op)+str(choice(args))+choice(op)+str(choice(args))
    return exp,eval(exp)


def listexpr(nb,op, *args):
    l=[]
    for i in range(nb):
        l.append(expression(op,*args))
    return l


def listexpr_C(nb,op, *args):
    l=[]
    for i in range(nb):
        l.append(expression(op,*args))
    return l


# Exemple d'utilisation
for w in range(10):
    print(expression(['+', '-', '*', '/'], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Exemple d'utilisation
print(listexpr_C(10, ['*', '>>', '<<', '|'], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


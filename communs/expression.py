


# Retourne une expresions constante avecaléatoireement 2 ou trois opérandes 
# Construire avec les operateurs de la liste op
# les constantes sont dans la liste args 

from random import choice, randint
from evalC import evalC

def expression_C(op, *args):
    nbop = randint(2, 3)
    first, second = choice(op), choice(op)
    if nbop == 2:
        exp = str(choice(args)) + first + str(choice(args))
    else:
        if (first == '>>' or first == '<<') and (int(eval(str(choice(args)) + second + str(choice(args))))) < 0:
            exp = str(choice(args)) + first + '(' + str(choice(args)) + second + str(choice(args)) + ')' + ' * (-1)'
        else:
            exp = str(choice(args)) + first + str(choice(args)) + second + str(choice(args))

    return exp, evalC(exp)


def expression(op, *args):
    nbop = randint(2, 3)
    if nbop == 2:
        exp = str(choice(args)) + choice(op) + str(choice(args))
    else:
        exp = str(choice(args)) + choice(op) + str(choice(args)) + choice(op) + str(choice(args))

    return exp, round(eval(exp), 2)


def listexpr(nb,op, *args):
    l = []
    for i in range(nb):
        l.append(expression(op,*args))
    return l


def listexpr_C(nb,op, *args):
    l = []
    for i in range(nb):
        l.append(expression_C(op,*args))
    return l



def expression_C_avancee(op, *args):
    nbop = randint(2, 3)
    #nom_op, operation_random = choice(list(op.items()))
    operation_random = op


    #if nom_op == 'binaire':
    exp = str(choice(args)) + choice(operation_random) + str(choice(args)) + choice(operation_random) + str(choice(args))



    # if nbop == 2:
    #     exp = str(choice(args)) + choice(op) + str(choice(args))
    # else:
    #     exp = str(choice(args)) + choice(op) + str(choice(args)) + choice(op) + str(choice(args))
    # return exp, evalC(exp)






def main() -> None:

    # en Python
    for w in range(10):
        print(expression(['+', '-', '*', '/'], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    # en C:

    des_operations_unaires = ['sizeof', '-', '~', '!', '*', '&', '++', '--'] # il faut `casts de type` aussi

    des_operations_binaires = ['+', '*', '-', '*', '/', '%', '>>', '<<']

    des_operations_comparaisons = ['<', '>', '<=', '>=', '==', '!=', '&&', '||']

    des_operations_bit_a_bit = ['^', '&', '|']

    des_operations_affectations = ['=',  '*=', '/=', '%=', '+=', '-=', '<<=', '>>=', '&=', '^=', '|=']

    des_operations_expressions = [ ['[', ']'],
                                    ['(', ')'], '.', '->']

    # je ne sais pas comment faire une operation binaire pour que ça sera correct
    une_operation_ternaire = f'%s ? %s : %s'
    # virgule ','

    all_operations = {'unaire': des_operations_unaires, 'binaire': des_operations_binaires,
                        'cmp': des_operations_comparaisons, 'bit_a_bit': des_operations_bit_a_bit,
                        'affect': des_operations_affectations, 'expressions': des_operations_expressions}

    # Exemple d'utilisation
    print(listexpr_C(10, des_operations_binaires, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    expression_C_avancee(des_operations_binaires, [i for i in range(1, 11)])



if __name__ == '__main__':
    main()

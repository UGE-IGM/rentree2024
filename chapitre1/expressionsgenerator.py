

# cette fonction retourne une expression aléatoire basé sur 
# la liste de variables v passé en paramètre
# et la liste de operateur op passé en paramètre 
def expression(v, op):
    import random
    l=set()
    va = random.choice(v)
    l.add(va)
    exp = "{"+va+"}"
    for i in range(random.randint(1, 5)):
        va = random.choice(v)
        l.add(va)
        exp += random.choice(op) +  "{"+va+"}"
    return exp,l

if "__main__" == __name__ :
    v = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    op = ["+", "-", "*", "/","**","%", "//", ">>", "<<", "&", "|", "^"]
    for i in range(10):
        print(expression(v, op))


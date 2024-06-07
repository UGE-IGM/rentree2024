

# Renvois une liste de couples (title,pltest) à partir d'une chaine 
# Soit une ligne commencant par # suivie d'un titre
# Soit une ligne commencant par >>> suivie d'un pltest
# une ligne ne commancant ni par # ni par >>> le résultat du test 
def parsePltest(text):

    lines = text.split("\n")
    pltests = []
    title = ""
    pltest = ""
    state = 0
    for line in lines:
        if state==0:
            if line.startswith("#"):
                title = line[1:].strip()
                state = 1
                pltest = ""
            else:
                print("error not in test ")
        elif state == 1:
            if not  line.startswith("#"):
                pltest = pltest + line + "\n"
            else:
                state = 1
                pltests.append((title,pltest))
                title = line[1:].strip()
                pltest = ""
    pltests.append((title,pltest))    
    return pltests


t="""# test 1
>>> f() # Hidden  test 
3
>>> g() # Cecie est un test
4
# test 2
>>> f()
3
>>> g()+f()
7
"""

print(parsePltest(t)) # [('test 1', 'f()\n'), ('test 2', 'f()\n')]

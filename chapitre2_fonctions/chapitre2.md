

# Objectifs 

Les objectifs pédagogiques pour les [fonctions](theorie1.md) être capable d':

1) Ecrire une fonction dans le langage.
    - Ecrire une fonction constante faire remarquer que cela n'a pas beaucoup d'intéret.

2) Ecrire une fonction qui fait un calcul **simple** (aléatoire)
    - Pour cela il faut être capable de produire une paire (énoncé, expression),
    - Un noms de fonction aléatoire, si vous donner des noms de parametre dans votre énoncé il faut qu'ils soient aléatoires.
    Exemple de calculs:
    - carré, cube, aire d'une surface, volume d'un solide,cf.[aires](theorie2.md) [Volumes](theorie3.md)

    Testez des valeurs problèmatiques si il en a : -1,0,1.  
    Jouez sur les constantes.

3) Ecrire une fonction **recursive** simple. 
    - Factorielle 
    - Somme, Somme des carrés, Somme des Cubes 
    - Une formule de récurence simple : Un= aUn-1+ b  
    Plus dur
    - Une a plusieurs niveau: Fibonacci, Un= aUn-1+ bUn-2, Un= aUn-1+ bUn-2 + CUn-3



# Objectifs avec des boucles

Si l'on a des boucles alors on peut:

1) Ecrire une version itérative des fonctions récursives vues plus haut.
2) Un exercice avec une boucle !!
    Débrouillez vous pour qu'il soit aléatoire  :)


# Une fonction avec une fonction en parametre 

Ecrire des exos simples avec une fonction en parametre.

Dans le cas du C pour simplifier vous pouvez donner le typedef *fonction_int_a_int*.


Exemple:Vérifier qu'une valeur vérifie la négation d'un prédicat.
```C
int estpair(int n){ return n&1 == 0; }
int negation(int (*f)(int), int p){ return ! (f(n));}
```
Pour l'inverse :
```C
typedef int (*fonction_int_a_int)(int);
int inverser_valeur_retour(fonction_int_a_int f, int n) {
    int valeur = f(n);
    return -valeur;
}
```
La composition de deux fonctions .


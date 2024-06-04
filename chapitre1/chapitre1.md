

# Le chapitre 1 

Les identificateurs, les constantes, les types, les expresssions.

Déclarations et définitions. 


## Les constantes 

Objectif que les étudiants soient capables de reconnaitre le type d'une constante (façon minimale: 3 n'est pas un float).

## Les expressions constantes 

Objectif que les étudiants soient capables de calculer une expression constante et d'identifier son type.

## les identifiants 

Comment différencier les mots clefs des identifants (par coeur).

Qu'un identifiant ne contient que des caractères alphanumériques et le souligné, et ne commence pas par un chiffre.


********==========================********

## Exercices sur les expressions  

1) Quels sont les identifiant correctes (expression rationnel: \[a-zA-z]\[a-zA-Z0-9]*)
1) Match list ou bubles entre des expressions et leur valeur. 
2) Match list ou bubles entre des expressions et leur type.  
3) Pour le C 
    a) l'ordre d'execution peut il changer le resultat du calcul ?
    b) L'expression a telle un effet de bord (modification du contenu de la mémoire).

4) Exercice sur l'ordre d'évaluation et la priorité des opérateurs. 
Exemple:   a+b*c est il égale à (a+b)*c ou à a+(b*c)
5) Exercice que contient la variable X après cette liste d'instruction.
6) Rangez ces instructions dans l'ordre pour que la variable X contiennne la valeur Z.

# Exercice sur les expressions conditionnelles 

1) Intervales 
2) Tableau de vérité
3) Découpage du Plan, ensemble d'inégalités.


# Idée d'exercices 

1) scrabble : quel est le bonus de la case i,j fournir une image du terrain.
2) master mind : on a un un groupe de 4 couleurs R,b,j,v avec 2 blanche et 1 noir, quelles sont les combinaisons qui ne peuvent pas être solution. L'exercice consiste a dire si une combinaison peut être une solution ou pas.
3) L'age du capitaine. 



# Expressions en langage C

En langage de programmation C, les expressions sont des combinaisons de valeurs, variables, opérateurs et appels de fonctions qui sont évaluées pour produire un résultat. 

Les expressions sont caractérisées par un type, une valeur et un effet de bord.

L'expressions est évalué à l'exécution du programme et produit une valeur d'un certain type. L'effet de bord est le fait que le calcul de l'expression a pour effet de modifier le contenu de la mémoire ou d'effectuer un action sur l'extérieur.


Voici un aperçu des différents familles d'expressions que vous pouvez rencontrer en C :

### 1. Expressions arithmétiques
Les expressions arithmétiques utilisent des opérateurs arithmétiques pour effectuer des calculs sur des valeurs numériques.
- **Addition** : `a + b`
- **Soustraction** : `a - b`
- **Multiplication** : `a * b`
- **Division** : `a / b`
- **Modulo** : `a % b`

### 2. Expressions de comparaison
Ces expressions comparent deux valeurs et renvoient un résultat booléen (`1` pour vrai et `0` pour faux).
- **Égal à** : `a == b`
- **Différent de** : `a != b`
- **Inférieur à** : `a < b`
- **Supérieur à** : `a > b`
- **Inférieur ou égal à** : `a <= b`
- **Supérieur ou égal à** : `a >= b`

### 3. Expressions logiques
Les expressions logiques utilisent des opérateurs logiques pour combiner plusieurs conditions.
- **ET logique** : `a && b`
- **OU logique** : `a || b`
- **NON logique** : `!a`

### 4. Expressions bit à bit
Ces expressions effectuent des opérations au niveau des bits.
- **ET bit à bit** : `a & b`
- **OU bit à bit** : `a | b`
- **XOR bit à bit** : `a ^ b`
- **Complément bit à bit** : `~a`
- **Décalage à gauche** : `a << n`
- **Décalage à droite** : `a >> n`

### 5. Expressions d'affectation
Les expressions d'affectation assignent une valeur à une variable.
- **Affectation simple** : `a = b`
- **Affectation avec opération** : `a += b` (équivaut à `a = a + b`), `a -= b`, `a *= b`, etc.

### 6. Expressions de type
Ces expressions permettent de manipuler les types des variables.
- **Cast de type** : `(int) a`

### 7. Expressions conditionnelles (opérateur ternaire)
L'opérateur ternaire est une forme compacte de l'instruction `if-else`.
- **Syntaxe** : `condition ? expression_si_vrai : expression_si_faux`
- **Exemple** : `int max = (a > b) ? a : b;`

### 8. Expressions de séquence
Les expressions de séquence permettent d'exécuter plusieurs expressions en séquence.
- **Syntaxe** : `expression1, expression2, expression3, ...`
- **Exemple** : `int a = (b = 3, b + 2);` (ici, `a` sera égal à 5)

### 9. Appels de fonction
Les appels de fonction sont aussi considérés comme des expressions.
- **Syntaxe** : `fonction(arguments)`
- **Exemple** : `int result = sqrt(25);` (appel de la fonction `sqrt` pour calculer la racine carrée de 25)

### 10. Expressions de pointeur
Ces expressions impliquent des pointeurs et des opérations de manipulation de pointeurs.
- **Déférencement** : `*p` (accède à la valeur pointée par `p`)
- **Adresse** : `&a` (obtient l'adresse de `a`)
- **Accès via pointeur** : `p->membre` ou `(*p).membre` (accède au membre d'une structure pointée par `p`)

### Exemples combinés
```c
#include <stdio.h>

int main() {
    int a = 5, b = 10;
    int result;
    
    // Expression arithmétique
    result = a + b;
    printf("a + b = %d\n", result);
    
    // Expression de comparaison
    if (a < b) {
        printf("a is less than b\n");
    }
    
    // Expression logique
    if (a < b && b > 0) {
        printf("Both conditions are true\n");
    }
    
    // Opérateur ternaire
    result = (a > b) ? a : b;
    printf("The greater value is %d\n", result);
    
    // Appel de fonction
    printf("Square root of 25 is %.2f\n", sqrt(25.0));

    return 0;
}
```

Dans cet exemple, diverses expressions sont utilisées pour illustrer leur syntaxe et leur fonction.
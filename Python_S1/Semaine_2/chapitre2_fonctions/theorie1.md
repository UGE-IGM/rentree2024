
# Fonctions 

Comprendre les fonctions dans les langages de programmation est essentiel pour maîtriser la programmation. Voici les concepts clés à connaître :

### 1. Définition d'une fonction
Une fonction est un bloc de code réutilisable conçu pour accomplir une tâche particulière. Elle permet de structurer le code de manière plus lisible et modulaire.

### 2. Syntaxe de base
La syntaxe de définition d'une fonction varie selon le langage, mais elle inclut généralement un nom, des paramètres, un corps de fonction, et un retour de valeur.
 Par exemple, en Python :
```python
def nom_de_fonction(parametre1, parametre2):
    # Corps de la fonction
    valeur_de_retour = parametre1+parametre2
    return valeur_de_retour
```

### 3. Paramètres et Arguments
- **Paramètres** : variables listées dans la définition de la fonction.
- **Arguments** : valeurs réelles passées à la fonction lorsque celle-ci est appelée.
 Par exemple, en Python :
```python
>>> print(nom_de_fonction("Hello ","World !"))
Hello World !
```

### 4. Valeur de retour
La valeur de retour est le résultat qu'une fonction renvoie au terme de son exécution. 
Certaines fonctions ne renvoient rien (en Python, on utilise `return` sans valeur ou pas de `return` du tout, ce qui renvoie `None`).
```python
def double(x):
    return x*2
val = double(6) # la valeur de retour est assigné à la variable val
print(double(7)) # la valeur de retour est affiché
```


### 5. Portée des variables
Les variables définies à l'intérieur d'une fonction sont locales à cette fonction, ce qui signifie qu'elles ne peuvent pas être utilisées en dehors de celle-ci. Il y a aussi des variables globales accessibles dans tout le programme.

#### locales vs globales 

Une variable locale de même nom cache la variable globale.


### 6. Fonctions imbriquées
Il est possible de définir des fonctions à l'intérieur d'autres fonctions. Cela permet de créer des scopes (portées) locaux supplémentaires.

### 7. Fonction anonymes ou lambdas
Certaines langages (comme Python, JavaScript) permettent de définir des fonctions sans nom, appelées lambdas ou fonctions anonymes. Exemple en Python :
```python
carre = lambda x: x * x
print(carre(5))  # Output: 25
```

### 8. Fonctions d'ordre supérieur
Les fonctions d'ordre supérieur sont des fonctions qui peuvent prendre des fonctions en paramètres ou retourner des fonctions. Exemple en JavaScript :
```javascript
function appliqueFonction(fonction, valeur) {
    return fonction(valeur);
}
console.log(appliqueFonction(x => x * 2, 5));  // Output: 10
```
Un exemple classique est la fonction qsort de la norme POSIX.
```C
#include <stdlib.h>

void qsort(void base[.size * .nmemb], size_t nmemb, size_t size,
            int (*compar)(const void [.size], const void [.size]));
```


### 9. Récursivité
Une fonction récursive est une fonction qui s'appelle elle-même. La récursivité doit toujours avoir une condition d'arrêt pour éviter une boucle infinie.
```python
def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n - 1)
print(factorielle(5))  # Output: 120
```
La récursivité est surtout utile quand il faut faire un parcourt qui n'est pas connu à l'avance. Par exemple la recherche de la sortie dans un labyrinthe ou la coloration d'une surface délimité par une courbe indescriptible. 

### 10. Surcharge de fonctions (Overloading) [java,C++]
Certains langages, comme C++ ou Java, permettent de définir plusieurs fonctions ayant le même nom mais des paramètres différents. Ceci s’appelle la surcharge de fonctions.
C'est le type des argument qui permettent au compilateur de choisir la bonne fonction.


### 11. Cloisonnement lexical (Closure) [python,javascript]
Un cloisonnement lexical est une fonction qui se souvient de l'environnement dans lequel elle a été créée. Cela permet de capturer et d'utiliser des variables locales même après la fin de l'exécution du bloc de code.
```javascript
function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    }
}
let counter = createCounter();
console.log(counter());  // Output: 1
console.log(counter());  // Output: 2
```

Ces concepts constituent la base de la compréhension des fonctions dans la programmation. Les maîtriser permet de créer des programmes plus efficaces, lisibles et faciles à maintenir.
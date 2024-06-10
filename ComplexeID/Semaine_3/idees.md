# Exercices TP3

## Exercice 1

1. **[MATRICE_ALEATOIRE]** écrivez la fonction **<code>matrice_aleatoire(n)</code>** pour qu’elle renvoie une matrice **<code>n</code>** × **<code>n</code>** d’entiers entre 1 et 9, choisis au hasard.

2. **[VERIFIER_MATRICE]** écrivez la fonction **<code>verifier_matrice(M)</code>** qui prend en paramètre une matrice **<code>n</code>** × **<code>n</code>** d’entiers, afin que cette fonction renvoie **<code>True</code>** si la matrice est une solution valide et **<code>False</code>** sinon. Remarquez que les vérifications à effectuer sont assez répétitives; il est donc plus que recommandé de créer une ou des fonctions auxiliaires.

3. **[GRILLE_VALIDE_ALEATOIRE]** écrivez la fonction **<code>grille_valide_aleatoire()</code>** qui renvoie une grille Sudoku valide. on peut “renommer” les éléments de la matrice en appliquant un décalage modulaire: par exemple, remplacer M[i][j] par (M[i][j] + 5) % 9 + 1 pour renvoyer des solutions valides plus variées.

### _Tous les exercices de type "Écrivez la fonction {fonction()}" sont déjà sur PLaTon grâce à la template PLTest_

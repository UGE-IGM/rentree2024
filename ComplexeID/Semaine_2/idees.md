# Exercices TP2

## Exercice 1

1. **[LISTE_ALEATOIRE_NATURELS]** écrivez la fonction **<code>liste_aleatoire_naturels(n, maximum)</code>** qui renvoie une liste aléatoire de **<code>n</code>** naturels compris entre 0 et **<code>maximum</code>**.

2. **[ENUMERER_1]** écrivez la fonction **<code>enumerer_1(liste)</code>** qui prend en paramètre une **<code>liste</code>** de naturels et renvoie une autre liste contenant en case **<code>i</code>** le nombre de fois que **<code>i</code>** apparaît dans la liste en utilisant la méthode **<code>count(k)</code>**

3. **[ENUMERER_2]** écrivez la fonction **<code>enumerer_2(liste)</code>** qui prend en paramètre une **<code>liste</code>** de naturels et renvoie une autre liste contenant en case **<code>i</code>** le nombre de fois que **<code>i</code>** apparaît dans la liste en parcourant les éléments de la liste un par un et en incrémentant le compteur dans la liste d'occurences

4. **[TRACER]** coder la fonction tracer et créer le graphique du temps d'exécution des fonctions.
   
## Exercice 2

1. **[LISTE_ALEATOIRE_TRIEE]** écrivez la fonction **<code>liste_aleatoire_triee(n, pas=10)</code>** qui renvoie une liste triée de **<code>n</code>** naturels choisis au hasard. Votre fonction doit être en **<code>O(n)</code>**, si l’on néglige la complexité de la fonction utilisée pour générer un nombre aléatoire.

2. **[INSERTION_TRIEE_1]** écrivez la fonction **<code>insertion_triee_1(liste, element)</code>** qui implémente la manière naïve de procéder: un ajout du nouvel **<code>element</code>** en fin de **<code>liste</code>**, suivi d’un appel à la méthode **<code>sort()</code>**.

3. **[INSERTION_TRIEE_2]** écrivez la fonction **<code>insertion_triee_2(liste, element)</code>** qui implémente l'approche:
   1. Après avoir ajouté **<code>element</code>** en fin de **<code>liste</code>**, s’il est précédé d’un élément plus grand que lui, on échange ces deux éléments; sinon, on         sort de la fonction
   2. On examine ensuite **<code>element</code>** en avant-dernière position, et on fait la même chose;
   3. Et ainsi de suite jusqu’à ce qu’on arrive au début de la **<code>liste</code>**.

4. **[INSERTION_TRIEE_3]** écrivez la fonction **<code>insertion_triee_3(liste, element)</code>** qui implémente une autre façon de faire:
    - On cherche l’endroit où l’insertion doit s’effectuer, puis on insère **<code>element</code>** directement à cette position plutôt que d’effectuer des échanges
   
5. **[TRACER]** cf: Tracer 1-4
   
## Exercice 3

1. **[SUPPRIMER_PAIRS_1]** Écrivez la fonction **<code>supprimer_pairs_1(liste)</code>** qui supprime les éléments pairs de la **<code>liste</code>** de naturels donnée. On ne doit pas utiliser de liste auxiliaire et il faut utiliser **<code>while</code>**

2. **[SUPPRIMER_PAIRS_2]** Écrivez la fonction **<code>supprimer_pairs_2(liste)</code>** qui supprime les éléments pairs de la **<code>liste</code>** de naturels donnée. On doit cette fois utiliser une liste auxiliaire qui va écraser la première avec la syntaxe **<code>liste[:] = liste_auxiliaire</code>**

3. **[SUPPRIMER_PAIRS_3]** Écrivez la fonction **<code>supprimer_pairs_3(liste)</code>** qui supprime les éléments pairs de la **<code>liste</code>** de naturels donnée exactement comme **<code>supprimer_pairs_1(liste)</code>** mais en partant cette fois-ci de la fin de la liste plutôt que du début. 

4. **[TRACER]** cf: Tracer 1-4

### _Tous les exercices de type "Écrivez la fonction {fonction()}" sont déjà sur PLaTon grâce à la template PLTest_

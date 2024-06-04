
# Boucles 

## Avec un indice 

Imprimer les nombre de 0 à n
```Python
n= constante
i=0
while i< n :
    print(i)
    i= i +1
```
Mieux avec une boucle for et la fonction **range** :

```python
for i in range(n):
    print(i)
```

## Avec une sequence 

Python propose plusieurs structure de données préprogrammés : list,set,dict, etc que l'on peut parcourir avec une boucle . 
Au lieux de travailler avec des indice on travail directement sur les élements. 

```python
for e in ensemble:
    print(e)
```
Par exemple:
```python
l = [(1,2),(2,3),("tt","uu"))]
for e in ensemble:
    print(e)
```
done
```python
(1, 2)
(2, 3)
('tt', 'uu')
```


# Idée d'exercices 

1) scrabble : quel est le bonus de la case i,j fournir une image du terrain.
Soit le dico suivant (ou tableau en C) des valeurs des lettres. Donner la valeur du mot W posé de x,y à x',y'. 

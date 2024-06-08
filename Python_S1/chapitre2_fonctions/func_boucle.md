
### 1. **Calcul de la somme des carrés des n premiers entiers**

Cette fonction utilise une boucle pour calculer la somme des carrés des n premiers entiers.
```python
def somme_carre_n_premiers_entiers(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i * i
    return somme

# Exemple d'utilisation
print(somme_carre_n_premiers_entiers(10))  # Sortie : 385
```

### 2. **Inverser une chaîne de caractères**

Cette fonction utilise une boucle pour inverser une chaîne de caractères.
```python
def inverser_chaine(chaine):
    chaine_inversee = ""
    for caractere in chaine:
        chaine_inversee = caractere + chaine_inversee
    return chaine_inversee

# Exemple d'utilisation
print(inverser_chaine("Python"))  # Sortie : nohtyP
```

### 3. **Trouver la factorielle d'un nombre**

Cette fonction utilise une boucle pour calculer le facteuriel d'un nombre.
```python
def factoriel(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Exemple d'utilisation
print(factoriel(5))  # Sortie : 120
```

### 4. **Calculer la somme des éléments d'une liste**

Cette fonction utilise une boucle pour calculer la somme des éléments d'une liste.
```python
def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

# Exemple d'utilisation
print(somme_liste([1, 2, 3, 4, 5]))  # Sortie : 15
```

### 5. **Trouver les nombres premiers jusqu'à n**

Cette fonction utilise une boucle pour trouver tous les nombres premiers jusqu'à n.
```python
def nombres_premiers_jusqua(n):
    premiers = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            premiers.append(num)
    return premiers

# Exemple d'utilisation
print(nombres_premiers_jusqua(30))  # Sortie : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### 6. **Calculer la suite de Fibonacci jusqu'à n termes**

Cette fonction utilise une boucle pour générer la suite de Fibonacci jusqu'à n termes.
```python
def suite_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        suivant = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(suivant)
    return fibonacci[:n]

# Exemple d'utilisation
print(suite_fibonacci(10))  # Sortie : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 7. **Compter les voyelles dans une chaîne de caractères**

Cette fonction utilise une boucle pour compter le nombre de voyelles dans une chaîne de caractères.

```python
def compter_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    compteur = 0
    for caractere in chaine:
        if caractere in voyelles:
            compteur += 1
    return compteur

# Exemple d'utilisation
print(compter_voyelles("Bonjour tout le monde!"))  # Sortie : 7
```
Remarque pour le français il faut utiliser une chaine voyelle un peu plus longue:
```python
voyelles = "aeiouAEIOUàèìòùÀÈÌÒÙáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛäëïöüÄËÏÖÜÿŸ"
````
Pour le polonais:
```python
voyelles = "aeiouyAEIOUYąęĄĘóÓ"
```

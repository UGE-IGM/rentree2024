Les fichiers ipynb de ce répertoire sont des TP notés (et leurs corrections) effectués en 2024 par les étudiants de L3 dans le cadre du cours d'algorithmique des graphes. 

Les étudiants sont censés maîtriser les algorithmes vus au cours et qui leur sont communiqués dans la feuille algorithmes.pdf (dont ils disposent pendant les TP et à l'examen). De nombreuses questions reviennent simplement à traduire en Python le pseudocode qui leur a été donné dans ces feuilles ou dans les exercices de TD. 

Les fichiers .py inclus leur sont fournis en cours d'années et implémentent des graphes (pondérés ou non, orientés ou non, ...) ou des structures de données utiles (union-find, heaps, ...). En l'état, ils ne couvrent pas encore toute la matière présentée ci-dessous.


# Parcours de graphes non orientés et applications
- implémentation des parcours classiques: largeur, profondeur
- détection des composantes connexes
- reconnaissance des graphes bipartis
- construction des arbres de parcours

# Arbres et forêts couvrantes de poids minimum
- algorithmes de Prim, Kruskal

# Plus courts chemins
- algorithme de Dijkstra pour les graphes sans poids négatifs
- algorithme de Bellman-Ford pour les graphes sans **cycles** négatifs
- algorithme de Floyd-Warshall pour les plus courts chemins entre chaque paire de sommets

# Graphes orientés
- tri topologique
- fermeture transitive
- détection des composantes fortement connexes

# Flots et applications
- algorithme d'Edmonds-Karp pour le calcul d'un flot maximum
- déduction d'une coupe de capacité minimum
- calcul d'un couplage dans un graphe biparti

# Programmation dynamique
- plus courts chemins dans les DAG

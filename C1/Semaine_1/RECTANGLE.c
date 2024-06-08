

// PL:title= Aire d'un rectange
/* PL:statement==

Ecrire un programme qui lit deux entiers la hauteur et la longeur d'un rectangle 
et calcule et affiche l'aire de ce rectangle.


PL:== */
// PL:code_before==
#include <stdio.h>
#include <stdlib.h>

// PL:==

// PL:soluce==
int main(int argc, char *argv[]) {
    int longueur, hauteur;
    if (argc == 3) {
    longueur = atoi(argv[1]);
    hauteur = atoi(argv[2]);
    printf("Aire du rectangle de longueur %d et de hauteur %d : %d\n", longueur, hauteur, longueur * hauteur);
    return 0;
    }
    else {
        scanf("%d %d", &longueur, &hauteur);
        printf("Aire du rectangle de longueur %d et de hauteur %d : %d\n", longueur, hauteur, longueur * hauteur);
        return 0;
    }
}
// PL:==
// PL:code_after==

// PL:==

/* PL:code==

int main(int argc, char *argv[]) {
    int longueur, hauteur;
    if (argc == 3) {
    longueur = atoi(argv[1]);
    hauteur = atoi(argv[2]);
    printf("Aire du rectangle de longueur %d et de hauteur %d : %d\n", longueur, hauteur, longueur * hauteur);
    return 0;
    }
    else {
        scanf("%d %d", &longueur, &hauteur);
        printf("Aire du rectangle de longueur %d et de hauteur %d : %d\n", longueur, hauteur, longueur * hauteur);
        return 0;
    }
}
PL:== */

/* PL:checks_args_stdin==
[['test1',[],"23 56\n"],
['test2',[],"16 17\n"],
['test aléatoire 1',[]," ".join([str(random.randint(1,100)) for i in range(2)])+"\n"],
['test aléatoire 2',[]," ".join([str(random.randint(1,100)) for i in range(2)])+"\n"],
['test aléatoire 3',[]," ".join([str(random.randint(1,100)) for i in range(2)])+"\n"]]
]
PL:== */


#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int nballoc = 0;
int totalsize = 0;
int nbrealloc = 0;
void *__dr_malloc(size_t s) {{  nballoc++; totalsize += s ; 
    return malloc(s); 
}}

void *__dr_realloc(void *ptr, size_t size){{
    nbrealloc++; 
    return realloc(ptr,size);
}}

#define malloc __dr_malloc
#define realloc __dr_realloc








int compare(int a, int b) {
    return a-b;
}

int *makeSortedCopie(int *t, int n) {
    int *t2= (int *) malloc(sizeof(int) * n);
    int i;
    for (i=0; i<n; i++) {
        t2[i]= t[i];
    }
    qsort(t2, n, sizeof(int), (int (*)(const void *, const void *))compare);
    return t2;
}


int *intersection(int *X, int n1, int *Y, int n2, int *n) {
    int *t= (int *) malloc(sizeof(int) * (n1<n2? n1: n2));
    int *t1= makeSortedCopie(X, n1);
    int *t2= makeSortedCopie(Y, n2);
    int i=0, j=0, k=0;
    for (i=0; i<n1 && j<n2;) {
            if (t1[i] == t2[j]) {
                t[k++]= t1[i];
                i++;j++;
            }  
            else if (t1[i] < t2[j]) {
                i++;
            }  
            else {
                j++;
            }
        }
    *n= k;
    free(t1);
    free(t2);
    return realloc(t, sizeof(int) * k);
}





int main(int c, char *v[]) {
    int n;
    int TAILLE= atoi(v[1]);
    int *t1= malloc(sizeof(int) * TAILLE);
    int *t2 = malloc(sizeof(int) * TAILLE);
    srand(TAILLE);
    for (int i=0; i<TAILLE; i++) {
    int r= rand() % 2 ;
        t1[i]= i*2 + r;
        t2[i]= i*2+TAILLE/2;
    }

    int *t= intersection(t1, TAILLE, t2, TAILLE, &n);
    for (int i=0; i< 100; i++) {
        printf("%d ", t[i]);
    } 

    return 0;
}



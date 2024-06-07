

/* code after typique */

int main(int argc,char **argv){
    int i;
    float f;
    char *s;
    /* traitement des parametres d'appel avec saut du nom de l'executable */
    while (*++argv){
        /* parametre entier */
        i=atoi(*argv);
        /* parametre float */
        f=atof(*argv);
        /* parametre chaine */
        s = *argv;

        /* faire quelque chose */
        student_fonction(i);
    }

    /** utilisation de l'entrée standard */
    while (scanf("%d %f %s",&i,&f,s)==3)
    {
        /* faire quelque chose */
        student_fonction(i,f,s);
    }
}



int main(int argc,char **argv){
 
/* traitement des parametres d'appel avec saut du nom de l'executable */
while (*++argv)
 {
    /* parametre entier */
    int i=atoi(*argv);
    /* parametre float */
    float f=atof(*argv);
    /* parametre chaine */
    char *s=*argv;

    /* faire quelque chose */
    student_fonction(i,f,s);
}

/** utilisation de l'entrée standard */
while (scanf("%d %f %s",&i,&f,s)==3)
{
    /* faire quelque chose */
    student_fonction(i,f,s);
}
}
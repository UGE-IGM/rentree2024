import multiprocessing
import subprocess
from foldable_feedback_utils import FoldableFeedbackContent

from fork_process_setitimer import runStudentCode

def subnlbybr(str):
    return "<br/>".join(str.split("\n"))

# Remove this ZONE

cflags = []
nb_attempt = 0
meta={}
meta['consumedHints']=0
editor={}
feedback={}
foldableFB={}
editor["code"] = """
int *intersection(int *t1, int n1, int *t2, int n2, int *n) {
    int *t= (int *) malloc(sizeof(int) * (n1<n2? n1: n2));
    int i=0, j=0, k=0;
    for (i=0; i<n1;i++)
        for(j=0;j<n2;j++)
            if (t1[i] == t2[j]) {
                t[k++]= t1[i];
            break;
            }
    *n= k;

    return realloc(t, sizeof(int) * k);
}
"""
code_before = "#include <unistd.h>\n#include <stdlib.h>\n"

code_after = ""
compiler="gcc"
compilerlineprof= "{compiler} {src_name} -o {prog_name}"
compilerlinestud= "{compiler} {src_name} -o {prog_name}"
taboo =" Y a rien de tabou dans cet exercice"
studentsrc = "src_student.c"
professeursrc = "src_prof.c"
studentexe =  "./studentex"
professeurexe = "./profex"
interpreteur = ""

nb_hints = 0







import random


introduction= f'''

Ecrire une fonction qui prend en parametre deux tableaux d'entiers.
Qui renvoie un tableau d'entiers contenant les éléments communs aux deux tableaux.
La fonction prend un pointeur sur un entier en paramètre qui contiendra la taille du tableau retourné.

Attention à la gestion de la mémoire.

La taille des tableaux peut être supérieur à 10^5. 
Si l'algorithme est de complexité quadratique, il ne passera pas les tests, trop long.

Vous pouvez utiliser la fonction qsort pour trier les tableaux.
Ne modifier pas les tableaux passés en paramètre.

Vous pouvez ecrire plusieurs fonctions pour décomposer votre travail.

```C 
    int *intersection(int *t1, int n1, int *t2, int n2, int *n) 
``` 

'''

soluce = f'''

int *intersection(int *t1, int n1, int *t2, int n2, int *n) {{
    int *t= (int *) malloc(sizeof(int) * (n1<n2? n1: n2));
    int i, j, k=0;
    for (i=0; i<n1; i++) {{
        for (j=0; j<n2; j++) {{
            if (t1[i] == t2[j]) {{
                t[k++]= t1[i];
                break;
            }}  
        }}
    }}
    *n= k;
    return realloc(t, sizeof(int) * k);
}}


'''


code_before = '''
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



'''

soluce = '''


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

'''

code_after = '''

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
'''

checks_args_stdin=''' [ ['Taille petit',["1000"], "",0.01],
    ['Aleatoire et grand',[str(randint(2000,40000))],"", 0.001]
]
'''

statement = introduction  
      



solution='''
int *intersection(int *t1, int n1, int *t2, int n2, int *n) {
    int *t= (int *) malloc(sizeof(int) * (n1<n2? n1: n2));
    int i=0, j=0, k=0;
    for (i=0; i<n1;i++)
        for(j=0;j<n2;j++)
            if (t1[i] == t2[j]) {
                t[k++]= t1[i];
            break;
            }
    *n= k;

    return realloc(t, sizeof(int) * k);
}

'''

# FIN DE ZONE

# Definitions de fonctions utiles
# Pre-process before executing the checks
def prepare_code_to_file(src_code, filename):
    """
    Place inside file named `filename`
    """
    src_final = code_before + "\n\n"
    src_final += src_code + "\n\n"
    src_final += code_after + "\n\n"
    with open(filename, 'w') as f:
        f.write(src_final)

def compile_source(compilerline,src_name, prog_name, compiler):
    """
    compile the source in argument and return 
    """
    command_args = compilerline.format(src_name=src_name,prog_name=prog_name, compiler=compiler)
    sp = subprocess.run(command_args.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    spout = sp.stdout.decode()
    errout = sp.stderr.decode()
    returncode = sp.returncode
    return (returncode, spout, errout)



nb_hints = meta['consumedHints']
# principals signals
signals = {
    2: "SIGINT",
    3: "SIGQUIT",
    4: "SIGILL",
    6: "SIGABRT",
    8: "SIGFPE",
    9: "SIGKILL",
    11: "SIGSEGV",
    13: "SIGPIPE",
    14: "SIGALRM",
    15: "SIGTERM"
};


# Update nb attempt
nb_attempt += 1 # count each try....


if __name__ == "__main__":

    # Prepare the code to be written in the professeur code
    prepare_code_to_file(soluce, professeursrc)

    FBcontent = FoldableFeedbackContent()

    # Compile the teacher solution
    returncode, spout, errout =compile_source(compilerlineprof,professeursrc,professeurexe, compiler)

    if len(spout) + len(errout) != 0 :
        grade_compil = 0
        text_compil = 'Compilation Prof Ratée'
        compil_state = 'error'
        class_state = 'error'
        FBcontent.add_feedback(
            name = "Compilation Prof Ratée ",
            display = class_state != "success",
            feedback_type = class_state,
            obtained = spout + errout
        )
    else:
        # Now we can compile the student proposition
        prepare_code_to_file(editor["code"], studentsrc)
        # Compile the student proposition
        returncode, spout, errout = compile_source(compilerlinestud,studentsrc,studentexe , compiler)
        # Compilation ok
        if len(spout) + len(errout) == 0:
            grade_compil = 100
            text_compil = 'Compilation réussie'
            compil_state = 'success'
            class_state = 'success'
        else:
            # Compilation Aborted
            if "error:" in errout:
                grade_compil = 0
                text_compil = 'Compilation échouée'+errout
                compil_state = 'error'
                class_state = 'error'
            # So there must have some warning
            else:
                nb_w_compil = (spout+errout).count('warning')
                grade_compil = max(0, 100 - (nb_w_compil*10) )
                text_compil = 'Compilation réussie avec ' + str(nb_w_compil) + ' warning'
                if nb_w_compil > 1:
                    text_compil += 's'
                compil_state = 'warning'
                class_state = 'warning'

        if "taboo" in globals():
            if taboo != "":
                import re
                taboo = taboo.strip()
                pat = re.compile(taboo, re.IGNORECASE)
                if pat.search(editor["code"]):
                    compil_state = 'taboo-error'
                    class_state = 'error'
                    text_compil = 'Compilation échouée non respect du taboo : '+taboo+' '
                    grade_compil = 0

        # begin of feedback

        #if "compile_feedback" in globals():
        FBcontent.add_feedback(
            name = "Compilation : " + str(grade_compil) + " %",
            display = class_state != "success",
            feedback_type = class_state
        )

        if compil_state == 'taboo-error':
            FBcontent.add_to_last_feedback(
                description = "Refus de compilation :\nNon respect du taboo : " + taboo
            )
        elif compil_state != 'success':
            FBcontent.add_to_last_feedback(
                description = text_compil + ' avec flags ' + ' '.join(cflags),
                obtained = spout + errout
            )
        else:
            FBcontent.add_to_last_feedback(
                description = text_compil + ' avec flags ' + ' '.join(cflags) + "\nC'était parfait, le compilateur n'a rien dit..."
            )

    # We replace the compil state to error to disable tests
    if compil_state == 'taboo-error':
        compil_state = 'error'

    # Tests
    nb_good = 0
    nb_bad = 0
    grade_checks = 0

    FBtests = FoldableFeedbackContent()

    # data test generation : must be in a separate place
    # since it need a new eval at each attempt to be really
    # random !!!
    from random import *
    checks_data = eval(checks_args_stdin)

    if compil_state != 'error':
        q=multiprocessing.Queue()
        for test_c in checks_data:
            f_in=open("stdin_content", "w")
            f_in.write(test_c[2])
            f_in.close()

            # Timeout 
            if len(test_c) == 4:
                timeout = float(test_c[3])
            else:
                timeout = 1

            # Use the teacher solution to generated expected output of the test
            command_args = " ".join([ interpreteur,professeurexe] + list(map(lambda x: "'"+str(x)+"'", test_c[1])) )
            sp = subprocess.run(command_args, stdin=open("stdin_content", "r"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=1)
            try: 
                expected_ouput = sp.stdout.decode() + sp.stderr.decode()
            except:
                expected_ouput = "Impossible de décoder la sortie standard"
            if -sp.returncode in signals:
                expected_ouput += "Process exited with UNIX signal ("+str(-sp.returncode)+") "+signals[-sp.returncode]
            elif sp.returncode < 0:
                expected_ouput += "Process exited with UNIX signal ("+str(-sp.returncode)+")"

            # Now execute the student programm
            command_args = " ".join([interpreteur,studentexe] + list(map(lambda x: "'"+str(x)+"'", test_c[1])) )
            
            runStudentCode(1,command_args,test_c[2],q)
            # sp = subprocess.run(command_args, stdin=open("stdin_content", "r"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=1)
        
        for test_c in checks_data:
            spout = q.get()


            if spout == expected_ouput:
                nb_good += 1
                XXX = " ".join([str(x) for x in test_c[1]])
                terminal_log = "Platon@debian~$> " + interpreteur+ " "+ professeurexe +" "+ XXX + "\n"
                if len(test_c[2]) > 0:
                    stdin_explain = "Contenu de l'entrée standard durant l'exécution : \n"
                    stdin_explain += subnlbybr(test_c[2])
                else:
                    stdin_explain = ""
                FBtests.add_feedback(
                    name = test_c[0],
                    description = stdin_explain,
                    expected = expected_ouput,
                    obtained = expected_ouput,
                    arguments = terminal_log,
                    display = False,
                    feedback_type = "success"
                )
            else:
                nb_bad += 1
                XXX = " ".join([str(x) for x in test_c[1]])
                terminal_log = "Platon@debian~$> " + interpreteur+ " " + studentexe +" "+ XXX + "\n"
                if len(test_c[2]) > 0:
                    stdin_explain = "Contenu de l'entrée standard durant l'exécution : \n"
                    stdin_explain += subnlbybr(test_c[2])
                else:
                    stdin_explain = ""
                FBtests.add_feedback(
                    name = test_c[0],
                    description = stdin_explain,
                    expected = expected_ouput,
                    obtained = spout,
                    arguments = terminal_log,
                    display = True,
                    feedback_type = "error"
                )

        grade_checks = min([((nb_good*100) // (nb_good+nb_bad)) , (100 // (2**nb_bad))])

    FBcontent.add_category(
        name = "Tests : " + str(grade_checks) + " %",
        display = grade_checks != 100,
        feedback_type = "success" if grade_checks == 100 else ("error" if grade_checks == 0 else "warning")
    )

    if compil_state == 'error':
        FBcontent.add_to_last_category(
            description = "Erreur à la compilation : Pas de test lancé"
        )
    else:
        FBcontent.add_to_last_category(
            feedbacks = FBtests
        )

    # Calcul de la partie : note d'autonomie

    if nb_hints > 0:
        count_hint = 0
        for e in hints.items:
            if 'consumed' in e:
                count_hint += 1
        grade_alone = 50 + (50*(nb_hints - count_hint) // (nb_hints))
        feedback["content"] += '<p style="margin-bottom: 5px; margin-top: 5px;"><b><u>Autonomie :</u> ' + str(grade_alone) + '%</b></p>'
        if count_hint == 0:
            feedback["content"] += '<div class="success-state" style="padding: 5px; border: 1px solid #155724 transparent;">'
            feedback["content"] += 'Sans indice</div>'
        else: 
            feedback["content"] += '<div class="warning-state" style="padding: 5px; border: 1px solid #155724 transparent;">'
            if count_hint == 1:
                feedback["content"] += '1 indice utilisé</div>'
            else:
                feedback["content"] += str(count_hint)+' indices utilisés</div>'
    else:
        grade_alone = 100

    grade_attempt = 50 + (200 // (3+nb_attempt))
    if grade_attempt < 100:
        FBcontent.add_feedback(
            name = "Efficacité : " + str(grade_attempt) + " %"
        )

    if nb_attempt == 1:
        FBcontent.add_to_last_feedback(
            description = "1 tentative",
            display = False,
            feedback_type = "success"
        )
        all_grade = [(grade_compil * grade_checks * grade_attempt * grade_alone) // 1000000]
    else:
        FBcontent.add_to_last_feedback(
            description = str(nb_attempt) + " tentatives",
            display = True,
            feedback_type = "warning"
        )
        all_grade.append((grade_compil * grade_checks * grade_attempt * grade_alone) // 1000000)

    # overall grade !
    feedback["content"] = 'Note actuelle : ' + str(max(all_grade)) + ' / 100'
    foldableFB["content"] = FBcontent.get()

    grade = (grade_compil * grade_checks * grade_attempt * grade_alone) // 1000000

    ## END OF GRADING SCRIPT

    print(feedback["content"])
    print(foldableFB["content"])



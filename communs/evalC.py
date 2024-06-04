
import subprocess

# Cree un expression cf expreesion

def evalC(exp):
    txt = f"""

    #include <stdio.h>
    #include <string.h>

    int main(void)
    {{
        int a = 0, b = 0, tab[10], i = 0, *p = NULL;
        char *chaine = "Bonjour";
        int len_chaine = strlen(chaine);
        printf("%d", (int)({exp}));
        return 0;
    }}

    """

    with open("/tmp/code.c", "w") as f:
        f.write(txt)

    subprocess.run(["gcc","/tmp/code.c","-o","/tmp/exe"])
    subprocess.run(["/tmp/exe"], stdout=open("/tmp/val","w") )
    with open("/tmp/val","r") as f:
        val = int(f.read())

    return val

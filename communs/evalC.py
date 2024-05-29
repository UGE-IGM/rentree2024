
import subprocess

# Cree un expression cf expreesion

exp = ' -3 + 5 '
def evalC(exp):
    txt = f"""

    #include <stdio.h>


    int main(int argc, char const *argv[])
    {{
        printf("%d",(int)({exp}));
        return 0;
    }}

    """

    with open("/tmp/code.c","w") as f:
        f.write(txt)

    subprocess.run(["gcc","code.c","-o","/tmp/exe"])
    subprocess.run(["/tmp/exe"],stdout=open("val","w") )
    with open("val","r") as f:
        val = int(f.read())

    return val

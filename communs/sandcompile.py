

import py_compile 
import pprint
import json
def compile_file(file):
    try:
        print("compiling")
        py_compile.compile(file)
        
        return True, None

    except SyntaxError as e:
        pprint(json.dump(e.__dict__, indent=4))
        return False, e

if __name__ == "__main__":
    import sys
    for f in sys.argv[1:]:
        x,t = compile_file(f)
        if x :
            print(f, "compiled")
        else:
             pprint(json.dump(t.__dict__, indent=4))
    print("done")


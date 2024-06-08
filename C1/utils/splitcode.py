
#*****************************************************************************
#  Copyright (C) 2023 Dominique Revuz < dominique dot revuz at univ-eiffel . fr>
#
#  Distributed under the terms of Creative Commons Attribution-ShareAlike 3.0
#  Creative Commons CC-by-SA 3.0
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  The full text of the CC-By-SA 3.0 is available at:
#
#            https://creativecommons.org/licenses/by-sa/3.0/
#            https://creativecommons.org/licenses/by-sa/3.0/fr/
#*****************************************************************************

# copyright dominique  Revuz 2023 

import re
import sys

ERROR="no"

LISTOFVARIABLES=['OPTION', 'title', 'code_before', 'statement', 'solution', 'code_after', 'checks_args_stdin']

debug = False

def splitLine(line):
    line = line.strip()
    name,value = line[6:].split("=",1)
    name = name.strip()
    value = value.strip()

    return name,value

def splitcode(arg):
    state = None
    dict={"error":ERROR}
    with open(arg,"r") as f:
        for line in f.readlines():
            if state == None:
                if line.startswith("/* PL:title=") and line.endswith(" */\n"):
                    dict['title']= line[6+7:-4]
                elif line.startswith("// PL:title="):
                    dict['title']= line[6+7:-1]
                elif line.startswith("// PL:") and not "==" in line:
                    name,value = splitLine(line)
                    dict[name]= value
                elif line.startswith("/* PL:"):
                    state= "info"
                    name =  (line.strip())[6:-2]
                    if debug : print(f"Starting info state :<{name}>")
                    multi="\n"
                elif line.startswith("// PL:"):
                    state= "code"
                    name =  line[6:-3]
                    if debug : print(f"Starting code state :<{name}>")
                    multi="\n"
                continue                
            elif state == "info":        
                if line.startswith("PL:== */"):
                    dict[name]= multi
                    state=None
                    multi=""
                    if debug : print(f"Closing info state :<{name}>")
                else:
                    multi +=  line
            else:     
                if line.startswith("// PL:=="):
                    if debug : print(f"Closing {state} state :<{name}>")
                    dict[name]= multi
                    state=None
                else:
                    multi +=  line

    return(dict)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: splitcode.py [--debug] [file ...] ")
        sys.exit(1)
    errors = ""
    for filename in sys.argv[1:]:
        if filename == "--debug":
            debug = True
            continue
        dico = splitcode(filename)
        for i in LISTOFVARIABLES:
            if not i in dico:
                errors += f" '{i}' variable not defined in {filename}\n"

        if errors:
            print(f"Error while reading the file {filename}\n"+ errors, file=sys.stderr)
            errors = "\n"

    if errors:
        sys.exit(1)

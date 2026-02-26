import argparse
import keyboard
import re

# menn v1.0.0
# forked from enn v1.2.4
# made by las-r on github, mit license

# helper functions
def getVar(v):
    if v in var: 
        return var[v]
    else: 
        return 0
def checkName(v):
    if any(c in v for c in ["=", ";", " ", "<", ">"]) or v in ["0", "1"]:
        return
    else:
        return v

# argument parsing
parser = argparse.ArgumentParser(
    prog="menn",
    description="Menn v1.0 - A minimal logic-oriented esolang."
)
parser.add_argument("filename", help="Program file to run")
args = parser.parse_args()

# parse file
pname = args.filename
with open(pname) as pfile: 
    prog = pfile.read()
prog = re.sub(r'\/.*?\/', '', prog)
prog = prog.replace("\n", "").replace(" ", "")
lprog = [p for p in prog.split(";") if p]

# program loop
var = {"0": 0, "1": 1}
try:
    running = True
    while running:
        for i, p in enumerate(lprog):
            # variables
            if p[-1] == "=":
                if p[:-1] not in var: 
                    var[checkName(p[:-1])] = 0; #type: ignore
            
            elif "=" in p:
                q = p.split("=")
                qa = q[1].split(",")[0]
                qb = q[1].split(",")[1]
                var[checkName(q[0])] = int(not (getVar(qa) and getVar(qb))) #type: ignore
        
            # output       
            elif p[0] == ">":
                if p[1:]: 
                    print(getVar(p[1:]), end="", flush=True)
                else: 
                    print()
    
except KeyboardInterrupt:
    keyboard.unhook_all()

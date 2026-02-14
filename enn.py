import re
import sys
import time

# enn v1.0
# made by las-r on github, mit license

# helper functions
def getVar(v):
    if v in var: return var[v]
    else: return 0

# open file
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)
if len(sys.argv) > 2: wait = float(sys.argv[2])
else: wait = 0

# parse file
pname = sys.argv[1]
with open(pname) as pfile: prog = pfile.read()
prog = re.sub(r'\/.*?\/', '', prog)
prog = prog.replace("\n", "").replace(" ", "")
print(prog)
prog = [p for p in prog.split(";") if p]

# program loop
var = {0: 0, 1: 1}
b = False
while True:
    for i, p in enumerate(prog):
        if p[-1] == "=":
            if p[:-1] not in var: var[p[:-1]] = 0b0;
                
        elif "=" in p:
            q = p.split("=")
            qa = q[1].split(",")[0]
            qb = q[1].split(",")[1]
            var[q[0]] = int(not (getVar(qa) and getVar(qb)))
    
        elif p[0] == ">":
            if p[1:]: print(getVar(p[1:]), end="", flush=True)
            else: print()
            
        else:
            if p in var: 
                if getVar(p): var[p] = 0
                else: var[p] = 1
        
    time.sleep(wait)
    if b: break

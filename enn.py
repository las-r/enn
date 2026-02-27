import argparse
import keyboard
import re
import time

# enn v1.2.6
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
    prog="enn",
    description="Enn v1.2.5 - A logic-oriented esolang."
)
parser.add_argument("filename", help="Program file to run")
parser.add_argument(
    "-w", "--wait",
    type=float,
    default=0,
    help="Delay between execution cycles (seconds)"
)
parser.add_argument(
    "-o", "--once",
    action="store_true",
    help="Run program once instead of looping forever"
)
parser.add_argument(
    "-d", "--debug",
    action="store_true",
    help="Print variable state after each cycle"
)
parser.add_argument(
    "-ne", "--no-ext",
    action="store_true",
    help="Do not automatically append .enn"
)
parser.add_argument(
    "-m", "--minify",
    action="store_true",
    help="Create a minified version of the program"
)
parser.add_argument(
    "-v", "--version",
    action="version",
    version="Enn v1.2.5"
)
args = parser.parse_args()
wait = args.wait

# parse file
if args.no_ext:
    pname = args.filename
else:
    pname = args.filename if args.filename.endswith(".enn") else args.filename + ".enn"
with open(pname) as pfile: 
    prog = pfile.read()
prog = re.sub(r'\/.*?\/', '', prog)
prog = prog.replace("\n", "").replace(" ", "")
lprog = [p for p in prog.split(";") if p]

# minify
if args.minify:
    si = pname.rfind(".")
    mna = pname[:si]
    ext = pname[si:]
    mname = mna + ".min" + ext
    with open(mname, "x") as mfile:
        mfile.write(prog)

# program loop
var = {"0": 0, "1": 1}
try:
    running = True
    while running:
        for i, p in enumerate(lprog):
            # variable set
            if p[-1] == "=":
                if p[:-1] not in var: 
                    var[checkName(p[:-1])] = 0; #type: ignore
                
            elif "=" in p:
                q = p.split("=")
                qa = q[1].split(",")[0]
                qb = q[1].split(",")[1]
                var[checkName(q[0])] = int(not (getVar(qa) and getVar(qb))) #type: ignore
        
            # output
            elif p.startswith(">>"):
                c = p[2:].split(",")
                x = ""
                for bit in c:
                    x += str(getVar(bit))
                if len(x) == 8:
                    b = int(x, 2)
                    d = b.to_bytes(len(x) // 8, "big").decode("utf-8")
                    print(d, end="", flush=True)
                    
            elif p[0] == ">":
                if p[1:]: 
                    print(getVar(p[1:]), end="", flush=True)
                else: 
                    print()
            
            # input        
            elif p[0] == "<":
                if p[1:]:
                    var[p[1:]] = int(keyboard.is_pressed("space"))
                else:
                    while not keyboard.is_pressed("space"):
                        time.sleep(0.01)
            
            # toggle
            else:
                if p in var:
                    var[p] = 1 - getVar(p)
        
        if args.debug:
            print("\n[DEBUG]", var)
        if args.once:
            running = False
        time.sleep(wait)
    
except KeyboardInterrupt:
    keyboard.unhook_all()

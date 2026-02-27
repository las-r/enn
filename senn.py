from collections import defaultdict
import argparse
import keyboard
import re
import time

# senn v1.0.0
# forked from enn v1.2.4
# made by las-r on github, mit license

# memory and pointer initialization
stk = defaultdict(int)
ptrs = {",": 0, ".": 0, "?": 0}

# helper functions
def getPtrVal(pchar):
    if pchar == "1":
        return 1
    elif ptrs[pchar] in stk: 
        return stk[ptrs[pchar]]
    else: 
        return 0

# argument parsing
parser = argparse.ArgumentParser(
    prog="senn",
    description="Senn v1.0 - A stack-based logic-oriented esolang."
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
    help="Print pointer and tape state after each cycle"
)
parser.add_argument(
    "-ne", "--no-ext",
    action="store_true",
    help="Do not automatically append .snn"
)
parser.add_argument(
    "-v", "--version",
    action="version",
    version="Senn v1.0"
)
args = parser.parse_args()
wait = args.wait

# parse file
if args.no_ext:
    pname = args.filename
else:
    pname = args.filename if args.filename.endswith(".snn") else args.filename + ".snn"

try:
    with open(pname) as pfile: 
        prog = pfile.read()
except FileNotFoundError:
    print(f"File {pname} not found.")
    exit()

# cleanup comments and whitespace
prog = re.sub(r'\/.*?\/', '', prog, flags=re.DOTALL)
prog = "".join(prog.split())
lprog = [p for p in prog.split(";") if p]

# program loop
try:
    running = True
    while running:
        for p in lprog:
            # pointer movement
            if ('+' in p or '-' in p) and p[0] in ",.?":
                move = p.count('+') - p.count('-')
                ptrs[p[0]] += move
                
            # pointer toggle
            if len(p) == 1 and p[0] in ",.?":
                stk[ptrs[p[0]]] = int(not bool(getPtrVal(p[0])))
        
            # ascii output
            elif p.startswith(">>"):
                saddr = ptrs[p[2:]]
                x = ""
                for i in range(8):
                    x += str(stk[saddr + i])
                b = int(x, 2)
                d = chr(b)
                print(d, end="", flush=True)
                    
            # bit output
            elif p.startswith(">"):
                if len(p) > 1:
                    print(getPtrVal(p[1:]), end="", flush=True)
                else:
                    print()
            
            # input        
            elif p[0] == "<":
                if p[1:]:
                    stk[ptrs[p[1:]]] = int(keyboard.is_pressed("space"))
                else:
                    while not keyboard.is_pressed("space"):
                        time.sleep(0.01)
                
            # nand operation
            elif len(p) == 3 and all(c in ",.?" for c in p):
                tgt, i1, i2 = p[0], p[1], p[2]
                stk[ptrs[tgt]] = int(not (getPtrVal(i1) and getPtrVal(i2)))
        
        if args.debug:
            mem_view = {k: v for k, v in stk.items() if v != 0 or k in ptrs.values()}
            print(f"\n[DEBUG] Pointers: {ptrs} | Tape: {dict(sorted(mem_view.items()))}")
            
        if args.once:
            running = False
        if wait > 0:
            time.sleep(wait)
    
except KeyboardInterrupt:
    keyboard.unhook_all()

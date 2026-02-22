# Enn: Executable NAND Network
A logic-oriented esolang.

## How Enn works
Every instruction in Enn does 1 of 4 things:
- Set a variable
- Output a variable
- Toggle a variable
- Check for input

The only computation given to you is the ability to use NAND (and also NOT, technically).

**IMPORTANT NOTE:** Every program loops by default. To end a program, you must forcequit it, or use the `--once` argument.

## Usage
**REQUIREMENTS:** Python v3.x + [keyboard](https://pypi.org/project/keyboard/) + [argparse](https://pypi.org/project/argparse/)

```
python enn.py program [options]
```

If `.enn` is not included, it will be appended automatically.

### Arguments _(v≥1.2)_
**`-w <seconds>`, `--wait <seconds>`**\
Delay between execution cycles.\
Default: `0`
```
python enn.py program -w 0.1
```

**`-o`, `--once`**\
Run the program once instead of looping forever.
```
python enn.py program --once
```

**`-d`, `--debug`**\
Print variable state after each execution cycle.
```
python enn.py program --debug
```

**`-ne`, `--no-ext`**\
Do not automatically append `.enn` to the filename.
```
python enn.py program.txt --no-ext
```

**`-m`, `--minify` _(v≥1.2.3)_**\
Create a minified version of the program as `program.min.enn`
```
python enn.py program.enn --minify
```

**`-v`, `--version`**\
Display interpreter version.
```
python enn.py --version
```

## Syntax
### Basic Guidelines
- Line breaks, indentation, and trailing spaces do not matter.
- Every instruction should be ended with `;`.
- Comments are padded with `/`.
- Variable names cannot include spaces or use the following characters: `=, l, <, >`
  - Variable names also cannot be `0` or `1`

### Commands
#### Set a variable
Variables are bits.

`q` is the name of the variable.
```
q=;
```
Variable `q` is set to `w` NAND `e`. This is the only logic you can use.
```
q=w,e;
```
You can also use direct values.
```
q=w,0;
```
#### Toggle a variable
`q` is toggled between `0` and `1`.
```
q;
```
#### Output a value
`q` is outputted to the console. Variable outputs are inline.
```
>q;
```
An output symbol with no variable is a newline.
```
>;
```
Two output symbols is an ASCII/UTF-8 output. _(v≥1.2)_
```
>>q,w,e,r,t,y,u,i,o,p;
```
#### Input a value _(v≥1.1)_
Inputs can only pull from the spacebar.

`k` is set to whether the spacebar is actively being pressed or not.
```
<k;
```
An input symbol with no variable pauses the program until the spacebar is pressed.
```
<;
```

## Computational Class
Enn can be defined as a Bounded Storage Machine (BSM).

### Proof
To categorize Enn as a Bounded Storage Machine, we must show that its computational power and memory constraints align with the formal definition of a BSM: _a system with a finite, fixed number of bits and a transition function that maps current states to future states_.

#### 1. Memory Constraints
An Enn program's memory is defined by the variable defined in it's source code. Because variables cannot be dynamically created and/or remove during runtime, the total amount of bits (n) the memory has is determined at the program's creation.

#### 2. Transition Function
Enn directly implements the NAND operation, and the toggle command is effectively a NOT operation. Because programs loop by default, variables can act as latches, allowing the program to maintain a "state" over time.

#### 3. Functional Completeness
Enn uses the NAND gate as its primary function. In digital logic, NAND is universal, meaning it can be used to reconstruct any other logic. Any boolean function can be constructed using only NAND gates, making Enn capable of representing any digital asynchronous circuit that fits in n bits.

#### 4. Comparison to Turing Machines
Enn's memory is bounded, placing it in the same complexity class as a Finite State Automaton (FSA). Turing Machines require an infinite memory (tape), which Enn is incapable of producing.

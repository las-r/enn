# Enn: Executable NAND Network
A logic-oriented esolang.

## How Enn works
Every instruction in Enn does 1 of 4 things:
- Set a variable
- Output a variable
- Toggle a variable
- Check for input

The only computation given to you is the ability to use NAND.

**IMPORTANT NOTE:** Every program loops by default. To end a program, you must forcequit it, or use the `--once` argument.

## Usage
**REQUIREMENTS:** Python v3.x + [keyboard](https://pypi.org/project/keyboard/) + [argparse](https://pypi.org/project/argparse/)

```
python enn.py program [options]
```

If `.enn` is not included, it will be appended automatically.

### Options _(v≥1.2)_
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
`k` is set to whether the spacebar is actively being pressed or not.
```
<k;
```
An input symbol with no variable pauses the program until the spacebar is pressed.
```
<;
```

That's it, really.

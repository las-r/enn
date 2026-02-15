# Enn: Executable NAND Network
A logic-oriented esolang.

## How Enn works
Every instruction in Enn does 1 of 2 things:
- Set a variable
- Output a variable
- Check input

The only computation given to you is the ability to use NAND.

**IMPORTANT NOTE:** Every program loops. To end a program, you must forcequit it.

## Usage
**REQUIREMENTS:** Python v3.x

Simply place `enn.py` in the same directory as your program and run it using `enn.py PROGRAM[.enn] [CYCLE WAIT TIME]`.

## Syntax
### Basic Guidelines
- Every instruction should be ended with `;`.
- Spaces, lines, and indentation does not matter.
- Variable names can use any character besides `=`, `>`, and `;`.
- Comments are padded with `/`.

### Commands
#### Create a variable
`q` is the name of the variable.
```
q=;
```
#### Use a NAND gate
Variable `q` is set to `w` NAND `e`.
```
q=w,e;
```
You can also use direct values.
```
q=w,0;
```
#### Output a value
`q` is outputed to the console. Variable outputs are inline.
```
>q;
```
An output symbol with no variable is a newline.
```
>;
```
#### Input a value
`k` is set to whether the spacebar is actively being pressed or not.
```
<k;
```
An input symbol with no variable pauses the program until the spacebar is pressed.
```
<;
```

That's it, really.

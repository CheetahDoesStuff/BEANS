# Developement In BEANS

## Setup

This project require you to have [uv](https://docs.astral.sh/uv/) and [git](https://git-scm.com/) preinstalled.

Currently BEANS code is executed through a file in the repo itself, so youll need to clone the repo:

`git clone https://github.com/BravestCheetah/BEANS`

Then running code is incredibly simple:

`uv run exec.py path/to/code.bean`

But, how do you actually write code?

## Writing Code

First of all, create your code file, ending in .bean

Before we start, lets go over the different argument types:

* INT 

An normal integer, defined by writing the prefix "i" before an number, like this: `i32`

* BIN

A normal binary number, defiined by writing prefix "b" before an number, like this: `b01010101`

* Register Adress

A Register adress defined by writing the prefix "r" before an number, like this: `r5`

* Memory Adress

A Memory adress defiined by wriiting the prefix "m" before the number, like this: `m12`

Now, lets write some code! Let me go over a simple example computing 1+1!
Here is the code:
```beans
LDI r0 i1
ADD r0 r0 r1
HALT
```

Lets go over the code

**NOTE: this program is also availble [here](https://github.com/BravestCheetah/BEANS/blob/main/examples/add2numbers.bean)**

* `LDI r0 i1` - Loads the number 1 into register 0
* `ADD r0 r0 r1` - Adds the number in register 0 with itself and saving the result into register 1
* `HALT` - Stops the program

Now, if you ran this code using the program you should see that the result of 1+1 is stored in register 1.

This is a very simple example and more examples can be found [here.](https://github.com/BravestCheetah/BEANS/tree/main/examples)
But, lets at least go over the list of instructions and what they do.

## Instructrions

| Instruction | Arguments | Explanation | Example |
|-------------|-----------|-------------|---------|
| **Data** |  |  |  |
| LDI | reg, int | Loads the integer into the register provided | [add2numbers.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/add2numbers.bean) |
| STR | mem, reg | Stores the data of the register provided into the memory adress provided | Coming soon |
| LOAD | mem, reg | Loads the value of the memory adress provided into the register provided | Coming soon |
| - |  |  |  |
| **Arithemtic** |  |  |  |
| ADD | reg 1, reg 2, reg 3 | stores the result of reg 1 + reg 2 into reg 3 | [add2numbers.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/add2numbers.bean) |
| SUB | reg 1, reg 2, reg 3 | stores the result of reg 1 - reg 2 into reg 3 | Works the same as ADD |
| - |  |  |  |
| **Bitwise** |  |  |  |
| bOR | reg 1, reg 2, reg 3 | stores the result of reg 1 bitwise OR reg 2 into reg 3 | [bitwiseOperations.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/bitwiseOperations.bean) |
| bOR | reg 1, reg 2, reg 3 | stores the result of reg 1 bitwise XOR reg 2 into reg 3 | [bitwiseOperations.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/bitwiseOperations.bean) |
| bAND | reg 1, reg 2, reg 3 | stores the result of reg 1 bitwise AND reg 2 into reg 3 | [bitwiseOperations.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/bitwiseOperations.bean) |
| bNOT | reg 1, reg 2 | stores the result of bitwise NOT of reg 1 into reg 2 | [bitwiseOperations.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/bitwiseOperations.bean) |
| LSHFT | reg 1, reg 2, reg 3 | Shifts the bits in reg 1 left by reg 2 steps and stores it into reg 3 | [bitwiseOperations.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/bitwiseOperations.bean) |
| RSHFT | reg 1, reg 2, reg 3 | Shifts the bits in reg 1 right by reg 2 steps and stores it into reg 3 | [bitwiseOperations.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/bitwiseOperations.bean) |
| - |  |  |  |
| **IO System** |  |  |  |
| LDIO | int, int, int, mem, mem | see [io_modules.md](https://github.com/BravestCheetah/BEANS/blob/main/docs/io_modules.md) | [io_modules.md](https://github.com/BravestCheetah/BEANS/blob/main/docs/io_modules.md) |
| **Misc** |  |  |  |
| HALT |  | Stops the program no matter where in the file its placed | [add2numbers.bean](https://github.com/BravestCheetah/BEANS/blob/main/examples/add2numbers.bean) |
| TEST |  | Simply prints to the console output, used for interpreter developement purpouses. | Not needed |





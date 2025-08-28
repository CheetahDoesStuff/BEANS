# BEANS IO Modules
**NOTE: Throughout this file, the phrase "BIOMod" is used, "BIOMod" simply refers to BEANS IO Module**

## Installing BIOMods
**Currently, only manual installation is avalible!**

### Manual Installation

TODO: Add IO Dev Docs and Module List and update these links
TODO: Develop modules

First, youll need an BIOMod, you can refrence the [Module Developement Documentation](https://about.blank/) but you can also find modules in the [Official Module List](https://about.blank/)

Then youll have to locate your platforms module directory, when running beans youll get an output similar to this:
```
2025-08-25 19:04:30 ( BEANS ) | [INFO] -------- BEANS ---------
2025-08-25 19:04:30 ( BEANS ) | [INFO]  - Beans Is Initializing - 
2025-08-25 19:04:30 ( BEANS ) | [INFO]  - Beans IO Path: /home/cheetah/.local/share/BEANS/BIOMods - 
2025-08-25 19:04:30 ( BEANS ) | [INFO] -------- BEANS ---------
```
Where the outputed BEANS IO Path is the path we are looking for.

Now that we have both our BIOMod and the path to our Module directory, well move our BIOMod (which should be a python file) to our Module directory. But before we proceed we have to make sure of some things about the module file so we can actually use it:

- The name of the file should only be 3 letters long (not including .py)
- The name of the file has to only contain valid characters in the default ascii character set
- The file isnt in some subdirectory of the BIOMods folder

Alright, now you should be all set! To learn how to use these BIOMods, please refer to the next section.

## Importing and using BIOMods

### Loading the BIOMod

You can load the BIOMod by using the bult in LDIO operation, it takes in 5 arguments, grouped into 2 groups:
- Group 1: Int, Int, Int
  
  This group contains 3 integers which when handled will be translated into a string made out of 3 characters following the ascii set.
  This is the BIOMod ID, which in other terms is the name of the BIOMod python file (eg. TST.py would be the values 84 - T, 83 - S, 84 - T)
  
- Group 2: Mem, Mem

  This group contain 2 memory adresses, these are used to specify a range of which the IO module will be mapped to (To learn what memory mapping is, please read the next section). For example "m1 m4" would translate to "m1, m2, m3, m4". Note that its recommended to map your Modules to memory adresses that you dont use outside of communicating to the module as the module can accidentally overwrite stored data.

So a full call would be formatted like this: `LDIO 84 83 84 m1 m4`

### Using the BIOMod

The Module system uses a memory mapped architecture which means you map the Module to have read and write access to some of your memory adresses specified in group 2 of the argument. Note that different modules require different amounts of adresses to function properly and they do have the ability to error and exit the program at any time.

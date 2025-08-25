# BEANS IO Modules
**NOTE: Throughout this file, the phrase "BIOMod" is used, "BIOMod" simply refers to BEANS IO Module**

## Installing BIOMods
**Currently, only manual installation is avalible!**

### Manual Installation
First, youll need an BIOMod, you can refrence the [Module Developement Documentation](https://about.blank/) but you can also find modules in the [Official Module List](https://about.blank/)

Then youll have to locate your platforms module directory, when running beans youll get an output similar to this:
```
2025-08-25 19:04:30 ( BEANS ) | [INFO] -------- BEANS ---------
2025-08-25 19:04:30 ( BEANS ) | [INFO]  - Beans Is Initializing - 
2025-08-25 19:04:30 ( BEANS ) | [INFO]  - Beans IO Path: /home/cheetah/.local/share/BEANS/BIOMods - 
2025-08-25 19:04:30 ( BEANS ) | [INFO] -------- BEANS ---------
```
Where the outputed BEANS IO Path is the path we are looking for.

Now that we have both our BIOMod and the path to our Module directory, well move our BIOMod (whiich should be a python file) to our Module directory. But before we proceed we have to make sure of some things about the module file so we can actually use it:

- The name of the file should only be 3 letters long (not including .py)
- The name of the file has to only contain valid characters in the default ascii character set
- The file isnt in some subdirectory of the BIOMods folder
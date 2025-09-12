# Advanced Usage 
*to use something to the fullest, you gotta use all it offers*

Lets go over how to use and read the CLI and GUI of the Interpreter. Well go over how to execute your code, customize the BEANS VM instance and read the debug and info values presented in the GUI.

## The CLI
*Im a linux dude, ofc its gonna be a cli*

The CLI is the main way of executing your BEANS code. There are other ways (by importing functions and running the directly), but its not recommended as it may in most cases cause errors or unintended behaviour (aka dont do that, thats why i made the cli lmao)

### Using the cli (beans command)
*to utilize means to use something.*

The base cli requires one argument, the file to execute. Note that there are more flags and optional arguments for customizing the interpreter and the VM. But as those are optional lets go over the simplest command you can call, running a file with default settings. If you dont know how to execute files, please refer to the [developement documentation](https://github.com/CheetahDoesStuff/BEANS/blob/main/docs/developement.md).

Here is the most basic command you can run:

`beans my_file.bean`

But there is a lot of flags and arguments, so lets go over them!

### cli arguments

* `-p` / `--module-path`
  A custom path specifying where the interpreter should look for IO modules. Learn more in the [IO Module Usage Manual](https://github.com/CheetahDoesStuff/BEANS/blob/main/docs/io_modules.md)
  Default: Automatically set to your systems data path. Refer to the IO Module Usage Manual to learn how to view your specific path.

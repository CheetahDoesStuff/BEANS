from BEANS.interpreter.memory.registers import registers
from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.operation_handler import execute_operation

def parse_args(args: list[str]) -> list:
    
    parsed = []

    for arg in args:
        if arg.startswith("r"):
            parsed.append(("reg", int(arg[1:])))
        
        elif arg.startswith("m"):
            parsed.append(("mem", int(arg[1:])))

        elif arg.startswith("i"):
            parsed.append(("int", int(arg[1:])))
        
        elif arg.startswith("b"):
            parsed.append(("bin", int(arg[1:], 2)))
        
    return parsed

def interpret_line(line: str, regs: registers, mem: memory, pc_index: int):
    code = line.split(' ')
    return execute_operation(code[0], (regs, mem), parse_args(code[1:]), pc_index)
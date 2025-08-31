from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers

from BEANS.interpreter.op_api import handle_args


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore

        args = handle_args(args, ["reg", "reg", "reg"])

        value = mem[0].read(args[0]) - mem[0].read(args[1])
        mem[0].write(args[2], value)

        return pc_index + 1
from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers

from BEANS.interpreter.op_api import handle_args


class operation:
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore

        args = handle_args(args, ["mem" ,"reg"])

        mem[1].write(args[0], mem[0].regs[args[1]])

        return pc_index + 1
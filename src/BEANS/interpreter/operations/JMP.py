from src.BEANS.interpreter.memory.memory import memory
from src.BEANS.interpreter.memory.registers import registers

from src.BEANS.interpreter.op_api import handle_args


class operation:

    @staticmethod
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore
        args = handle_args(args, ["reg", "num"])
        
        value = mem[0].read(args[0])
        if value == 0:
            return args[1]

        return pc_index + 1
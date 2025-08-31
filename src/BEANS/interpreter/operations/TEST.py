from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers

from BEANS.interpreter.op_api import handle_args


class operation:

    @staticmethod
    def execute_operation(mem: tuple[registers, memory], args, pc_index): # type: ignore
        handle_args(args, [])
        
        print(f"TEST got called!")
        return pc_index + 1
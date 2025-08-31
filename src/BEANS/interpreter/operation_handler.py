from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers

import importlib, pathlib, os
import sys

OPERATIONS_FOLDER = pathlib.Path(__file__).parent / "operations"
sys.path.insert(0, os.path.abspath("."))

_operations_cache = {} # Store Operation Cache So You Only Have To Load Modules Once

def _load_operations():
    global _operations_cache

    if _operations_cache:
        return _operations_cache
    
    for file in pathlib.Path(OPERATIONS_FOLDER).iterdir():
        if file.name.endswith(".py"):
                mod_name = file.name[:-3]
                module = importlib.import_module(f"src.BEANS.interpreter.operations.{mod_name}")

                _operations_cache[mod_name.upper()] = module
            
    return _operations_cache

def execute_operation(operation: str, mem: tuple[registers, memory], args: list, pc_index: int):
    operations = _load_operations()
    operation = operation.upper()

    if operation in operations:
        operation_class = getattr(operations[operation], "operation")
        return operation_class.execute_operation(mem, args, pc_index)
    
    else:
        raise ValueError(f"Operation '{operation}' could not execute: not found")
from BEANS.interpreter.memory.registers import registers, register

class memory():
    def __init__(self, mem_size: int, mem_reg_size: int):
        self.memory = registers(mem_reg_size, mem_size)
    
    def read(self, address: int):
        return self.memory.read(address)
    
    def write(self, adress: int, val_reg: register):
        self.memory.write(adress, val_reg.value())
    
from BEANS.interpreter.memory.memory import memory

class restricted_memory:
    def __init__(self, memory: memory, access_adresses: list) -> None:
        self.mem = memory
        self.access_adresses = access_adresses

    def read(self, adress: int) -> int:

        if adress in self.access_adresses:
            return self.mem.read(adress)
        else:
            return 0
    
    def write(self, adress: int, value: int):
        
        if adress in self.access_adresses:
            self.mem.memory.write(adress, value)
        
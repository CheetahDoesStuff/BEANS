from sys import argv
import sys
import signal
import os
from pathlib import Path
from time import perf_counter

from BEANS.BEANS_GUI.gui import BEANSGui
from BEANS.interpreter.interpreter import interpret_line
from BEANS.interpreter.memory.memory import memory
from BEANS.interpreter.memory.registers import registers
from BEANS.data import data

from usefullog.logger import Logger
from platformdirs import user_log_dir

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication

class BEANSExecutor:
    def __init__(self, path, gui: BEANSGui, logger: Logger, mem: memory, regs: registers):
        self.code_path = path
        self.gui = gui
        self.logger = logger
        self.mem = mem
        self.regs = regs

        with open(self.code_path, "r") as f:
            self.lines = f.readlines()

        self.index = 0


    def get_data(self) -> tuple[str, str]:

        reg_data = ""
        for reg in self.regs.regs:
            value = str(reg.val) + " "
            if len(value) == 2:
                value = "0" + value
            
            reg_data += value


        mem_data = ""
        for reg in self.mem.memory.regs:
            value = str(reg.val) + " "
            if len(value) == 2:
                value = "0" + value

            mem_data += value

        mem_values = [f"{int(val):02}" for val in mem_data.split()]
        chunk_size = len(mem_values) // 4
        mem_data = ""

        for i in range(4):
            start = i * chunk_size
            end = (i + 1) * chunk_size
            mem_data += " ".join(mem_values[start:end]) + "\n"
                
        return (reg_data, mem_data)


    def step(self):

        start = perf_counter()

        if self.index >= len(self.lines):
            return

        line = self.lines[self.index].strip()
        if not line or line.startswith("//"):
            self.index += 1
            return

        self.index = interpret_line(line, self.regs, self.mem, self.index)

        self.gui.label_last_op.setText(f"Last Operation: {line}")
        self.gui.label_last_op_line.setText(
            f"Line: {self.index} / {len(self.lines)}"
        )

        reg_data, mem_data = self.get_data()
        self.gui.label_register_data.setText(reg_data)
        self.gui.label_memory_data.setText(mem_data)

        self.gui.label_last_op_time.setText(f"Time Taken: {(perf_counter() - start) * 1000:.3f} ms")
        


def run_executor(code_path):

    app = QApplication([])
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    os.makedirs(user_log_dir("BEANS", "Cheetah"), exist_ok=True)
    data.init_logs()

    start = perf_counter()
    data.logger.info("Initializing BEANS...")

    if (not os.path.exists(code_path)) or (not code_path.endswith(".bean")):
        data.logger.error("File provided doesnt exist or is not a valid BEANS file")
        data.exit()

    mem = memory(data.memory_count, data.num_size)
    regs = registers(data.num_size, data.register_count)

    gui = BEANSGui(code_path, data.logger)
    executor = BEANSExecutor(argv[1], gui, data.logger, mem, regs)

    gui.show()

    timer = QTimer()
    timer.timeout.connect(executor.step)
    data.logger.info(f"Initiialized BEANS in {(perf_counter() - start) * 1000:.3f} ms")
    timer.start(0)

    sys.exit(app.exec())

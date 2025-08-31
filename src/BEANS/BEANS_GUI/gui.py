from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QScrollArea
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QCloseEvent, QFont

from usefullog.logger import Logger
from time import perf_counter

import sys

from BEANS.data import data

class BEANSGui(QMainWindow):
    def __init__(self, code_path, logger: Logger):
        super().__init__()

        self.logger = logger
        # self.logger.info("Constructing GUI...")
        # start = perf_counter()

        self.setWindowTitle(f"BEANS - {code_path}")
        self.setGeometry(400, 400, 550, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.label_font = QFont()
        self.label_font.setPointSize(12)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        top_layout = QHBoxLayout()

        operation_panel = QGroupBox("OPERATION")
        operation_layout = QVBoxLayout()
        operation_panel.setLayout(operation_layout)

        self.label_last_op = QLabel("Last Operation: None")
        self.label_last_op.setFont(self.label_font)
        operation_layout.addWidget(self.label_last_op, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.label_last_op_line = QLabel("Line: None / None")
        self.label_last_op_line.setFont(self.label_font)
        operation_layout.addWidget(self.label_last_op_line, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.label_last_op_time = QLabel("Time Taken: None")
        self.label_last_op_time.setFont(self.label_font)
        operation_layout.addWidget(self.label_last_op_time, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        top_layout.addWidget(operation_panel)


        memory_group_layout = QVBoxLayout()

        register_panel = QGroupBox("REGISTERS")
        register_layout = QVBoxLayout()
        register_panel.setLayout(register_layout)

        self.label_register_data = QLabel("00 00 00 00 00 00 00 00\n00 00 00 00 00 00 00 00")
        self.label_register_data.setFont(self.label_font)
        register_layout.addWidget(self.label_register_data)

        memory_group_layout.addWidget(register_panel)


        memory_panel = QGroupBox("MEMORY")
        memory_layout = QVBoxLayout()
        memory_panel.setLayout(memory_layout)

        self.label_memory_data = QLabel("00 00 00 00 00 00 00 00\n00 00 00 00 00 00 00 00\n00 00 00 00 00 00 00 00\n00 00 00 00 00 00 00 00")
        self.label_memory_data.setFont(self.label_font)
        memory_layout.addWidget(self.label_memory_data)

        memory_group_layout.addWidget(memory_panel)
        top_layout.addLayout(memory_group_layout)
        main_layout.addLayout(top_layout)



        module_panel = QGroupBox("I/O MODULES")
        module_layout = QVBoxLayout()
        module_panel.setLayout(module_layout)

        
        main_layout.addWidget(module_panel)

        # logger.info(f"Constructed GUI in {(perf_counter() - start) * 1000:.3f}ms")
    
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        for module in data.module_list:
            module.kill()
        
        return super().closeEvent(a0)
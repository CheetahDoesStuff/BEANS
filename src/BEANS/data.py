from usefullog.logger import Logger
from platformdirs import user_log_dir, user_data_dir
from sys import exit as sys_exit
from pathlib import Path



# A data class containing all settings and some data of the project, then we create an instance of the data refrenced everywhere to get / set data

class _data:
    def __init__(self):
        
        self.logger = Logger(
            "BEANS",
            do_log_saving=True,
            log_save_folder=user_log_dir("BEANS", "Cheetah")
        )

        self.module_list = []
        self.data_path = Path(user_data_dir("BEANS", "Cheetah")) / "BIOMods"
        
        self.num_size = 16
        self.register_count = 16
        self.memory_count = 64
    


    def init_logs(self):
        self.logger.info("-------- BEANS ---------")
        self.logger.info(" - Beans Is Initializing - ")
        self.logger.info(f" - Beans IO Path: {self.data_path} - ")
        self.logger.info("-------- BEANS ---------")


    def exit(self, msg: str = "Exiting the program..."):
        if msg:
            self.logger.critical(msg)

        sys_exit(1)


data = _data()
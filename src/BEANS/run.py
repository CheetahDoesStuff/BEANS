def main():
    from BEANS.executor import run_executor
    from BEANS.data import data

    from platformdirs import user_data_dir
    import argparse
    from pathlib import Path
    
    parser = argparse.ArgumentParser(description="Execute a .bean assembly file using the BEANExecutor")

    parser.add_argument("file", type=str, help="Path to the .bean file to execute.")
    parser.add_argument("-m", "--module-path", type=str, help="The path to the directory containing modules used.", default=Path(user_data_dir("BEANS", "Cheetah")) / "BIOMods")
    parser.add_argument("-b", "--value-size", type=str, help="The size of each value in bits.", default=16)
    parser.add_argument("--register-count", type=str, help="The amount of registers the program creates.", default=16)
    parser.add_argument("--memory-adress-count", type=str, help="The amount of memory adresses the program creates.", default=64)

    args = parser.parse_args()

    data.data_path = args.module_path
    data.num_size = args.value_size
    data.register_count = args.register_count
    data.memory_count = args.memory_adress_count

    run_executor(args.file)



if __name__ == "__main__":
    main()

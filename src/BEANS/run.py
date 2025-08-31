def main():
    from BEANS.executor import run_executor
    from BEANS.data import data
    import argparse
    
    parser = argparse.ArgumentParser(description="Execute a .bean assembly file using the BEANExecutor")

    parser.add_argument("file", type=str, help="Path to the .bean file to execute.")


if __name__ == "__main__":
    main()

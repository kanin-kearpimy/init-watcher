import os
from .utils import compare_directories, create_init_file
from .Directory import Directory

current_dir = os.getcwd()


def main():
    """main function of application"""

    old_directory = Directory(current_dir)

    # first time initilization.
    create_init_file(old_directory.get_directories())

    # watcher for file change.
    while True:
        new_directory = Directory(current_dir)
        differ = compare_directories(
            old_directory.get_directories(), new_directory.get_directories()
        )
        if len(differ) > 0:
            create_init_file(new_directory.get_directories())
            old_directory = new_directory


if __name__ == "__main__":
    """entry point of command line"""

    print("Start Watching __init__")
    print(f"Current Directory: {current_dir}")
    main()

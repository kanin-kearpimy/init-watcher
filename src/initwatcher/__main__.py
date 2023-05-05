from .utils import compare_directories, create_init_file
from .dircheck import Directory
import os

current_dir = os.getcwd()


def main():
    old_directory = Directory(current_dir)

    create_init_file(old_directory.get_directories())

    while True:
        new_directory = Directory(current_dir)
        differ = compare_directories(
            old_directory.get_directories(), new_directory.get_directories()
        )
        if len(differ) > 0:
            create_init_file(new_directory.get_directories())
            old_directory = new_directory


if __name__ == "__main__":
    print("Start Watching __init__")
    print("Current Directory: {}".format(current_dir))
    main()

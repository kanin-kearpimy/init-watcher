from __future__ import annotations

EXCLUDES = ["__pycache__", "test"]


def compare_directories(old_directory: list[str], new_directory: list[str]):
    """Compare current directory with old directory

    Keyword arguments:
    old_directory -- directory in form of path (string)
    new_directory -- directory in form of path (string)
    Return: difference between old and new in form of path (string)
    """

    differences = []
    for directory in new_directory:
        if directory not in old_directory:
            differences.append(directory)

    return differences


def is_exclude_directory(path: str):
    """check if path is excluded

    Keyword arguments:
    path -- directory in form of path (string)
    Return: boolean -> True if it excluded, False otherwise.
    """

    sub_directories = path.split("/")
    for exclude in EXCLUDES:
        if exclude in sub_directories:
            return True

    return False


def create_init_file(paths: list[str]):
    """create __init__.py in set of paths

    Keyword arguments:
    paths -- array of directory (string)
    Return: None
    """
    for path in paths:
        if is_exclude_directory(path) == True:
            continue
        file = open("{}/__init__.py".format(path), "w")
        file.close()

from __future__ import annotations

EXCLUDES = ["__pycache__", "test"]


def compare_directories(a_directory, b_directory):
    differences = []
    for directory in b_directory:
        if directory not in a_directory:
            differences.append(directory)

    return differences


def is_exclude_directory(path: str):
    sub_directories = path.split("/")
    for exclude in EXCLUDES:
        if exclude in sub_directories:
            return True

    return False


def create_init_file(paths: list[str]):
    for path in paths:
        if is_exclude_directory(path) == True:
            continue
        file = open("{}/__init__.py".format(path), "w")
        file.close()
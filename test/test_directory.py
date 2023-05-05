import os
from src.initwatcher.Directory import Directory


def test_get_directories():
    """get correct current directory"""

    current_dir = os.getcwd()
    expect_result = []
    directory_path = f"{current_dir}/__job__"
    os.makedirs(directory_path)
    directory = Directory(directory_path)
    directories = directory.get_directories()
    assert len(directories) == len(expect_result)
    os.rmdir(directory_path)

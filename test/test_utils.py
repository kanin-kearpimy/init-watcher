import os
from src.initwatcher import utils


def test_exclude_directory():
    expect_result = True
    is_exclude_dir = utils.is_exclude_directory("root/__pycache__/abc")
    assert expect_result == is_exclude_dir


def test_exclude_test_directory():
    expect_result = True
    is_exclude_dir = utils.is_exclude_directory("root/123/www/aaa/test/ass/brtyyi/q")
    assert expect_result == is_exclude_dir


def test_not_exclude_directory():
    expect_result = False
    is_exclude_dir = utils.is_exclude_directory("root/package_a")
    assert expect_result == is_exclude_dir


def test_different_directories():
    old_directory = ["root/a/b", "root/package_T"]
    new_directory = ["root/a/b", "root/package_T", "root/package_B"]
    expect_result = ["root/package_B"]
    differences = utils.compare_directories(old_directory, new_directory)
    assert len(differences) == len(expect_result)
    assert expect_result == differences


def test_different_2_directories():
    old_directory = ["root/a/b", "root/package_T", "root/a/b/c/d/e/f"]
    new_directory = ["root/a/b", "root/package_T", "root/package_B"]
    expect_result = ["root/package_B"]
    differences = utils.compare_directories(old_directory, new_directory)
    assert len(differences) == len(expect_result)
    assert expect_result == differences


def test_no_diffrent_directories():
    old_directory = ["root/a/b"]
    new_directory = ["root/a/b"]
    expect_result = []
    differences = utils.compare_directories(old_directory, new_directory)
    assert len(differences) == len(expect_result)
    assert expect_result == differences


def test_not_create_init_file():
    paths = ["{}/test/utils".format(os.getcwd())]
    utils.create_init_file(paths)
    assert "__init__.py" not in os.listdir(paths[0])


def test_create_init_file():
    directory = "{}/__job__".format(os.getcwd())
    os.makedirs(directory)
    paths = [directory]
    utils.create_init_file(paths)
    assert "__init__.py" in os.listdir(paths[0])
    os.remove("{}/__init__.py".format(directory))
    os.rmdir(directory)

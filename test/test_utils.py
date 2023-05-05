import os
from src.initwatcher import utils

current_dir = os.getcwd()


def test_exclude_directory():
    """
    is_exclude_directory()
    should return True when __pycache__/ is in paths
    Because it's excluded
    """
    expect_result = True
    is_exclude_dir = utils.is_exclude_directory("root/__pycache__/abc")
    assert expect_result == is_exclude_dir


def test_exclude_test_directory():
    """
    is_exclude_directory()
    should return True when test/ is in paths
    Because it's excluded
    """
    expect_result = True
    is_exclude_dir = utils.is_exclude_directory("root/123/www/aaa/test/ass/brtyyi/q")
    assert expect_result == is_exclude_dir


def test_not_exclude_directory():
    """
    is_exclude_directory()
    should return False when facing root/package_a (not excluded)
    """
    expect_result = False
    is_exclude_dir = utils.is_exclude_directory("root/package_a")
    assert expect_result == is_exclude_dir


def test_different_directories():
    """
    compare_directories()
    should return root/package_B due to differences
    between old and new directories system
    """
    old_directory = ["root/a/b", "root/package_T"]
    new_directory = ["root/a/b", "root/package_T", "root/package_B"]
    expect_result = ["root/package_B"]
    differences = utils.compare_directories(old_directory, new_directory)
    assert len(differences) == len(expect_result)
    assert expect_result == differences


def test_different_2_directories():
    """
    compare_directories()
    should return root/package_B due to differences
    between old and new directories system

    Nothing to do with "root/a/b/c/d/e/f"
    because it's deleted
    """
    old_directory = ["root/a/b", "root/package_T", "root/a/b/c/d/e/f"]
    new_directory = ["root/a/b", "root/package_T", "root/package_B"]
    expect_result = ["root/package_B"]
    differences = utils.compare_directories(old_directory, new_directory)
    assert len(differences) == len(expect_result)
    assert expect_result == differences


def test_no_diffrent_directories():
    """
    compare_directories()
    should return [] due to no differences
    between old and new directories system
    """
    old_directory = ["root/a/b"]
    new_directory = ["root/a/b"]
    expect_result = []
    differences = utils.compare_directories(old_directory, new_directory)
    assert len(differences) == len(expect_result)
    assert expect_result == differences


def test_not_create_init_file():
    """
    create_init_file()
    should not create __init__.py in /test/utils
    because test/ is excluded
    """
    directory = f"{current_dir}/test/utils"
    os.makedirs(directory)
    paths = [f"{current_dir}/test/utils"]
    utils.create_init_file(paths)
    assert "__init__.py" not in os.listdir(paths[0])
    os.rmdir(directory)


def test_create_init_file():
    """
    create_init_file()
    should create __init__.py in /test/utils
    """
    directory = f"{current_dir}/__job__"
    os.makedirs(directory)
    paths = [directory]
    utils.create_init_file(paths)
    assert "__init__.py" in os.listdir(paths[0])
    os.remove(f"{directory}/__init__.py")
    os.rmdir(directory)

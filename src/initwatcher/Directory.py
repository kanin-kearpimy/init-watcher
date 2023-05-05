from __future__ import annotations
import os


class Directory:
    """Directory class"""

    current_directory = ""
    directories = []

    def __init__(self, current_directory: str):
        self.current_directory = current_directory
        self.directories = []
        self.__get_all_directory(current_directory)

    def __get_all_directory(self, current: str):
        for directory in os.listdir(current):
            if os.path.isdir(f"{current}/{directory}"):
                self.directories.append(f"{current}/{directory}")
                self.__get_all_directory(f"{current}/{directory}")

    def get_directories(self):
        """return current array of directories"""
        return self.directories

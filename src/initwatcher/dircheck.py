from __future__ import annotations
import os


class Directory:
    def __init__(self, current_directory):
        self.current_directory = current_directory
        self.directories = []
        self.__get_all_directory(current_directory)

    def __get_all_directory(self, current: str):
        for directory in os.listdir(current):
            if os.path.isdir("{}/{}".format(current, directory)):
                self.directories.append("{}/{}".format(current, directory))
                self.__get_all_directory("{}/{}".format(current, directory))

    def get_directories(self):
        return self.directories

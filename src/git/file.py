""" Class modeling the file.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""
from src.process.process import Process

class File():

    def __init__(self, name):
        """
        Construct a new 'File' object.

        :param name: The file's name
        """
        self.__name = name
        self.__raw_content = None

    def compute_content_current(self, repository, commit):
        """
        Computes the file content in the current commit.

        :param repository: The Repository object
        :param repository: The Commit object

        :return: The file's raw content
        """
        cmd = f"git -C {repository.get_local_path()} show {commit.get_current()}:{self.__name}"
        status, stdout, stderr = Process.start_process(cmd)

        self.__raw_content = stdout
        return status, stdout, stderr

    def compute_content_parent(self, repository, commit):
        """
        Computes the file content in the parent commit.

        :param repository: The Repository object
        :param repository: The Commit object

        :return: The file's raw content
        """
        cmd = f"git -C {repository.get_local_path()} show {commit.get_parent()}:{self.__name}"
        status, stdout, stderr = Process.start_process(cmd)

        self.__raw_content = stdout
        return status, stdout, stderr

    def get_name(self):
        """
        Get the file's name.

        :return: The files's name
        """
        return self.__name

    def get_raw_content(self):
        """
        Get the file's raw content.

        :return: The files's raw content
        """
        return self.__raw_content

    def set_name(self, name):
        """
        Set the file's name.

        :param name: The file name
        :return: Return nothing
        """
        self.__name = name

    def set_raw_content(self, raw_content):
        """
        Set the file's raw content.

        :param raw_content: The file raw content
        :return: Return nothing
        """
        self.__raw_content = raw_content


    def __hash__(self):
        """
        Hash override.

        :return: The hash from the File object.
        """
        return hash(self.__name)


    def __str__(self):
        """
        String representation.

        :return: The string represention of the File object.
        """
        result = f"File name: {self.__name}\n\n"

        for line in self.__lines:
            result += f"{line} \n"

        return result
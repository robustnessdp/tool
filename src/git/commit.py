""" Class modeling the commit.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

import re
from src.process.process import Process
from src.git.file import File

class Commit():

    def __init__(self, current=None, parent=None):
        """
        Construct a new 'Commit' object.

        :param current: The hash from the current Commit
        :param parent: The hash from the remote Commit
        :param language: The Language from the  from the remote Commit
        """
        self.__current = current
        self.__parent = parent
        self.__date = None
        self.__author = None
        self.__changed_files = set()

    def compute_date(self, repository):
        """
        Computes the commit date, setting the data in the self object.

        :param name: The Repository object
        :return: Return nothing
        """
        cmd = f"git -C {repository.get_local_path()} log --pretty=format:'%as' -n 1 {self.__current}"
        status, stdout, stderr = Process.start_process(cmd)

        if stdout:
            self.__date = stdout

    def compute_parent(self, repository):
        """
        Computes the parent, setting the data in the self object.

        :param name: The Repository object
        :return: Return nothing
        """
        cmd = f"git -C {repository.get_local_path()} log --pretty=format:'%P' -n 1 {self.__current}"
        status, stdout, stderr = Process.start_process(cmd)
        if stdout:
            self.__parent = re.split(r'\s+', stdout)[0]

    def compute_changed_files(self, repository):
        """
        Computes the list of changed File at the commit, setting the data in the self object.

        :param name: The Repository object
        :return: Return nothing
        """
        if self.__current and self.__parent:
            cmd = f"git -C {repository.get_local_path()} diff --name-only {self.__current} {self.__parent}"
            status, stdout, stderr = Process.start_process(cmd)

            for line in stdout.split("\n"):
                if line:
                    try:
                        if repository.get_language().is_code_file(line):
                            file = File(line)
                            self.__changed_files.add(file)
                        else:
                            continue
                    except Exception as err:
                        print(err)
                        continue
        else:
            raise Exception(f"The current commit or its parent does not exist. \nCommit: {self.__current} Parent: {self.__parent}")

    def get_current(self):
        """
        Get the hash from the current commit.

        :return: Hash from the current commit
        """
        return self.__current

    def get_parent(self):
        """
        Get the hash from the parent commit.

        :return: Hash from the parent commit
        """
        return self.__parent

    def get_changed_files(self):
        """
        Get the list of changed File at the commit

        :return: List of File.
        """
        return self.__changed_files

    def get_date(self):
        """
        Get the commit date.

        :return: The commit date
        """
        return self.__date

    def get_author(self):
        """
        Get the commit Author.

        :return: The ommit Author
        """
        return self.__author

    def set_current(self, current):
        """
        Set the hash from the current commit.

        :param parent: The hash from current commit
        :return: Return nothing
        """
        self.__current = current

    def set_parent(self, parent):
        """
        Set the hash from the parent commit.

        :param parent: The hash from parent commit
        :return: Return nothing
        """
        self.__parent = parent

    def set_changed_files(self, changed_files):
        """
        Set the changed files commit.

        :param changed_files: The list of File
        :return: Return nothing
        """
        self.__changed_files

    def set_date(self, date):
        """
        Set the commit date.

        :param date: The commit date
        :return: Return nothing
        """
        self.__date = date

    def set_author(self, author):
        """
        Set the commit Author.

        :param author: The commit Author
        :return: Return nothing
        """
        self.__author = author

    def __hash__(self):
        """
        Hash override.

        :return: The hash from the Commit object.
        """
        return hash(self.__current)

    def __str__(self):
        """
        String representation.

        :return: The string represention of the File object.
        """
        result = f"Current commit: {self.__current} Parent commit: {self.__parent} Date: {self.__date}\n"
        result += f"All changed files: \n"
        for file in self.__changed_files:
            result += f"    - {file.get_name()} \n"

        return result
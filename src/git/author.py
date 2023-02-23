""" Class modeling the author.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.process.process import Process

class Author():
    """
    This class encapsulates the data regarding the author of a commit, besides operations to gather that data in a local repository.
    """

    def __init__(self, name=None, email=None):
        """
        Construct a new Author object.

        :param name: The author's name
        :param email: The author's email
        """
        self.__name = name
        self.__email = email

    def compute_author(self, repository, commit):
        """
        Compute in a repository the author of a commit, and set data in the self object.

        :param repository: The Repository object
        :param email: The Commit object
        :return: Return nothing
        """

        cmd = f"git -C {repository.get_local_path()} log --pretty=format:'%an' -n 1 {commit.get_current()}"
        status, stdout, stderr = Process.start_process(cmd)

        if stdout:
            name = stdout
            self.__name = name

        cmd = f"git -C {repository.get_local_path()} log --pretty=format:'%ae' -n 1 {commit.get_current()}"
        status, stdout, stderr = Process.start_process(cmd)

        if stdout:
            email = stdout
            self.__email = email

    def get_name(self):
        """
        Get the author's name.

        :return: The author name
        """
        return self.__name
    
    def get_email(self):
        """
        Get the author's email.

        :return: The author email
        """
        return self.__email

    def set_name(self, name):
        """
        Set the author's name.

        :param name: The author's name
        :return: Return nothing
        """
        self.__name = name

    def set_email(self, email):
        """
        Set the author's email.

        :param email: The author's email
        :return: Return nothing
        """
        self.__email = email

    def __str__(self):
        """
        String representation.

        :return: The string representation of the Author object.
        """
        return f"Name: {self.__name} Email: {self.__email}"

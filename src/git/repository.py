""" Class modeling the repository.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.language.language import Language
from src.git.commit import Commit
from src.process.process import Process

class Repository():
    def __init__(self, remote_path, local_path, branch, language: Language):
        """
        Construct a new 'Repository' object.

        :param remote_path: The repository's url
        :param local_path: The repository's local_path
        :param branch: The repository's branch
        :param language: The repository's 'Language'
        """

        self.__remote_path = remote_path
        self.__local_path = local_path
        self.__branch = branch
        self.__language = language
        self.__commits = []

    def clone_repo(self):
        """
        Clone the repository's in the local path.

        :return: Tuple containing the status code, the stdout and the stderr
        """
        cmd = f"git clone {self.__remote_path} {self.__local_path}"
        status, stdout, stderr = Process.start_process(cmd)
        return status, stdout, stderr

    def delete_repo(self):
        """
        Delete the repository's in the local path.

        :return: Tuple containing the status code, the stdout and the stderr
        """
        cmd = f"rm -rf {self.__local_path}"
        status, stdout, stderr = Process.start_process(cmd)
        return status, stdout, stderr

    def branch_checkout(self):
        """
        Chekout the repository's in the branch.

        :return: Tuple containing the status code, the stdout and the stderr
        """
        cmd = f"git -C {self.__local_path} checkout {self.__branch}"
        status, stdout, stderr = Process.start_process(cmd)
        return status, stdout, stderr

    def compute_commits(self):
        """
        Computes the entire list of commit hashs in the current branch.

        :return: List containing the commits hashs
        """
        cmd = f"git -C {self.__local_path} log --pretty=format:'%H'"
        status, stdout, stderr = Process.start_process(cmd)

        for line in stdout.split("\n"):
            if line:
                commit = Commit(current=line, parent=None)
                commit.compute_parent(self)
                commit.compute_date(self)
                self.__commits.append(commit)

        return self.__commits

    def get_remote_path(self):
        """
        Get the repository's remote path.

        :return: The repository's remote path
        """
        return self.__remote_path

    def get_local_path(self):
        """
        Get the repository's local path.

        :return: The repository's local path
        """
        return self.__local_path

    def get_branch(self):
        """
        Get the repository's remote path.

        :return: The repository's branch path
        """
        return self.__branch

    def get_language(self):
        """
        Get the repository's remote Language.

        :return: The repository's Language
        """
        return self.__language

    def get_commits(self):
        """
        Get the repository's list of commits.

        :return: The repository's list of commits
        """
        return self.__commits

    def set_remote_path(self, remote_path):
        """
        Set the repository's remote path.

        :param local_path: The repository's remote_path
        :return: Return nothing
        """
        self.__remote_path = remote_path

    def set_local_path(self, local_path):
        """
        Set the repository's local path.

        :param local_path: The repository's local_path
        :return: Return nothing
        """
        self.__local_path = local_path

    def set_branch(self, branch):
        """
        Set the repository's branch.

        :param branch: The repository's branch
        :return: Return nothing
        """
        self.__branch = branch

    def set_language(self, language: Language):
        """
        Set the repository's Language.

        :param language: The repository's Language
        :return: Return nothing
        """
        self.__language= language

    def set_commits(self, commits):
        """
        Set the repository's list of commits.

        :param commits: List of Commit
        :return: Return nothing
        """
        self.__commits = commits

    def set_commits(self, hashs: [str]):
        """
        Set the repository's list of commits.

        :param commits: List of hashs
        :return: Return nothing
        """
        for current in hashs:
            commit = Commit(current=current, parent=None)
            commit.compute_parent(self)
            self.__commits.append(commit)

    def __str__(self):
        """
        String representation.

        :return: The string represention of the Repository object.
        """
        result = f"URL: {self.__remote_path} Clone path: {self.__local_path}\n"
        result += f"All commits: \n"
        for commit in self.__commits:
            result += f"    - Current: {commit.get_current()} Parent: {commit.get_parent()}\n"
        return result

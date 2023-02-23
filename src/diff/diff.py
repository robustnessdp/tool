""" Class modeling the diff between two files.

    For more details about diffs using the GNUDiff tool, see: https://www.gnu.org/software/diffutils/

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

import re
import os
from src.process.process import Process
from src.diff.hunk import Hunk, ChangeType
from src.git.file import File

class Diff():
    def __init__(self, file_left: File, file_right: File):
        """
        Construct a new Diff object.

        :param file_left: String containing the left file's raw content.
        :param file_right: String containing the right file's raw content.
        :param file_path: The file path.
        """
        self.__file_left = file_left
        self.__file_right = file_right
        self.__diff = []
        self.__hunks = []

    def compute_diff(self, repository):
        """
        Computes the Diff between the two files, and set data in the self object.

        :param repository: Repository object.
        :return: Returns nothing.
        """
        if self.__file_left and self.__file_right:

            with open(f"{repository.get_local_path()}/{os.getpid()}_1.txt", "w") as file:
                file.write(self.__file_left.get_raw_content())

            with open(f"{repository.get_local_path()}/{os.getpid()}_2.txt", "w") as file:
                file.write(self.__file_right.get_raw_content())

            # Run the GNUDiff tool, to compute the differences between the two files.
            cmd = f"diff {repository.get_local_path()}/{os.getpid()}_2.txt {repository.get_local_path()}/{os.getpid()}_1.txt"
            status, stdout, stderr = Process.start_process(cmd)

            for line in stdout.split("\n"):
                if line:
                    self.__diff.append(line)

            os.remove(f"{repository.get_local_path()}/{os.getpid()}_1.txt")
            os.remove(f"{repository.get_local_path()}/{os.getpid()}_2.txt")

    def compute_hunks(self):
        """
        Computes the hunks, and set data in the self object.

        :param repository: Repository object.
        :return: Returns nothing.
        """
        match_line = re.compile('^(\\d+)(,\\d+)?(a|c|d)(\\d+)(,\\d+)?')
        match_character = re.compile('(a|c|d)')

        for line in self.__diff:
            if match_line.match(line):
                hunk = Hunk()

                character = match_character.findall(line)[0]
                if character:

                    if character == 'a':
                        hunk.set_change_type(ChangeType.ADDITION)
                    elif character == 'c':
                        hunk.set_change_type(ChangeType.CHANGE)
                    elif character == 'd':
                        hunk.set_change_type(ChangeType.DELETION)
                else:
                    continue

                left, right = line.split(character)

                left_split = left.split(",")
                if len(left_split) == 2:
                    hunk.set_left_from(int(left_split[0]))
                    hunk.set_left_to(int(left_split[1]))
                else:
                    hunk.set_left_from(int(left))
                    hunk.set_left_to(int(left))

                right_split = right.split(",")
                if len(right_split) == 2:
                    hunk.set_right_from(int(right_split[0]))
                    hunk.set_right_to(int(right_split[1]))
                else:
                    hunk.set_right_from(int(right))
                    hunk.set_right_to(int(right))

                self.__hunks.append(hunk)

    def get_file_left(self):
        """
        Gets the left file raw content.

        :return: String containing the left file raw content.
        """
        return self.__file_left

    def get_file_right(self):
        """
        Gets the right file raw content.

        :return: String containing the right file raw content.
        """
        return self.__file_right

    def get_diff(self):
        """
        Gets the diff content.

        :return: List containing the diff between the two files.
        """
        return self.__diff

    def get_hunks(self):
        """
        Gets the hunks in the diff.

        :return: List of Hunk containing the diff's hunks.
        """
        return self.__hunks

    def set_file_left(self, file_left):
        """
        Sets the left file raw content.

        :param file_left: String containing the left file raw content.
        :return: Returns nothing.
        """
        self.__file_left = file_left

    def set_file_right(self, file_right):
        """
        Sets the right file raw content.

        :param file_right: String containing the right file raw content.
        :return: Returns nothing.
        """
        self.__file_right = file_right

    def set_diff(self, diff):
        """
        Sets the diff content.

        :param diff: List containing the diff between the two files.
        :return: Returns nothing.
        """
        self.__diff = diff

    def set_hunks(self, hunks):
        """
        Sets the hunks in the diff.

        :param diff: List of Hunk containing the diff's hunks.
        :return: Returns nothing.
        """
        self.__hunks = hunks
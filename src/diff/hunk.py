""" Class modeling the hunks in diffs.

    For more details about hunks, see: https://www.gnu.org/software/diffutils/manual/html_node/Hunks.html

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from enum import Enum

class ChangeType(Enum):
    """
    Enum representing the possible states for hunks.
    """

    ADDITION = 1
    CHANGE = 2
    DELETION = 3

class Hunk():
    ID = 0

    def __init__(self, left_from=None, left_to=None, right_from=None, right_to=None, change_type: ChangeType = None):
        """
        Construct a new Hunk object.

        :param left_from: The start line of the hunk in the left file.
        :param left_to: The end line of the hunk in the left file.
        :param right_from: The start line of the hunk in the right file.
        :param right_to: The end line of the hunk in the right file.
        :param change_type: The hunk ChangeType.
        :return: Returns nothing.
        """
        self.__left_from = left_from
        self.__left_to = left_to
        self.__right_from = right_from
        self.__right_to = right_to
        self.__change_type = change_type
        self.__id = Hunk.ID
        Hunk.ID += 1

    def get_id(self):
        """
        Gets the hunk id.

        :return: The hunk id.
        """
        return self.__id

    def get_left_from(self):
        """
        Gets the start line of the hunk in the left file.

        :return: The start line of the hunk in the left file.
        """
        return self.__left_from

    def get_left_to(self):
        """
        Gets the end line of the hunk in the left file.

        :return: The start line of the hunk in the left file.
        """
        return self.__left_to

    def get_right_from(self):
        """
        Gets the start line of the hunk in the right file.

        :return: The start line of the hunk in the left file.
        """
        return self.__right_from

    def get_right_to(self):
        """
        Gets the end line of the hunk in the right file.

        :return: The start line of the hunk in the left file.
        """
        return self.__right_to

    def get_change_type(self):
        """
        Gets the hunk change type.

        :return: The hunk ChangeType.
        """
        return self.__change_type

    def set_left_from(self, left_from):
        """
        Sets the start line of the hunk in the left file.

        :param left_from: The start line of the hunk in the left file.
        :return: Returns nothing.
        """
        self.__left_from = left_from

    def set_left_to(self, left_to):
        """
        Sets the end line of the hunk in the left file.

        :param left_to: The end line of the hunk in the left file.
        :return: Returns nothing.
        """
        self.__left_to = left_to

    def set_right_from(self, right_from):
        """
        Sets the start line of the hunk in the right file.

        :param right_from: The start line of the hunk in the right file.
        :return: Returns nothing.
        """
        self.__right_from = right_from

    def set_right_to(self, right_to):
        """
        Sets the end line of the hunk in the right file.

        :param right_to: The end line of the hunk in the right file.
        :return: Returns nothing.
        """
        self.__right_to = right_to

    def set_change_type(self, change_type: ChangeType):
        """
        Sets the hunk change type.

        :param change_type: The hunk ChangeType.
        :return: Returns nothing.
        """
        self.__change_type = change_type

    def __str__(self):
        """
        String representation.

        :return: The string representation of the Hunk object.
        """
        return f"Hunk: [ Id: {self.__id} Change: {self.__change_type} Left from: {self.__left_from} Left to: {self.__left_to} Right from: {self.__right_from} Right to: {self.__right_to} ]"
""" Class modeling the relation between one Hunk and impacted CodeElement.

    For each Hunk, there is two list of CodeElement. The list of CodeElements impacted in the left file, and the list of
    CodeElements impacted in the right file.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

class HunkElementAggregator():

    def __init__(self, hunk):
        """
        Constructs a new HunkElementAggregator object. This object stores the relation between a Hunk, and the
        impacted CodeElements.

        :param hunk: The Hunk object.
        """
        self.__hunk = hunk
        self.__elements_left = []
        self.__elements_right = []


    def add_elements_left(self, element):
        """
        Adds a CodeElement in the list of elements impacted in the left file.

        :param element: The CodeElement object.
        """
        self.__elements_left += element

    def add_elements_right(self, element):
        """
        Adds a CodeElement in the list of elements impacted in the right file.

        :param element: The CodeElement object.
        """
        self.__elements_right += element

    def get_hunk(self):
        """
        Gets the Hunk.

        :return: The Hunk object.
        """
        return self.__hunk

    def get_elements_left(self):
        """
        Gets the list of CodeElements impacted in the left file.

        :return: The list of CodeElements impacted in the left file.
        """
        return self.__elements_left

    def get_elements_right(self):
        """
        Gets the list of CodeElements impacted in the right file.

        :return: The list of CodeElements impacted in the right file.
        """
        return self.__elements_right

    def set_hunk(self, hunk):
        """
        Sets the Hunk.

        :param hunk: The Hunk object.
        :return: Returns nothing.
        """
        self.__hunk = hunk

    def set_element_left(self, element):
        """
        Sets the list of CodeElements impacted in the left file.

        :param element: The list of CodeElements impacted in the left file
        :return: Returns nothing.
        """
        self.__elements_left = element

    def set_element_right(self, element):
        """
        Sets the list of CodeElements impacted in the right file.

        :param element: The list of CodeElements impacted in the right file
        :return: Returns nothing.
        """
        self.__elements_right = element
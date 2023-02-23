""" Super class modeling the language processed by this tool.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

class Language():

    def __init__(self, code_element_to_collect=None, code_file_extension=None):
        """
        Construct a new Language object.

        :param code_element_to_collect: List of language's code elements (see the tree sitter documentation), that should have its changes collected. Elements out of this list will be ignored.
        :param code_file_extension: List of valid language file extensions. Files with extension out this list will be ignored.
        """
        self.__code_element_to_collect = code_element_to_collect
        self.__code_file_extension = code_file_extension

    def is_code_file(self, file_name):
        """
        Checks if the file contains a valid extension for the language.

        :param file_name: file name.
        :return: True if the file is valid, False otherwise.
        """
        try:
            extension = file_name.split(".")[-1]
            if extension in self.__code_file_extension:
                return True
            else:
                return False
        except Exception:
            raise Exception(f"This file does not contain an extension on its name.")

    def get_elements_to_collect(self):
        """
        Get language's code elements to collect.

        :return: List containing the code elements to collect.
        """
        return self.__code_element_to_collect

    def get_code_file_extension(self):
        """
        Get valid language file extensions.

        :return: List containing valid file extensions for the language.
        """
        return self.__code_file_extension

    def set_elements_to_collect(self, code_element_to_collect):
        """
        Set language's code elements to collect.

        :param code_element_to_collect: List containing the code elements to collect.
        :return: Returns nothing.
        """
        self.__code_element_to_collect = code_element_to_collect

    def set_code_file_extension(self, code_file_extension):
        """
        Set valid language file extensions.

        :param code_file_extension: List containing the code elements to collect.
        :return: Returns nothing.
        """
        self.__code_file_extension = code_file_extension




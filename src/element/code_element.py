""" Class modeling code element.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

class CodeElement():

    ID = 0
    def __init__(self, type, start_position, end_position):
        """
        Construct a new CodeElement object.

        :param type: The code element type (e.g., class_declaration, method_declaration).
        :param start_position: The element start position.
        :param file_path: The element end position.
        """
        self.__id = CodeElement.ID
        self.__type = type
        self.__declaration = None
        self.__start_position = start_position
        self.__end_position = end_position
        self.__body_preview = None
        CodeElement.ID += 1

    def get_id(self):
        """
        Gets the code element id.

        :return: The element id.
        """
        return self.__id

    def get_type(self):
        """
        Gets the code element type.

        :return: The element type.
        """
        return self.__type

    def get_declaration(self):
        """
        Gets the code element declaration.

        :return: For classes and methods, returns the declaration (method' or class' name). Otherwise, returns None.
        """
        return self.__declaration

    def get_start_position(self):
        """
        Gets the code element start position.

        :return: The element start position into the file.
        """
        return self.__start_position

    def get_end_position(self):
        """
        Gets the code element end position.

        :return: The element end position into the file.
        """
        return self.__end_position

    def get_body_preview(self):
        """
        Gets the code element body preview.

        :return: The first 30 characters in the code element body.
        """
        return self.__body_preview

    def set_type(self, type):
        """
        Sets the code element type.

        :param type: The code element type.
        :return: Returns nothing.
        """
        self.__type = type

    def set_declaration(self, declaration):
        """
        Sets the code element declaration.

        :param declaration: The method's or class' name.
        :return: Returns nothing.
        """
        self.__declaration = declaration

    def set_start_position(self, start_position):
        """
        Sets the code element start position.

        :param start_position: The code element start line into the file.
        :return: Returns nothing.
        """
        self.__start_position = start_position

    def set_end_position(self, end_position):
        """
        Sets the code element end position.

        :param end_position: The code element end line into the file.
        :return: Returns nothing.
        """
        self.__end_position = end_position

    def set_body_preview(self, body_preview):
        """
        Sets the code element body preview.

        :param body_preview: The code element body. If more than 30 characters were received, only the first 30 will be considered.
        :return: Returns nothing.
        """
        self.__body_preview = body_preview[0:30].decode("utf-8").replace("\n", " ") + "..."

    def __str__(self):
        """
        String representation.

        :return: The string representation of the CodeElement object.
        """
        return f"Element: [ Identifier: {self.__type} Declaration: {self.__declaration} Start: {self.__start_position} End: {self.__end_position} Body: {self.__body_preview} ]"
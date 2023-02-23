"""Sub class modeling the Java language, inheritance from Language.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.language.language import Language

class Java(Language):
    __CODE_FILE_EXTENSION = ['java']
    """Default valid Java file extensions"""

    __CODE_ELEMENTS_TO_COLLECT = ['try_statement', 'catch_clause', 'constructor_declaration', 'method_declaration', 'class_declaration']
    """Default Java's code elements that should be collected."""

    def __init__(self, code_element_to_collect=__CODE_ELEMENTS_TO_COLLECT, code_file_extension=__CODE_FILE_EXTENSION):
        """
        Construct a new Java object, setting the Java's default values for the super class attributes.

        :param code_element_to_collect: List of language's code elements (see the tree sitter documentation), that should have its changes collected. Elements out this list will be ignored.
        :param code_file_extension: List of valid language file extensions. Files with extension out this list will be ignored.
        """
        super().__init__(code_element_to_collect, code_file_extension)
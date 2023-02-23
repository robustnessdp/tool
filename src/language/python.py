"""Sub class modeling the Python language, inheritance from Language.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.language.language import Language

class Python(Language):

    __CODE_FILE_EXTENSION = ['py']
    """Default valid Python file extensions"""

    __CODE_ELEMENTS_TO_COLLECT = ['if_statement', 'do_statement', 'for_statement', 'enhanced_for_statement', 'while_statement',
        'binary_expression', 'ternary_expression', 'assert_statement', 'switch_expression', 'switch_block_statement_group',
        'lambda_expression', 'try_statement', 'catch_clause', 'method_declaration', 'class_declaration', 'interface_declaration',
        'enum_declaration']
    """Default Python's code elements that should be collected."""

    def __init__(self, code_element_to_collect=__CODE_ELEMENTS_TO_COLLECT, code_file_extension=__CODE_FILE_EXTENSION):
        """
        Construct a new Python object, setting the Python's default values for the super class attributes.

        :param code_element_to_collect: List of language's code elements (see the tree sitter documentation), that should have its changes collected. Elements out this list will be ignored.
        :param code_file_extension: List of valid language file extensions. Files with extension out this list will be ignored.
        """
        super().__init__(code_element_to_collect, code_file_extension)
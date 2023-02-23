""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.language.java import Java
from src.language.python import Python

class TestLanguage():

    def test_parameters(self):
        java = Java()
        assert java.get_elements_to_collect() == ['if_statement', 'do_statement', 'for_statement', 'enhanced_for_statement', 'while_statement',
        'binary_expression', 'ternary_expression', 'assert_statement', 'switch_expression', 'switch_block_statement_group',
        'lambda_expression', 'try_statement', 'catch_clause', 'method_declaration', 'class_declaration', 'interface_declaration',
        'enum_declaration']
        assert java.get_code_file_extension() == ['java']

        python = Python()
        assert python.get_elements_to_collect() == ['if_statement', 'do_statement', 'for_statement', 'enhanced_for_statement', 'while_statement',
        'binary_expression', 'ternary_expression', 'assert_statement', 'switch_expression', 'switch_block_statement_group',
        'lambda_expression', 'try_statement', 'catch_clause', 'method_declaration', 'class_declaration', 'interface_declaration',
        'enum_declaration']
        assert python.get_code_file_extension() == ["py"]

    def test_file_filter(self):
        java = Java()
        assert java.is_code_file("test.java") == True
        assert java.is_code_file(".java") == True
        assert java.is_code_file("test2.java") == True
        assert java.is_code_file("java.java") == True
        assert java.is_code_file("test.txt") == False
        assert java.is_code_file("test") == False

        python = Python()
        assert python.is_code_file("test.py") == True
        assert python.is_code_file(".py") == True
        assert python.is_code_file("test2.py") == True
        assert python.is_code_file("python.py") == True
        assert python.is_code_file("test.txt") == False
        assert python.is_code_file("test") == False
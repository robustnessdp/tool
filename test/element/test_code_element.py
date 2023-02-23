""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.element.code_element import CodeElement

class TestCodeElement():
    def test_constructor(self):
        element = CodeElement(type='class_declaration', start_position=0, end_position= 101)
        assert element.get_type() == 'class_declaration'
        assert element.get_start_position() == 0
        assert element.get_end_position() == 101
        assert element.get_body_preview() == None
        assert element.get_declaration() == None

        element = CodeElement(type='method_declaration', start_position=10, end_position= 23)
        assert element.get_type() == 'method_declaration'
        assert element.get_start_position() == 10
        assert element.get_end_position() == 23
        assert element.get_body_preview() == None
        assert element.get_declaration() == None

        element = CodeElement(type="", start_position=0, end_position=0)
        assert element.get_type() == ""
        assert element.get_start_position() == 0
        assert element.get_end_position() == 0
        assert element.get_body_preview() == None
        assert element.get_declaration() == None

        element = CodeElement(type=None, start_position=None, end_position=None)
        assert element.get_type() == None
        assert element.get_start_position() == None
        assert element.get_end_position() == None
        assert element.get_body_preview() == None
        assert element.get_declaration() == None


    def test_getters_and_setters(self):
        element = CodeElement(type=None, start_position=None, end_position=None)
        element.set_type('try_statement')
        element.set_body_preview(b'try{ foo(param, param, param): my_call() if true: then  }')
        element.set_start_position(120)
        element.set_end_position(170)
        element.set_declaration(None)

        assert element.get_type() == 'try_statement'
        assert element.get_start_position() == 120
        assert element.get_end_position() == 170
        assert element.get_body_preview() == "try{ foo(param, param, param):..."
        assert element.get_declaration() == None

        element.set_type('class_declaration')
        element.set_body_preview(b'class SinglyLinkedList {')
        element.set_start_position(13)
        element.set_end_position(151)
        element.set_declaration('SinglyLinkedList')

        assert element.get_type() == 'class_declaration'
        assert element.get_start_position() == 13
        assert element.get_end_position() == 151
        assert element.get_body_preview() == "class SinglyLinkedList {..."
        assert element.get_declaration() == 'SinglyLinkedList'

        element.set_type('method_declaration')
        element.set_body_preview(b'foo(b,c,a):')
        element.set_start_position(1213)
        element.set_end_position(1323)
        element.set_declaration('foo')

        assert element.get_type() == 'method_declaration'
        assert element.get_start_position() == 1213
        assert element.get_end_position() == 1323
        assert element.get_body_preview() == "foo(b,c,a):..."
        assert element.get_declaration() == 'foo'
""" Class containing static methods for visit the AST.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.element.code_element import CodeElement

class Visitor():

    @staticmethod
    def visit_and_compare_hunk_left(node, hunk, language):
        """
        Visit the AST, comparing the nodes intervals with the hunks left intervals.

        :param node: The root node in the AST.
        :param hunk: The list of hunks.
        :param language: The language object.
        :return: Returns nothing.
        """
        hunk_from = hunk.get_left_from()
        hunk_to = hunk.get_left_to()
        return Visitor.visit_and_compare(node, hunk_from, hunk_to, language)

    @staticmethod
    def visit_and_compare_hunk_right(node, hunk, language):
        """
        Visit the AST, comparing the nodes intervals with the hunks right intervals.

        :param node: The root node in the AST.
        :param hunk: The list of hunks.
        :param language: The language object.
        :return: Returns nothing.
        """
        hunk_from = hunk.get_right_from()
        hunk_to = hunk.get_right_to()
        return Visitor.visit_and_compare(node, hunk_from, hunk_to, language)

    @staticmethod
    def visit_and_compare(node, hunk_from, hunk_to, language):
        """
        Performs a BFS in the AST computing which nodes (code elements) are affected by a change interval (hunk_from, hunk_to).
        In other words, this method computes the code elements that contains intersection with the given change interval.

        :param node: The root node in the AST.
        :param hunk_from: The start interval.
        :param hunk_to: The end interval.
        :param language: The Language object.
        :return: Returns a list of Element.
        """
        result = []
        queue = [node]

        while not len(queue) == 0:
            current = queue.pop(0)

            start = max(current.start_point[0] + 1, hunk_from);
            end = min(current.end_point[0] + 1, hunk_to);

            if (end >= start):
                if current.type in language.get_elements_to_collect():
                    element = CodeElement(current.type, current.start_point[0] + 1, current.end_point[0] + 1)
                    element.set_body_preview(current.text)

                    if current.type == "class_declaration":
                        element.set_declaration(Visitor.__get_class_declaration(current))
                    if current.type == "method_declaration":
                        element.set_declaration(Visitor.__get_method_declaration(current))
                    if current.type == "constructor_declaration":
                        element.set_declaration(Visitor.__get_method_declaration(current))

                    result.append(element)

            for child in current.children:
                queue.append(child)

        return result

    @staticmethod
    def __get_class_declaration(node):
        """
        For methods, computes the method name.

        :param node: The node representing the method.
        :return: Returns the method's name.
        """
        for chield in node.children:
            if chield.type == 'identifier':
                return chield.text.decode("utf-8")

    @staticmethod
    def __get_method_declaration(node):
        """
        For classes, computes the class name.

        :param node: The node representing the class.
        :return: Returns the class's name.
        """
        for chield in node.children:
            if chield.type == 'identifier':
                return chield.text.decode("utf-8")



""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.git.repository import Repository
from src.language.java import Java
from src.language.python import Python
from src.diff.diff import Diff
from src.git.commit import Commit
from copy import deepcopy
from src.treesitter.tree_sitter_setup import TreeSetup
from src.treesitter.tree_sitter_visitor import Visitor

class TestTreeVisitor:

    def test_visit_case_one(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='2a27d09a1716a1a0bc73101fb0a8a864996cd005', parent='5c7c6c470260c3cb6964fae96d4deb17ee82dba4')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        file_right.compute_content_current(repository, commit)
        file_left.compute_content_parent(repository, commit)

        diff = Diff(file_right, file_left)
        diff.compute_diff(repository)
        diff.compute_hunks()

        parser = TreeSetup(Java(), "").parser()

        tree_left = parser.parse(str.encode(file_left.get_raw_content()))
        tree_right = parser.parse(str.encode(file_right.get_raw_content()))

        elements_left = Visitor.visit_and_compare_hunk_left(tree_left.root_node, diff.get_hunks()[1], Java())
        elements_right = Visitor.visit_and_compare_hunk_right(tree_right.root_node, diff.get_hunks()[1], Java())

        assert len(elements_left) == 2
        assert elements_left[0].get_type() == "class_declaration"
        assert elements_left[0].get_declaration() == "PascalTriangleTest"
        assert elements_left[1].get_type() == "method_declaration"
        assert elements_left[1].get_declaration() == "testForOne"

        assert len(elements_right) == 2
        assert elements_right[0].get_type() == "class_declaration"
        assert elements_right[0].get_declaration() == "PascalTriangleTest"
        assert elements_right[1].get_type() == "method_declaration"
        assert elements_right[1].get_declaration() == "testForOne"

    def test_visit_case_two(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='e572354976847d3cf4c5915bd2433402730dd935', parent='c0b2c5662812741345b076f76ae236a1e40cb056')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]

        file_right = deepcopy(file)
        file_left = deepcopy(file)

        file_right.compute_content_current(repository, commit)
        file_left.compute_content_parent(repository, commit)

        diff = Diff(file_right, file_left)
        diff.compute_diff(repository)
        diff.compute_hunks()

        parser = TreeSetup(Java(), "").parser()

        tree_left = parser.parse(str.encode(file_left.get_raw_content()))
        tree_right = parser.parse(str.encode(file_right.get_raw_content()))

        elements_left = Visitor.visit_and_compare_hunk_left(tree_left.root_node, diff.get_hunks()[0], Java())
        elements_right = Visitor.visit_and_compare_hunk_right(tree_right.root_node, diff.get_hunks()[0], Java())

        assert len(elements_left) == 4
        assert elements_left[0].get_type() == "class_declaration"
        assert elements_left[0].get_declaration() == "MinHeap"
        assert elements_left[0].get_start_position() == 11
        assert elements_left[0].get_end_position() == 127

        assert elements_left[1].get_type() == "method_declaration"
        assert elements_left[1].get_declaration() == "toggleUp"
        assert elements_left[1].get_start_position() == 50
        assert elements_left[1].get_end_position() == 56

        assert elements_left[3].get_type() == "binary_expression"
        assert elements_left[3].get_start_position() == 53
        assert elements_left[3].get_end_position() == 53

        assert len(elements_right) == 4
        assert elements_right[0].get_type() == "class_declaration"
        assert elements_right[0].get_declaration() == "MinHeap"
        assert elements_right[0].get_start_position() == 11
        assert elements_right[0].get_end_position() == 127

        assert elements_right[1].get_type() == "method_declaration"
        assert elements_right[1].get_declaration() == "toggleUp"
        assert elements_right[1].get_start_position() == 50
        assert elements_right[1].get_end_position() == 56

        assert elements_right[3].get_type() == "binary_expression"
        assert elements_right[3].get_start_position() == 53
        assert elements_right[3].get_end_position() == 53

    def test_visit_case_tree(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        repository.clone_repo()

        commit = Commit(current='54f765bdd0331f4b9381de8c879218ace1313be9', parent='d28ac6483a97deb5ac09a5261d851e97a25c2ee5')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        file_right.compute_content_current(repository, commit)
        file_left.compute_content_parent(repository, commit)

        diff = Diff(file_right, file_left)
        diff.compute_diff(repository)
        diff.compute_hunks()

        parser = TreeSetup(Python(), "").parser()

        tree_left = parser.parse(str.encode(file_left.get_raw_content()))
        tree_right = parser.parse(str.encode(file_right.get_raw_content()))

        elements_left = Visitor.visit_and_compare_hunk_left(tree_left.root_node, diff.get_hunks()[3], Python())
        elements_right = Visitor.visit_and_compare_hunk_right(tree_right.root_node, diff.get_hunks()[3], Python())

        assert len(elements_left) == 1
        assert elements_left[0].get_type() == "while_statement"
        assert elements_left[0].get_start_position() == 52
        assert elements_left[0].get_end_position() == 68

        assert len(elements_right) == 1
        assert elements_right[0].get_type() == "while_statement"
        assert elements_right[0].get_start_position() == 58
        assert elements_right[0].get_end_position() == 75

    def test_visit_case_four(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        repository.clone_repo()

        commit = Commit(current='b2a77cc4fb922ab66f0978e45c108bdb4c30396d', parent='24d3cf82445e3f4a2e5287829395a3bf1353a8a3')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        file_right.compute_content_current(repository, commit)
        file_left.compute_content_parent(repository, commit)

        diff = Diff(file_right, file_left)
        diff.compute_diff(repository)
        diff.compute_hunks()

        parser = TreeSetup(Python(), "").parser()

        tree_left = parser.parse(str.encode(file_left.get_raw_content()))
        tree_right = parser.parse(str.encode(file_right.get_raw_content()))

        elements_left = Visitor.visit_and_compare_hunk_left(tree_left.root_node, diff.get_hunks()[0], Python())
        elements_right = Visitor.visit_and_compare_hunk_right(tree_right.root_node, diff.get_hunks()[0], Python())

        assert len(elements_left) == 0
        assert len(elements_right) == 7
        assert elements_right[0].get_type() == "if_statement"
        assert elements_right[0].get_start_position() == 81
        assert elements_right[0].get_end_position() == 101

        assert elements_right[1].get_type() == "try_statement"
        assert elements_right[1].get_start_position() == 39
        assert elements_right[1].get_end_position() == 78

        assert elements_right[6].get_type() == "for_statement"
        assert elements_right[6].get_start_position() == 60
        assert elements_right[6].get_end_position() == 73
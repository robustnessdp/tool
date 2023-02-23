""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.diff.hunk import Hunk, ChangeType

class TestHunk():

    def test_constructor(self):
        hunk = Hunk(left_from=0, left_to=0, right_from=0, right_to=0, change_type=ChangeType.DELETION)
        assert hunk.get_left_from() == 0
        assert hunk.get_left_to() == 0
        assert hunk.get_right_from() == 0
        assert hunk.get_right_to() == 0
        assert hunk.get_change_type() == ChangeType.DELETION

        hunk = Hunk(left_from=10, left_to=123, right_from=9, right_to=124, change_type=ChangeType.CHANGE)
        assert hunk.get_left_from() == 10
        assert hunk.get_left_to() == 123
        assert hunk.get_right_from() == 9
        assert hunk.get_right_to() == 124
        assert hunk.get_change_type() == ChangeType.CHANGE

        hunk = Hunk(left_from=1210, left_to=123423, right_from=-1, right_to=124234, change_type=ChangeType.ADDITION)
        assert hunk.get_left_from() == 1210
        assert hunk.get_left_to() == 123423
        assert hunk.get_right_from() == -1
        assert hunk.get_right_to() == 124234
        assert hunk.get_change_type() == ChangeType.ADDITION

        hunk = Hunk(left_from=None, left_to=None, right_from=None, right_to=None, change_type=None)
        assert hunk.get_left_from() == None
        assert hunk.get_left_to() == None
        assert hunk.get_right_from() == None
        assert hunk.get_right_to() == None
        assert hunk.get_change_type() == None

    def test_getters_and_setters(self):
        hunk = Hunk(left_from=None, left_to=None, right_from=None, right_to=None, change_type=None)
        hunk.set_left_from(10)
        hunk.set_left_to(123)
        hunk.set_right_from(9)
        hunk.set_right_to(124)
        hunk.set_change_type(ChangeType.CHANGE)

        assert hunk.get_left_from() == 10
        assert hunk.get_left_to() == 123
        assert hunk.get_right_from() == 9
        assert hunk.get_right_to() == 124
        assert hunk.get_change_type() == ChangeType.CHANGE

        hunk.set_left_from(10123)
        hunk.set_left_to(145323)
        hunk.set_right_from(5349)
        hunk.set_right_to(5663)
        hunk.set_change_type(ChangeType.DELETION)

        assert hunk.get_left_from() == 10123
        assert hunk.get_left_to() == 145323
        assert hunk.get_right_from() == 5349
        assert hunk.get_right_to() == 5663
        assert hunk.get_change_type() == ChangeType.DELETION

        hunk.set_left_from(1)
        hunk.set_left_to(-828)
        hunk.set_right_from(-24)
        hunk.set_right_to(2453)
        hunk.set_change_type(ChangeType.DELETION)

        assert hunk.get_left_from() == 1
        assert hunk.get_left_to() == -828
        assert hunk.get_right_from() == -24
        assert hunk.get_right_to() == 2453
        assert hunk.get_change_type() == ChangeType.DELETION
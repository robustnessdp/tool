""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""


from src.aggregator.hunk_element_aggregator import HunkElementAggregator
from src.diff.hunk import Hunk
from src.element.code_element import CodeElement

class TestHunk():

    def test_constructor(self):
        he = HunkElementAggregator(hunk=Hunk())
        assert he.get_hunk() != None
        assert len(he.get_elements_left()) == 0
        assert len(he.get_elements_right()) == 0
        assert isinstance(he.get_hunk(), Hunk)

        he = HunkElementAggregator(hunk=Hunk())
        assert he.get_hunk() != None
        assert len(he.get_elements_left()) == 0
        assert len(he.get_elements_right()) == 0
        assert isinstance(he.get_hunk(), Hunk)

        he = HunkElementAggregator(hunk=None)
        assert len(he.get_elements_left()) == 0
        assert len(he.get_elements_right()) == 0
        assert he.get_hunk() == None

    def test_getters_and_setters(self):
        he = HunkElementAggregator(hunk=None)
        he.set_hunk(Hunk())
        he.set_element_left([])
        he.set_element_right([])

        assert he.get_hunk() != None
        assert isinstance(he.get_elements_left(), list)
        assert isinstance(he.get_elements_right(), list)
        assert len(he.get_elements_left()) == 0
        assert len(he.get_elements_right()) == 0

        he = HunkElementAggregator(hunk=None)
        he.set_hunk(Hunk())
        he.set_element_left([CodeElement(None, None, None) for x in range(0, 453)])
        he.set_element_right([CodeElement(None, None, None) for x in range(0, 3452)])

        assert he.get_hunk() != None
        assert isinstance(he.get_elements_left(), list)
        assert isinstance(he.get_elements_right(), list)
        assert len(he.get_elements_left()) == 453
        assert len(he.get_elements_right()) == 3452

        he = HunkElementAggregator(hunk=None)
        he.set_hunk(Hunk())
        he.set_element_left([CodeElement(None, None, None) for x in range(0, 2344)])
        he.set_element_right([CodeElement(None, None, None) for x in range(0, 3434)])

        assert he.get_hunk() != None
        assert isinstance(he.get_elements_left(), list)
        assert isinstance(he.get_elements_right(), list)
        assert len(he.get_elements_left()) == 2344
        assert len(he.get_elements_right()) == 3434

        he = HunkElementAggregator(hunk=None)
        for i in range (0, 100):
            element = CodeElement(type='class_declaration', start_position=0, end_position= 101)
            he.add_elements_left([element])
            he.add_elements_right([element])
            assert len(he.get_elements_left()) == i + 1
            assert len(he.get_elements_right()) == i + 1


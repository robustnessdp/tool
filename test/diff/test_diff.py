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
from src.diff.diff import Diff
from src.diff.hunk import Hunk
from src.git.commit import Commit
from copy import deepcopy
from src.git.file import File

class TestDiff():

    def test_constructor(self):
        diff = Diff(file_left=File(name="myfile"), file_right=File(name="myfile"))
        assert isinstance(diff.get_diff(), list)
        assert len(diff.get_diff()) == 0
        assert isinstance(diff.get_file_left(), File)
        assert isinstance(diff.get_file_right(), File)
        assert isinstance(diff.get_hunks(), list)
        assert len(diff.get_hunks()) == 0

        diff = Diff(file_left=None, file_right=None)
        assert isinstance(diff.get_diff(), list)
        assert len(diff.get_diff()) == 0
        assert diff.get_file_left() == None
        assert diff.get_file_right() == None
        assert isinstance(diff.get_hunks(), list)
        assert len(diff.get_hunks()) == 0

        diff = Diff(file_left=File(name="myfile2"), file_right=File(name="myfile2"))
        assert isinstance(diff.get_diff(), list)
        assert len(diff.get_diff()) == 0
        assert isinstance(diff.get_file_left(), File)
        assert isinstance(diff.get_file_right(), File)
        assert isinstance(diff.get_hunks(), list)
        assert len(diff.get_hunks()) == 0

    def test_getters_and_setters(self):
        diff = Diff(file_left=None, file_right=None)
        diff.set_file_left(File(name="myfile"))
        diff.set_file_right(File(name="myfile"))

        diff.set_diff([x for x in range(0, 100)])
        diff.set_hunks([Hunk() for x in range(0, 124)])

        assert isinstance(diff.get_diff(), list)
        assert len(diff.get_diff()) == 100
        assert isinstance(diff.get_file_left(), File)
        assert isinstance(diff.get_file_right(), File)
        assert isinstance(diff.get_hunks(), list)
        assert len(diff.get_hunks()) == 124


        diff = Diff(file_left=None, file_right=None)
        diff.set_file_left(File(name="myfile"))
        diff.set_file_right(File(name="myfile"))

        diff.set_diff([x for x in range(0, 323)])
        diff.set_hunks([Hunk() for x in range(0, 545)])

        assert isinstance(diff.get_diff(), list)
        assert len(diff.get_diff()) == 323
        assert isinstance(diff.get_file_left(), File)
        assert isinstance(diff.get_file_right(), File)
        assert isinstance(diff.get_hunks(), list)
        assert len(diff.get_hunks()) == 545

        diff = Diff(file_left=None, file_right=None)
        diff.set_file_left(File(name="myfile"))
        diff.set_file_right(File(name="myfile"))

        diff.set_diff([x for x in range(0, 24534)])
        diff.set_hunks([Hunk() for x in range(0, 56745)])

        assert isinstance(diff.get_diff(), list)
        assert len(diff.get_diff()) == 24534
        assert isinstance(diff.get_file_left(), File)
        assert isinstance(diff.get_file_right(), File)
        assert isinstance(diff.get_hunks(), list)
        assert len(diff.get_hunks()) == 56745

    def test_diff_and_hunks_case_one(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='0d1110a66465ed39afac087794da93aac7f30def', parent='b33c7786b4b7c13ce8b2259a2ddb36175851dbed')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        file_right.compute_content_current(repository, commit)
        file_left.compute_content_parent(repository, commit)

        diff = Diff(file_right, file_left)
        diff.compute_diff(repository)
        diff.compute_hunks()

        assert diff.get_diff() != None
        assert len(diff.get_diff()) == 4
        assert len(diff.get_hunks()) == 1
        assert isinstance(diff.get_hunks()[0], Hunk)
        assert diff.get_hunks()[0].get_left_from() == 71
        assert diff.get_hunks()[0].get_left_to() == 71
        assert diff.get_hunks()[0].get_right_from() == 71
        assert diff.get_hunks()[0].get_right_to() == 71

    def test_diff_and_hunks_case_two(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='c8b0a201da9579a0c83063685d478284414f3630', parent='9f7613b467bda734cdea196013c8fdfe19af81a2')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        file_right.compute_content_current(repository, commit)
        file_left.compute_content_parent(repository, commit)

        diff = Diff(file_right, file_left)
        diff.compute_diff(repository)
        diff.compute_hunks()

        assert diff.get_diff() != None
        assert len(diff.get_diff()) == 9
        assert len(diff.get_hunks()) == 1
        assert isinstance(diff.get_hunks()[0], Hunk)
        assert diff.get_hunks()[0].get_left_from() == 24
        assert diff.get_hunks()[0].get_left_to() == 28
        assert diff.get_hunks()[0].get_right_from() == 24
        assert diff.get_hunks()[0].get_right_to() == 25

    def test_diff_and_hunks_case_three(self):
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

        assert diff.get_diff() != None
        assert len(diff.get_diff()) == 75
        assert len(diff.get_hunks()) == 4
        assert isinstance(diff.get_hunks()[0], Hunk)

        assert diff.get_hunks()[0].get_left_from() == 1
        assert diff.get_hunks()[0].get_left_to() == 1
        assert diff.get_hunks()[0].get_right_from() == 0
        assert diff.get_hunks()[0].get_right_to() == 0

        assert diff.get_hunks()[1].get_left_from() == 10
        assert diff.get_hunks()[1].get_left_to() == 13
        assert diff.get_hunks()[1].get_right_from() == 9
        assert diff.get_hunks()[1].get_right_to() == 11

        assert diff.get_hunks()[2].get_left_from() == 15
        assert diff.get_hunks()[2].get_left_to() == 40
        assert diff.get_hunks()[2].get_right_from() == 13
        assert diff.get_hunks()[2].get_right_to() == 14

        assert diff.get_hunks()[3].get_left_from() == 41
        assert diff.get_hunks()[3].get_left_to() == 41
        assert diff.get_hunks()[3].get_right_from() == 16
        assert diff.get_hunks()[3].get_right_to() == 48
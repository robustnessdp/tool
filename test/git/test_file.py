""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.git.commit import Commit
from copy import deepcopy
from src.git.file import File
from src.git.repository import Repository
from src.language.java import Java

class TestFile():

    def test_constructor(self):
        file = File(name="myfile")
        assert file.get_name() == "myfile"
        assert file.get_raw_content() == None

        file = File(name="myfile2")
        assert file.get_name() == "myfile2"
        assert file.get_raw_content() == None

        file = File(name=None)
        assert file.get_name() == None
        assert file.get_raw_content() == None

        file = File(name="")
        assert file.get_name() == ""
        assert file.get_raw_content() == None

    def test_getters_and_setters(self):
        file = File(name=None)
        file.set_name("myfile")
        file.set_raw_content("")
        assert file.get_name() == "myfile"
        assert file.get_raw_content() == ""

        file = File(name="myfile2")
        file.set_name("myfile2")
        file.set_raw_content("This is my file content")
        assert file.get_name() == "myfile2"
        assert file.get_raw_content() == "This is my file content"

        file = File(name=None)
        file.set_name(None)
        file.set_raw_content(None)
        assert file.get_name() == None
        assert file.get_raw_content() == None

        file = File(name="")
        file.set_name("")
        file.set_raw_content("platform darwin -- Python 3.8.9, pytest-7.1.2, pluggy-1.0.0")
        assert file.get_name() == ""
        assert file.get_raw_content() == "platform darwin -- Python 3.8.9, pytest-7.1.2, pluggy-1.0.0"

    def test_compute_content_case_one(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='2a27d09a1716a1a0bc73101fb0a8a864996cd005', parent='5c7c6c470260c3cb6964fae96d4deb17ee82dba4')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        status, _, _ = file_left.compute_content_current(repository, commit)
        assert status == 0
        assert file_left.get_raw_content() != None
        assert len(file_left.get_raw_content()) >= 0

        status, _, _ = file_right.compute_content_current(repository, commit)
        assert status == 0
        assert file_right.get_raw_content() != None
        assert len(file_right.get_raw_content()) >= 0

    def test_compute_content_case_two(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='c8b0a201da9579a0c83063685d478284414f3630', parent='9f7613b467bda734cdea196013c8fdfe19af81a2')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        status, _, _ = file_left.compute_content_current(repository, commit)
        assert status == 0
        assert file_left.get_raw_content() != None
        assert len(file_left.get_raw_content()) >= 0

        status, _, _ = file_right.compute_content_current(repository, commit)
        assert status == 0
        assert file_right.get_raw_content() != None
        assert len(file_right.get_raw_content()) >= 0

    def test_compute_content_case_three(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='2a27d09a1716a1a0bc73101fb0a8a864996cd005', parent='5c7c6c470260c3cb6964fae96d4deb17ee82dba4')
        commit.compute_changed_files(repository)

        file = list(commit.get_changed_files())[0]
        file_right = deepcopy(file)
        file_left = deepcopy(file)

        status, _, _ = file_left.compute_content_current(repository, commit)
        assert status == 0
        assert file_left.get_raw_content() != None
        assert len(file_left.get_raw_content()) >= 0

        status, _, _ = file_right.compute_content_current(repository, commit)
        assert status == 0
        assert file_right.get_raw_content() != None
        assert len(file_right.get_raw_content()) >= 0
""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.git.repository import Repository
from src.language.python import Python
from src.git.commit import Commit
from src.git.author import Author
from src.language.java import Java

class TestAuthor():

    def test_constructor(self):
        author = Author(name="Name", email="email@email.com")
        assert author.get_name() == "Name"
        assert author.get_email() == "email@email.com"

        author = Author(name=None, email=None)
        assert author.get_name() == None
        assert author.get_email() == None

        author = Author(name="", email="")
        assert author.get_name() == ""
        assert author.get_email() == ""

    def test_getters_and_setters(self):
        author = Author(name=None, email=None)
        author.set_name("Name")
        author.set_email("email@email.com")
        assert author.get_name() == "Name"
        assert author.get_email() == "email@email.com"

        author = Author(name=None, email=None)
        author.set_name("")
        author.set_email("")
        assert author.get_name() == ""
        assert author.get_email() == ""

        author = Author(name=None, email=None)
        author.set_name(None)
        author.set_email(None)
        assert author.get_name() == None
        assert author.get_email() == None

    def test_compute_author_case_one(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        repository.clone_repo()

        commit = Commit(current='b2a77cc4fb922ab66f0978e45c108bdb4c30396d', parent='24d3cf82445e3f4a2e5287829395a3bf1353a8a3')
        author = Author(name=None, email=None)
        author.compute_author(repository, commit)

        assert author.get_name() == "Saptarshi Sengupta"
        assert author.get_email() == "94242536+saptarshi1996@users.noreply.github.com"

    def test_compute_author_case_two(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()

        commit = Commit(current='2a27d09a1716a1a0bc73101fb0a8a864996cd005', parent='5c7c6c470260c3cb6964fae96d4deb17ee82dba4')
        author = Author(name=None, email=None)
        author.compute_author(repository, commit)

        assert author.get_name() == "ArunPrasanth-V"
        assert author.get_email() == "88626504+ArunPrasanth-V@users.noreply.github.com"
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

class TestRepository:
    def test_constructor(self):

        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        assert repository.get_remote_path() == 'https://github.com/<supressed>/Java.git'
        assert repository.get_local_path() == '/Users/<supressed>/PycharmProjects/pfp/input/Java/'
        assert repository.get_branch() == 'master'
        assert isinstance(repository.get_language(), Java)
        assert repository.get_commits() == list()

        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        assert repository.get_remote_path() == 'https://github.com/<supressed>/Python.git'
        assert repository.get_local_path() == '/Users/<supressed>/PycharmProjects/pfp/input/Python/'
        assert repository.get_branch() == 'master'
        assert isinstance(repository.get_language(), Python)
        assert isinstance(repository.get_commits(), list)

        repository = Repository(remote_path=None, local_path=None, branch=None, language=None)
        assert repository.get_remote_path() == None
        assert repository.get_local_path() == None
        assert repository.get_branch() == None
        assert repository.get_language() == None
        assert isinstance(repository.get_commits(), list)

        repository = Repository(remote_path="", local_path="", branch="", language=None)
        assert repository.get_remote_path() == ""
        assert repository.get_local_path() == ""
        assert repository.get_branch() == ""
        assert repository.get_language() == None
        assert isinstance(repository.get_commits(), list)

    def test_getters_and_setters(self):

        repository = Repository(remote_path=None, local_path=None, branch=None, language=None)

        repository.set_remote_path('https://github.com/<supressed>/Java.git')
        repository.set_local_path('/Users/<supressed>/PycharmProjects/pfp/input/Java/')
        repository.set_branch('master')
        repository.set_language(Java())
        repository.set_commits(list())

        assert repository.get_remote_path() == 'https://github.com/<supressed>/Java.git'
        assert repository.get_local_path() == '/Users/<supressed>/PycharmProjects/pfp/input/Java/'
        assert repository.get_branch() == 'master'
        assert isinstance(repository.get_language(), Java)
        assert isinstance(repository.get_commits(), list)
        assert len(repository.get_commits()) == 0

        repository = Repository(remote_path=None, local_path=None, branch=None, language=None)

        repository.set_remote_path('')
        repository.set_local_path('')
        repository.set_branch('')
        repository.set_language(Java())
        repository.set_commits(list())

        assert repository.get_remote_path() == ''
        assert repository.get_local_path() == ''
        assert repository.get_branch() == ''
        assert isinstance(repository.get_language(), Java)
        assert isinstance(repository.get_commits(), list)
        assert len(repository.get_commits()) == 0

    def test_clone_delete(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())

        # Test repository deletion
        (status, stdout, stderr) = repository.delete_repo()
        assert status == 0

        (status, stdout, stderr) = repository.clone_repo()
        assert status == 0

        # Test repository cloning when already exists
        (status, stdout, stderr) = repository.clone_repo()
        assert status != 0

        # Test repository deletion
        (status, stdout, stderr) = repository.delete_repo()
        assert status == 0

        # Different repository
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())

        # Test repository deletion
        (status, stdout, stderr) = repository.delete_repo()
        assert status == 0

        # Test clone
        (status, stdout, stderr) = repository.clone_repo()
        assert status == 0

        # Test repository cloning when already exists
        (status, stdout, stderr) = repository.clone_repo()
        assert status != 0

        # Test repository deletion
        (status, stdout, stderr) = repository.delete_repo()
        assert status == 0

    def test_checkout(self):
        # Test repository checkout
        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        repository.clone_repo()
        (status, stdout, stderr) = repository.branch_checkout()
        print(stderr)
        assert status == 0

        # Test repository checkout invalid branch
        repository.set_branch('main')
        (status, stdout, stderr) = repository.branch_checkout()
        assert status != 0
        repository.delete_repo()

        # Test repository checkout, different repository
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()
        (status, stdout, stderr) = repository.branch_checkout()
        assert status == 0

        # Test repository checkout invalid branch
        repository.set_branch('development')
        (status, stdout, stderr) = repository.branch_checkout()
        assert status != 0
        repository.delete_repo()

    def test_compute_commits(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Python.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        repository.clone_repo()
        repository.branch_checkout()
        repository.compute_commits()
        repository.delete_repo()
        assert isinstance(repository.get_commits(), list)
        assert len(repository.get_commits()) == 2426
        assert repository.get_commits()[0].get_current() == '4a51244e0feee90c8a80d6516628c9acb69c40b3'
        assert repository.get_commits()[15].get_current() == 'dbee5f072f68c57bce3443e5ed07fe496ba9d76d'
        assert repository.get_commits()[2312].get_current() == 'df8798416b47864b64723be00403d113c7472a7d'
        assert repository.get_commits()[2425].get_current() == '2636f3c62f1a407b2996da6e3fe6fdc5d1ccd764'

        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()
        repository.branch_checkout()
        repository.compute_commits()
        repository.delete_repo()

        assert isinstance(repository.get_commits(), list)
        assert len(repository.get_commits()) == 1642
        assert repository.get_commits()[0].get_current() == '6665ab262c91d59af1b3e2ce9b731772a8f39c41'
        assert repository.get_commits()[22].get_current() == '45f3e5b6def330827088751026e18527b838673d'
        assert repository.get_commits()[1638].get_current() == '9661bb3df62929cad320ce576c7e156a7c91a748'
        assert repository.get_commits()[1641].get_current() == '40d42574e065e8078b242d201e0fc1455c430c71'

""" Test Class.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from src.git.commit import Commit
from src.git.author import Author
from src.git.repository import Repository
from src.language.java import Java
from src.language.python import Python

class TestCommit():
    def test_constructor(self):
        commit = Commit(current='9e7d32e77f54ee0a17bccb5e555b84948c2849c0', parent='1e7345f3f825e45ae544a85ae59e07d82079cc63')
        assert commit.get_current() == '9e7d32e77f54ee0a17bccb5e555b84948c2849c0'
        assert commit.get_parent() == '1e7345f3f825e45ae544a85ae59e07d82079cc63'
        assert commit.get_author() == None
        assert commit.get_date() == None
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit = Commit(current='0733791b263e17773f340a36f2329958ed08123d', parent='89668bf3f7dfa6336e4ae6432b34c0d7058d2b75')
        assert commit.get_current() == '0733791b263e17773f340a36f2329958ed08123d'
        assert commit.get_parent() == '89668bf3f7dfa6336e4ae6432b34c0d7058d2b75'
        assert commit.get_author() == None
        assert commit.get_date() == None
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit = Commit(current='47d5229fa3e2cacef146079ad5fe82f61cd3fef3', parent='8877722bf376671cbc78b236eed5ad21125c032c')
        assert commit.get_current() == '47d5229fa3e2cacef146079ad5fe82f61cd3fef3'
        assert commit.get_parent() == '8877722bf376671cbc78b236eed5ad21125c032c'
        assert commit.get_author() == None
        assert commit.get_date() == None
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit = Commit(current='47d5229f', parent='8877722')
        assert commit.get_current() == '47d5229f'
        assert commit.get_parent() == '8877722'
        assert commit.get_author() == None
        assert commit.get_date() == None
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit = Commit()
        assert commit.get_current() == None
        assert commit.get_parent() == None
        assert commit.get_author() == None
        assert commit.get_date() == None
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

    def test_getters_and_setters(self):
        commit = Commit()
        commit.set_current('9e7d32e77f54ee0a17bccb5e555b84948c2849c0')
        commit.set_parent('1e7345f3f825e45ae544a85ae59e07d82079cc63')
        commit.set_author(Author())
        commit.set_date('01-01-2021')

        assert commit.get_current() == '9e7d32e77f54ee0a17bccb5e555b84948c2849c0'
        assert commit.get_parent() == '1e7345f3f825e45ae544a85ae59e07d82079cc63'
        assert commit.get_author() is not None
        assert commit.get_date() == '01-01-2021'
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit = Commit()
        commit.set_current('0733791b263e17773f340a36f2329958ed08123d')
        commit.set_parent('89668bf3f7dfa6336e4ae6432b34c0d7058d2b75')
        commit.set_author(Author())
        commit.set_date('20-02-2021')

        assert commit.get_current() == '0733791b263e17773f340a36f2329958ed08123d'
        assert commit.get_parent() == '89668bf3f7dfa6336e4ae6432b34c0d7058d2b75'
        assert commit.get_author() is not None
        assert commit.get_date() == '20-02-2021'
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit.set_current('47d5229fa3e2cacef146079ad5fe82f61cd3fef3')
        commit.set_parent('8877722bf376671cbc78b236eed5ad21125c032c')
        commit.set_author(Author())
        commit.set_date('12-03-2021')

        assert commit.get_current() == '47d5229fa3e2cacef146079ad5fe82f61cd3fef3'
        assert commit.get_parent() == '8877722bf376671cbc78b236eed5ad21125c032c'
        assert commit.get_author() is not None
        assert commit.get_date() == '12-03-2021'
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

        commit.set_current('47d5229')
        commit.set_parent('8877722')
        commit.set_author(Author())
        commit.set_date('14-05-2021')

        assert commit.get_current() == '47d5229'
        assert commit.get_parent() == '8877722'
        assert commit.get_author() is not None
        assert commit.get_date() == '14-05-2021'
        assert isinstance(commit.get_changed_files(), set)
        assert len(commit.get_changed_files()) == 0

    def test_compute_parent_and_date(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()
        repository.branch_checkout()
        repository.compute_commits()

        commit = repository.get_commits()[0]
        assert commit.get_current() == '6665ab262c91d59af1b3e2ce9b731772a8f39c41'
        assert commit.get_parent() == '2a237708739ffe5176dcc6750f9c814e08e0744b'
        assert commit.get_date() == '2022-06-29'

        commit = repository.get_commits()[22]
        assert commit.get_current() == '45f3e5b6def330827088751026e18527b838673d'
        assert commit.get_parent() == '77e481336ef147033811ea7f3d2e763089ace18c'
        assert commit.get_date() == '2022-06-08'

        commit = repository.get_commits()[1638]
        assert commit.get_current() == '9661bb3df62929cad320ce576c7e156a7c91a748'
        assert commit.get_parent() == '12d7c48ee4b7f415f19dda4a889032263cc3529a'
        assert commit.get_date() == '2016-07-22'

        commit = repository.get_commits()[1641]
        assert commit.get_current() == '40d42574e065e8078b242d201e0fc1455c430c71'
        assert commit.get_parent() == None
        assert commit.get_date() == '2016-07-16'

        repository = Repository(remote_path='https://github.com/<supressed>/Python.git',local_path='/Users/<supressed>/PycharmProjects/pfp/input/Python/', branch='master', language=Python())
        repository.clone_repo()
        repository.branch_checkout()
        repository.compute_commits()

        commit = repository.get_commits()[0]
        assert commit.get_current() == '4a51244e0feee90c8a80d6516628c9acb69c40b3'
        assert commit.get_parent() == '04bc8f01dd81b8f4ca68e470d046fcb571b4d3d0'
        assert commit.get_date() == '2022-06-23'

        commit = repository.get_commits()[15]
        assert commit.get_current() == 'dbee5f072f68c57bce3443e5ed07fe496ba9d76d'
        assert commit.get_parent() == 'e95ecfaf27c545391bdb7a2d1d8948943a40f828'
        assert commit.get_date() == '2022-05-13'

        commit = repository.get_commits()[2312]
        assert commit.get_current() == 'df8798416b47864b64723be00403d113c7472a7d'
        assert commit.get_parent() == 'cebbf567ec17d1b3e1017af2b7cda0119ba019a7'
        assert commit.get_date() == '2016-10-08'

        commit = repository.get_commits()[2425]
        assert commit.get_current() == '2636f3c62f1a407b2996da6e3fe6fdc5d1ccd764'
        assert commit.get_parent() == None
        assert commit.get_date() == '2016-07-16'

    def test_compute_chaged_files(self):
        repository = Repository(remote_path='https://github.com/<supressed>/Java.git', local_path='/Users/<supressed>/PycharmProjects/pfp/input/Java/', branch='master', language=Java())
        repository.clone_repo()
        repository.branch_checkout()
        repository.compute_commits()

        commit = repository.get_commits()[30]
        print(commit.get_current())
        commit.compute_changed_files(repository)
        assert len(commit.get_changed_files()) == 4
        assert 'src/test/java/com/thealgorithms/strings/longestNonRepeativeSubstringTest.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/main/java/com/thealgorithms/strings/longestNonRepeativeSubstring.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/main/java/com/thealgorithms/strings/zigZagPattern/zigZagPattern.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/test/java/com/thealgorithms/strings/zigZagPattern/zigZagPatternTest.java' in [file.get_name() for file in commit.get_changed_files()]

        commit = repository.get_commits()[41]
        commit.compute_changed_files(repository)

        assert len(commit.get_changed_files()) == 5
        assert 'src/main/java/com/thealgorithms/maths/VectorCrossProduct.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/main/java/com/thealgorithms/others/Implementing_auto_completing_features_using_trie.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/main/java/com/thealgorithms/misc/RangeInSortedArray.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/main/java/com/thealgorithms/dynamicprogramming/CoinChange.java' in [file.get_name() for file in commit.get_changed_files()]
        assert 'src/main/java/com/thealgorithms/datastructures/lists/CircleLinkedList.java' in [file.get_name() for file in commit.get_changed_files()]

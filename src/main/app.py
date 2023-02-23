from src.definitions import ROOT_DIR
from copy import deepcopy
from src.language.language import Language
from src.git.repository import Repository
from src.diff.diff import Diff
from src.treesitter.tree_sitter_visitor import Visitor
from src.treesitter.tree_sitter_setup import TreeSetup
from src.aggregator.hunk_element_aggregator import HunkElementAggregator
from src.jsonwriter.json_writer import JsonWriter
from src.git.author import Author

class App():

    def collect_full_data(self, remote_path, branch, language: Language):
        """
        First use case, collect the full data. All commits, all files.

        :param remote_path: url for the remote repository.
        :param branch: target branch.
        :param language: repository language.
        """

        repository = Repository(remote_path, self.__generate_local_path(remote_path), branch, language)

        try:
            repository.clone_repo()
        except Exception as err:
            print(err)

        try:
            repository.branch_checkout()
        except Exception as err:
            print(err)
            return

        repository.compute_commits()
        print(repository)

        for commit in repository.get_commits():
            try:
                commit.compute_changed_files(repository)
                commit.compute_date(repository)

                author = Author()
                author.compute_author(repository, commit)
                commit.set_author(author)

                print(commit)
                writer = JsonWriter()
                for file in commit.get_changed_files():
                    file_right = deepcopy(file)
                    file_left = deepcopy(file)

                    file_right.compute_content_current(repository, commit)
                    file_left.compute_content_parent(repository, commit)

                    diff = Diff(file_right, file_left)
                    diff.compute_diff(repository)
                    diff.compute_hunks()

                    parser = TreeSetup(language).parser()

                    tree_left = parser.parse(str.encode(file_left.get_raw_content()))
                    tree_right = parser.parse(str.encode(file_right.get_raw_content()))

                    root_node_left = tree_left.root_node
                    root_node_right = tree_right.root_node

                    output = []
                    for hunk in diff.get_hunks():
                        element = HunkElementAggregator(hunk)
                        element.add_elements_left(Visitor.visit_and_compare_hunk_left(root_node_left, hunk, language))
                        element.add_elements_right(Visitor.visit_and_compare_hunk_right(root_node_right, hunk, language))
                        output.append(element)

                    writer.append(commit, file, output)
                writer.write(file_name=commit.get_current())
            except Exception as err:
                print(err)
                continue

    def collect_all_file_commit_subset(self, remote_path, branch, language: Language, _hashs):
        """
        Second use case, all files in a commit subset.

        :param remote_path: url for the remote repository.
        :param branch: target branch.
        :param language: repository language.
        :param _hashs: list of hashs.
        """
        repository = Repository(remote_path, self.__generate_local_path(remote_path), branch, language)
        try:
            repository.clone_repo()
        except Exception as err:
            print(err)

        try:
            repository.branch_checkout()
        except Exception as err:
            print(err)
            return

        repository.set_commits(_hashs)
        print(repository)

        for commit in repository.get_commits():
            try:
                commit.compute_changed_files(repository)
                commit.compute_date(repository)

                author = Author()
                author.compute_author(repository, commit)
                commit.set_author(author)

                print(commit)
                writer = JsonWriter()
                for file in commit.get_changed_files():
                    file_right = deepcopy(file)
                    file_left = deepcopy(file)

                    file_right.compute_content_current(repository, commit)
                    file_left.compute_content_parent(repository, commit)

                    diff = Diff(file_right, file_left)
                    diff.compute_diff(repository)
                    diff.compute_hunks()

                    parser = TreeSetup(language).parser()

                    tree_left = parser.parse(str.encode(file_left.get_raw_content()))
                    tree_right = parser.parse(str.encode(file_right.get_raw_content()))

                    root_node_left = tree_left.root_node
                    root_node_right = tree_right.root_node

                    output = []
                    for hunk in diff.get_hunks():
                        element = HunkElementAggregator(hunk)
                        element.add_elements_left(Visitor.visit_and_compare_hunk_left(root_node_left, hunk, language))
                        element.add_elements_right(Visitor.visit_and_compare_hunk_right(root_node_right, hunk, language))
                        output.append(element)

                    writer.append(commit, file, output)
                writer.write(file_name=commit.get_current())
            except Exception as err:
                print(err)
                continue

    def collect_all_commit_file_subset(self, remote_path, branch, language: Language, _files):
        """
        Third use case, all commits in a file subset.

        :param remote_path: url for the remote repository.
        :param branch: target branch.
        :param language: repository language.
        :param _files: list of file names.
        """
        repository = Repository(remote_path, self.__generate_local_path(remote_path), branch, language)
        try:
            repository.clone_repo()
        except Exception as err:
            print(err)

        try:
            repository.branch_checkout()
        except Exception as err:
            print(err)
            return

        repository.compute_commits()
        print(repository)

        for commit in repository.get_commits():
            try:

                commit.compute_changed_files(repository)
                commit.compute_date(repository)

                author = Author()
                author.compute_author(repository, commit)
                commit.set_author(author)

                print(commit)
                writer = JsonWriter()
                for file in commit.get_changed_files():
                    if any([x for x in _files if x in file.get_name()]):
                        file_right = deepcopy(file)
                        file_left = deepcopy(file)

                        file_right.compute_content_current(repository, commit)
                        file_left.compute_content_parent(repository, commit)

                        diff = Diff(file_right, file_left)
                        diff.compute_diff(repository)
                        diff.compute_hunks()

                        parser = TreeSetup(language).parser()

                        tree_left = parser.parse(str.encode(file_left.get_raw_content()))
                        tree_right = parser.parse(str.encode(file_right.get_raw_content()))

                        root_node_left = tree_left.root_node
                        root_node_right = tree_right.root_node

                        output = []
                        for hunk in diff.get_hunks():
                            element = HunkElementAggregator(hunk)
                            element.add_elements_left(Visitor.visit_and_compare_hunk_left(root_node_left, hunk, language))
                            element.add_elements_right(Visitor.visit_and_compare_hunk_right(root_node_right, hunk, language))
                            output.append(element)

                        writer.append(commit, file, output)
                writer.write(file_name=commit.get_current())
            except Exception as err:
                print(err)
                continue

    def collect_one_file_one_commit(self, remote_path, branch, language: Language, _hash, _file):
        """
        Fouth use case, one commit, one file.

        :param remote_path: url for the remote repository.
        :param branch: target branch.
        :param language: repository language.
        :param _hash: list of hashs.
        :param _file: list of file names.
        """
        repository = Repository(remote_path, self.__generate_local_path(remote_path), branch, language)
        try:
            repository.clone_repo()
        except Exception as err:
            print(err)

        try:
            repository.branch_checkout()
        except Exception as err:
            print(err)
            return

        repository.set_commits([_hash])
        print(repository)

        for commit in repository.get_commits():
            try:
                commit.compute_changed_files(repository)
                commit.compute_date(repository)

                author = Author()
                author.compute_author(repository, commit)
                commit.set_author(author)

                print(commit)
                writer = JsonWriter()
                for file in commit.get_changed_files():
                    if any([x for x in [_file] if x in file.get_name()]):

                        file_right = deepcopy(file)
                        file_left = deepcopy(file)

                        file_right.compute_content_current(repository, commit)
                        file_left.compute_content_parent(repository, commit)

                        diff = Diff(file_right, file_left)
                        diff.compute_diff(repository)
                        diff.compute_hunks()
                        print(diff.get_diff())

                        parser = TreeSetup(language).parser()

                        tree_left = parser.parse(str.encode(file_left.get_raw_content()))
                        tree_right = parser.parse(str.encode(file_right.get_raw_content()))

                        root_node_left = tree_left.root_node
                        root_node_right = tree_right.root_node

                        output = []
                        for hunk in diff.get_hunks():
                            print(hunk)
                            element = HunkElementAggregator(hunk)
                            element.add_elements_left(Visitor.visit_and_compare_hunk_left(root_node_left, hunk, language))
                            element.add_elements_right(
                                Visitor.visit_and_compare_hunk_right(root_node_right, hunk, language))
                            output.append(element)

                        writer.append(commit, file, output)

                writer.write(file_name=commit.get_current())
            except Exception as err:
                print(err)
                continue

    def __generate_local_path(self, remote_path):
        return ROOT_DIR.rsplit("/", 1)[0] + "/input/" + remote_path.rsplit("/", 1)[1].replace(".git", "")
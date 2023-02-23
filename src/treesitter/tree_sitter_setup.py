""" Class for setup the Tree Sitter.

Setup the Tree Sitter (https://tree-sitter.github.io/tree-sitter/) to support the target languages.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""

from tree_sitter import Language as LanguageTreeSitter, Parser
from src.language.language import Language
from src.language.java import Java
from src.language.python import Python

class TreeSetup():

  def __init__(self, language: Language, lib_root_dir="../"):
    """
    Construct a new TreeSetup object, besides initialize the Tree Sitter for the target language.

    :param language: The Language object, defining the target language to be parsed.
    :return: Returns nothing.
    """

    LanguageTreeSitter.build_library(
      # Store the library in the `src` directory
      lib_root_dir + 'my-languages.so',
      [
        lib_root_dir + 'tree-sitter-java',
        lib_root_dir + 'tree-sitter-python',
      ]
    )

    self.__language = language
    if isinstance(self.__language, Java):
      self.JAVA_LANGUAGE = LanguageTreeSitter(lib_root_dir + 'my-languages.so', 'java')
    elif isinstance(self.__language, Python):
      self.PY_LANGUAGE = LanguageTreeSitter(lib_root_dir + 'my-languages.so', 'python')


  def parser(self):
    """
    Constructs the Tree Sitter parser for the language.

    :return: The parser for the language.
    """
    parser = Parser()
    if isinstance(self.__language, Java):
      parser.set_language(self.JAVA_LANGUAGE)
    elif isinstance(self.__language, Python):
      parser.set_language(self.PY_LANGUAGE)

    return parser


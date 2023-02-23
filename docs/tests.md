---
## Quality assurance 

To perform the system tests, we employ the [pytest](https://docs.pytest.org/en/7.1.x/) library. 

The tests were designed to ensure the tool quality, and guarantee that it meets the requirements and scope.

Since our tool operates mainly over repositories, we create two dummy repositories ([Java](https://github.com/<supressed>/Java/) and [Python](https://github.com/<supressed>/Python/)) for tests.

#### Executing

To execute the tests, run in the root directory: ```pytest test/```

All the tests log is available [**here**](https://htmlpreview.github.io/?https://github.com/<supressed>/<supressed>/blob/main/docs/test_log.html).

--- 
### Test Suits

##### [test.aggregator](https://github.com/<supressed>/<supressed>/tree/main/test/aggregator)
- Contains unit tests for the class hunk_element_aggregator.py.

  - Procedures tested by this suite
    - Unit tests.

##### [test.diff](https://github.com/<supressed>/<supressed>/tree/main/test/diff)
- Contains unit and integration tests for the classes diff.py and hunk.py.

  - Procedures tested by this suite
    - Procedures to compute diffs between files.
    - Procedures to extract hunks of changes from diffs.
    - Others.
    
##### [test.element](https://github.com/<supressed>/<supressed>/tree/main/test/element)
- Contains unit tests for the class code_element.py.

  - Procedures tested by this suite
    - Unit tests.

##### [test.git](https://github.com/<supressed>/<supressed>/tree/main/test/git)
- Unit and integration tests for the classes author.py, commit.py, repository.py and file.py.

  - Procedures tested by this suite
    - Procedures to clone, delete, and checkout repositories. 
    - Procedures to manipulate file content.
    - Procedures to get the list of commits in a repository.
    - Procedure to get all changed files in a commit.
    - Procedure to recovery a file content at certain commit.
    - Procedure to recovery commit's author information.
    - Procedure to collect commit's date.
    - Others.
  
  Obs: some tests in this suit might take a few minutes, since repository clone operation depends on network connection.

##### [test.language](https://github.com/<supressed>/<supressed>/tree/main/test/language)
- Unit tests for the language.py and its subclasses.
  
  - Procedures tested by this suite
    - Procedures to define the target files to be collected for the language.
    - Procedures to recovery code elements to be collected for the language.
    - Others.
    
##### [test.treesitter](https://github.com/<supressed>/<supressed>/tree/main/test/treesitter)
- Unit and integration tests for tree_sitter_visitor.py. 

  - Procedures tested by this suite
    - Procedures to create a new AST parser for the target language.
    - Procedures to collect code elements changed between commits.
    - Others.
  
---

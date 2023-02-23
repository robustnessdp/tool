""" Class modeling the entity for write the system output in json format.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""
import json

class JsonWriter():

    def __init__(self):
        """
        Construct a new JsonWriter object, starting a new buffer.
        """
        self.__out__ = {}

    def append(self, commit, file, hunk_element_aggregator):
        """
        Format the data received as parameter and append it on the current buffer.

        :param commit: The Commit object analysed.
        :param file: The File object analysed.
        :param hunk_element_aggregator: List of HunkElementAggregator.
        :return: Return nothing
        """
        if 'parent' not in self.__out__:
            self.__out__['parent'] = str(commit.get_parent())

        if 'date' not in self.__out__:
            self.__out__['date'] = str(commit.get_date())

        if 'author' not in self.__out__:
            self.__out__['author'] = {}

        if 'files' not in self.__out__:
            self.__out__['files'] = {}

        if file.get_name() not in self.__out__['files']:
            self.__out__['files'].update({file.get_name(): {}})

        if 'hunks' not in self.__out__['files'][file.get_name()]:
            self.__out__['files'][str(file.get_name())]['hunks'] = {}

        self.__out__['author'].update({"name": commit.get_author().get_name(), "email": commit.get_author().get_email()})

        for he in hunk_element_aggregator:
            self.__out__['files'][str(file.get_name())]['hunks'].update({he.get_hunk().get_id() : {"left_from" : he.get_hunk().get_left_from(), "left_to" : he.get_hunk().get_left_to(), "right_from" : he.get_hunk().get_right_from(), "right_to" : he.get_hunk().get_right_to()}})

            for e in he.get_elements_left():
                if "left_touched_elements" not in self.__out__['files'][str(file.get_name())]['hunks'][he.get_hunk().get_id()]:
                    self.__out__['files'][str(file.get_name())]['hunks'][he.get_hunk().get_id()]['left_touched_elements'] = {}

                self.__out__['files'][str(file.get_name())]['hunks'][he.get_hunk().get_id()]['left_touched_elements'].update({e.get_id() : {"identifier": e.get_type(), "declaration": e.get_declaration(), "start": e.get_start_position(), "end": e.get_end_position(), "body_preview": e.get_body_preview()}})

            for e in he.get_elements_right():
                if "right_touched_elements" not in self.__out__['files'][str(file.get_name())]['hunks'][he.get_hunk().get_id()]:
                    self.__out__['files'][str(file.get_name())]['hunks'][he.get_hunk().get_id()]['right_touched_elements'] = {}
                self.__out__['files'][str(file.get_name())]['hunks'][he.get_hunk().get_id()]['right_touched_elements'].update({e.get_id(): {"identifier": e.get_type(), "declaration": e.get_declaration(), "start": e.get_start_position(), "end": e.get_end_position(), "body_preview": e.get_body_preview()}})

    def write(self, file_name):
        """
        Write the buffer in a file.

        :param file_name: The name of the file to be written.
        :return: The file content.
        """
        file = open(f"../output/{file_name}.json", 'w')
        file.write(json.dumps(self.__out__))
        return json.dumps(self.__out__)

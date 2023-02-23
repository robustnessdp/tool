""" Class for external processes execution.

 __author__ = "<supressed>"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "<supressed>"
 __email__ = "<supressed>"
 __status__ = "Production"
"""
import shlex, subprocess

class Process():
    @staticmethod
    def start_process(command):
        """
        Executes a command line as a new process.

        :param command: String containing the command line.
        :return: A tuple containing: the process status code, the standard output, and the standard error output.
        """
        args = shlex.split(command)
        process = subprocess.run(args, capture_output=True)

        stdout = process.stdout.decode("utf-8")
        stderr = process.stderr.decode("utf-8")
        status = process.returncode

        return status, stdout, stderr
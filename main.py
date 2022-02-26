import logging
from config import Config
import sys
from utils import Utils
from task import Task


class Initialize:
    """
    Initialize the task execution.
    """
    @staticmethod
    def start():
        """
        Initializes the project parameters and starts the project execution.
        :return: None
        """
        Utils.init_logs()
        files = Utils.get_files()
        t = Task(files)
        t.run()


if __name__ == '__main__':
    Initialize.start()
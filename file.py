import logging
import os
import sys
from config import Config


class File:
    def __init__(self, filename):
        """
        self.name = name of file
        self.fileid = file handle
        self.file_content = list of file content
        self.file_length = length of file
        :param filename: name of file
        """
        self.name = filename
        self.fileid = self.get_file()
        self.file_content = self.get_file_content()
        self.file_length = len(self.file_content)

    def get_file(self):
        """
            Opens the file and returns its handle
            :return: file object
        """
        logging.debug("def get_file(self)")
        try:
            file_path = os.path.join(Config.param["RESOURCES_DIR"], self.name)
            logging.debug(file_path)
            file = open(file_path, encoding='utf-8')
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")
        else:
            return file

    def get_file_content(self):
        """
        Returns list of file content after stripping of white spaces
        :return: list of file content
        """
        logging.debug("def get_file(self)")
        try:
            file_data = self.fileid.readlines()
            file_content = map(lambda x: str.strip(x), file_data)
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")
        else:
            return list(file_content)

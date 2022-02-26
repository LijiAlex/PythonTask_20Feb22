import logging
import os
import sys
from config import Config


class Utils:
    """
    Contains common utility methods
    """

    @staticmethod
    def init_logs():
        """
        Initializes the log file and default logging format
        :return: None
        """
        try:
            log_dir_path = os.path.join(os.getcwd(), Config.param["LOG_DIR"])
            os.makedirs(log_dir_path, exist_ok=True)
            log_file = os.path.join(log_dir_path, Config.param["LOG_FILE"])
            logging.basicConfig(filename=log_file, level=Config.param["DEBUG_LEVEL"],
                                format='%(asctime)s %(levelname)s {%(pathname)s:%(lineno)d} %(message)s')
            logging.info("\n**********New execution begins************")
            logging.debug("Log file: {}".format(log_file))
        except FileNotFoundError as e:
            print("Error: ", e)
        except Exception as e:
            print("Error: ", e)

    @staticmethod
    def get_files():
        """
        Returns the files present in the config parameter RESOURCES_DIR
        :return: list of files
        """
        logging.debug("def get_files()")
        try:
            cwd = os.getcwd()
            resource_path = os.path.join(cwd, Config.param["RESOURCES_DIR"])
            files = os.listdir(resource_path)
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")
        else:
            logging.debug("Files: {}".format(files))
            return files

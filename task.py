import logging
import sys
import os
import sqlite3
from config import Config
from file import File
from functools import reduce


class Task:
    def __init__(self, f):
        """
        self.files: list of file handles for files in Resources directory
        self.merged_file_content: list of merged words of all file

        :param f : list of filenames in the Resources directory
        """
        self.files = [File(file) for file in f]
        self.merged_file_content = self.merge()

    def merge(self):
        """Merge the contents of all files.
        :return: list of all file contents
        """
        logging.debug("def merge(self)")
        try:
            merged = []
            for file in self.files:
                merged = merged+file.file_content
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")
        else:
            return merged

    def mergeFileContents(self):
        """Creates a merged list of file contents.
        Index 0 will have contents of file1 etc
        :return: list of list of file contents
        """
        logging.debug("def mergeFileContents(self)")
        try:
            merged = []
            for file in self.files:
                merged.append(file.file_content)
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")
        else:
            return merged

    def task1(self):
        """Reads each files in the resource folder and returns
        a list of tuples with word and its respective count.
        The output is captured in "task1_output.txt"
        """
        logging.debug("Executing task1()")
        try:
            count = {}
            for elem in self.merged_file_content :
                if elem in count:
                    count[elem] = count[elem]+1
                else:
                    count[elem] = 1
            output_file = "{}\\task1_output.txt".format(Config.param["OUTPUT_DIR"])
            f = open(output_file, 'w', encoding='utf-8')
            for elem in count:
                f.write("{}:{}\n".format(elem, count[elem]))
            f.close()
            logging.info("Output written to task1_output.txt")
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")

    def task2(self):
        """Reads each files in the resource folder and returns
        a list of tuples with an alphabet and no of words starting with that alphabet.
        """
        logging.debug("Executing task2()")
        try:
            count = {alpha:1 for alpha in 'abcdefghijklmnopqrstuvwxyz'}
            for elem in self.merged_file_content:
                if elem[0] in count:
                    count[elem[0]] = count[elem[0]]+1
            output_file = "{}\\task2_output.txt".format(Config.param["OUTPUT_DIR"])
            f = open(output_file, 'w', encoding='utf-8')
            for elem in count:
                f.write("{}:{}\n".format(elem, count[elem]))
            f.close()
            logging.info("Output written to task2_output.txt")
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")

    def task3(self):
        """Reads each files in the resource folder and returns
        only the alphabet part in the words.
        """
        logging.debug("Executing task3()")
        try:
            output_file = "{}\\task3_output.txt".format(Config.param["OUTPUT_DIR"])
            f = open(output_file, 'w', encoding='utf-8')
            for word in self.merged_file_content :
                newword = ""
                for ch in word:
                    if ch.isalpha():
                        newword += ch
                f.write(newword+"\n")
            f.close()
            logging.info("Output written to task3_output.txt")
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")

    def task4(self):
        """Create a list of tuples of all the words in all the files with each tuple having
        words present at the same index location.
        """
        logging.debug("Executing task4()")
        try:
            output_file = "{}\\task4_output.db".format(Config.param["OUTPUT_DIR"])
            db = sqlite3.connect(output_file)
            c = db.cursor()
            logging.debug("Connection established to database")
            #c.execute("drop table zipped")
            c.execute('create table if not exists zipped(table1 text, table2 text, table3 text, table4 text, table5 text)')
            c.execute("delete from zipped")
            logging.debug("Table zipped if not exists created")
            merged_list = self.mergeFileContents()
            output = zip(*merged_list)
            logging.debug("Contents zipped")
            for element in output:
                try:
                    col1, col2, col3, col4, col5 = element
                    c.execute("""insert into zipped values("{}","{}","{}","{}","{}")""".format(col1, col2, col3, col4, col5))
                except Exception as e:
                    logging.error("Error: {}".format(e))
                    continue
            db.commit()
            #data = c.execute("select * from zipped")
            #for i in data:
                #print(i)
            db.close()
            logging.info("Output written to task4_output.db")
        except Exception as e:
            logging.error("Error: {}".format(e))
            sys.exit("Execution truncated. Check log for details.")


    def run(self):
        os.makedirs(Config.param["OUTPUT_DIR"], exist_ok=True)
        self.task1()
        self.task2()
        self.task3()
        self.task4()

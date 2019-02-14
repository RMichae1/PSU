from os.path import join
import numpy as np


class Reader:
    def __init__(self, directory=None, order_name="order11.txt", problem="problem1.txt"):
        if directory:
            self.directory = directory
        else:
            self.directory = "./"
        # numpy makes later calculations more efficient
        self.order = np.array(self.read_input(order_name))
        self.space = np.array(self.read_input(problem))

    def read_input(self, filename):
        readfile = join(self.directory, filename)
        with open(readfile) as in_file:
            file_content = in_file.readline()
            # convert read input into useful filestructure
            file_list = file_content.split()
            return file_list

    def get_order(self):
        return self.order

    def get_space(self):
        return self.space

    def __str__(self):
        return self.order, self.space

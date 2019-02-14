import sys
from Reader import Reader
from PySide2 import QtCore, QtWidgets, QtGui
from SearchAlgorithms import HillClimbing, FCHillClimbing, RandomHillClimbing, SimulatedAnnealing, LocalBeamSearch


class Frontend(QtWidgets.QWidget):
    def __init__(self, algorithm_list):
        super().__init__()
        self.algorithm_list = algorithm_list
        self.algorithm_names = [str(alg) for alg in self.algorithm_list]
        self.start_button = QtWidgets.QPushButton("Run Algorithm")
        self.text = QtWidgets.QLabel("GROUP ALPHA")

        # make a dropdown for the algorithms
        self.selectionBox = QtWidgets.QComboBox()
        self.selectionBox.addItems(self.algorithm_names)
        #self.selectionBox.curr

        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.selectionBox)
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)
        #self.start_button.clicked.connect(self.run_search(self.selectionBox.))

    def run_search(self):
        pass


if __name__ == "__main__":
    # read input files and extract order and problem-space
    reader = Reader()
    orders = reader.get_order()
    problem_space = reader.get_space()

    hill_climber = HillClimbing(problem_space)
    fc_climber = FCHillClimbing(problem_space)
    random_climber = RandomHillClimbing(problem_space)
    annealer = SimulatedAnnealing(problem_space)
    beam_searcher = LocalBeamSearch(problem_space)

    algs = [hill_climber, fc_climber, random_climber, annealer, beam_searcher]

    app = QtWidgets.QApplication([])
    gui = Frontend(algs)
    gui.resize(800, 600)
    gui.show()
    sys.exit(app.exec_())
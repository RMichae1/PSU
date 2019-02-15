import sys
from Reader import Reader
from PySide2 import QtCore, QtWidgets, QtGui
from SearchAlgorithms import HillClimbing, FCHillClimbing, RandomHillClimbing, SimulatedAnnealing, LocalBeamSearch


class Frontend(QtWidgets.QWidget):
    def __init__(self, algorithm_list, orders, problems):
        super().__init__()
        self.algorithm_list = algorithm_list
        self.orders = orders
        self.problems = problems
        self.algorithm_names = [str(alg) for alg in self.algorithm_list]

        self.start_button = QtWidgets.QPushButton("Run Algorithm")
        self.text = QtWidgets.QLabel("GROUP ALPHA")

        # make all dropdowns for, algorithms, orders and problemspace
        self.algorithmSelectionBox = QtWidgets.QComboBox()
        self.orderSelectionBox = QtWidgets.QComboBox()
        self.problemSelectionBox = QtWidgets.QComboBox()

        self.algorithmSelectionBox.addItems(self.algorithm_names)
        self.orderSelectionBox.addItems(self.orders)
        self.problemSelectionBox.addItems(self.problems)

        self.text.setAlignment(QtCore.Qt.AlignCenter)

        # make console like output
        #self.textOut = QTextEdit(   )

        self.layout = QtWidgets.QVBoxLayout()
        self.add_widgets()
        self.setLayout(self.layout)

        active_algorithm_id = self.algorithmSelectionBox.currentIndex()
        self.start_button.clicked.connect(self.run_search(active_algorithm_id))

    def add_widgets(self):
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.problemSelectionBox)
        self.layout.addWidget(self.orderSelectionBox)
        self.layout.addWidget(self.algorithmSelectionBox)
        self.layout.addWidget(self.start_button)

    def run_search(self, algorithm_id):
        print(self.algorithm_list[algorithm_id].search())


if __name__ == "__main__":
    # read input files and extract order and problem-space
    reader = Reader()
    order_list = reader.get_files_like("order")
    problem_list = reader.get_files_like("problem")
    orders = reader.get_order()
    problem_space = reader.get_space()

    hill_climber = HillClimbing(problem_space)
    fc_climber = FCHillClimbing(problem_space)
    random_climber = RandomHillClimbing(problem_space)
    annealer = SimulatedAnnealing(problem_space)
    beam_searcher = LocalBeamSearch(problem_space)

    algs = [hill_climber, fc_climber, random_climber, annealer, beam_searcher]

    app = QtWidgets.QApplication([])
    gui = Frontend(algorithm_list=algs,
                   orders=order_list,
                   problems=problem_list)
    gui.resize(800, 600)
    gui.show()
    sys.exit(app.exec_())
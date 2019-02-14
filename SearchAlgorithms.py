import random
import numpy as np


class SearchAlg:
    def __init__(self, problem_space):
        self.problem_space = problem_space

    def search(self):
        return "SEARCHING"


class HillClimbing(SearchAlg):
    def __init__(self, problem_space):
        super().__init__(problem_space)

    def search(self):
        return super(HillClimbing, self).search()

    def __str__(self):
        return "Hill Climbing"


class FCHillClimbing(SearchAlg):
    def __init__(self, problem_space):
        super().__init__(problem_space)

    def search(self):
        return super(FCHillClimbing, self).search()

    def __str__(self):
        return "First Choice Hill Climbing"


class RandomHillClimbing(SearchAlg):
    def __init__(self, problem_space):
        super().__init__(problem_space)

    def search(self):
        return super(RandomHillClimbing, self).search()

    def __str__(self):
        return "Random Hill Climbing"


class SimulatedAnnealing(SearchAlg):
    def __init__(self, problem_space):
        super().__init__(problem_space)

    def search(self):
        return super(SimulatedAnnealing, self).search()

    def __str__(self):
        return "Simulated Annealing"


class LocalBeamSearch(SearchAlg):
    def __init__(self, problem_space, states=1):
        super().__init__(problem_space)
        self.states = states

    def search(self):
        return super(LocalBeamSearch, self).search()

    def __str__(self):
        return "Local Beam Search"

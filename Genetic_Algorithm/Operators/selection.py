import copy

import numpy as np
from abc import ABC, abstractmethod

from Genetic_Algorithm.population import Population


class SelStrategy(ABC):

    @abstractmethod
    def compute(self, population: Population) -> list:
        pass


class SelectionContext:

    def __init__(self, strategy: SelStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> SelStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SelStrategy):
        self._strategy = strategy

    def execute(self, population: Population) -> list:
        return self._strategy.compute(population)


class Tournament(SelStrategy):

    def __init__(self, n: int, rate=.2) -> None:
        self._rate = rate
        self._n = n

    def compute(self, population: Population) -> list:
        selection = []
        pop = copy.deepcopy(population)
        while len(selection) < population.size * self._rate:
            candidates = pop.n_random_genomes(self._n)
            candidates.sort(key=lambda g: g.fitness)
            selection.append(candidates[-1])
            pop.genomes.remove(candidates[-1])
        return selection


class RouletteWheel(SelStrategy):

    def __init__(self, rate=.2) -> None:
        self._rate = rate

    def compute(self, population: Population) -> list:
        selection = set()
        probabilities = [g.fitness / population.total_fitness() for g in population.genomes]
        while len(selection) < population.size * self._rate:
            genome = np.random.choice(population.genomes, p=probabilities)
            selection.add(genome)
        return list(selection)


class RankBased(SelStrategy):

    def __init__(self, rate=.2) -> None:
        self._rate = rate

    def compute(self, population: Population) -> list:
        selection = set()
        while len(selection) < population.size * self._rate:
            probabilities = [(idx + 1) // population.size for idx, _ in enumerate(population.genomes)]
            selection.add(np.random.choice(population.genomes, p=probabilities))
        return list(selection)

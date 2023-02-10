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

    def __init__(self, rate: int, n: int) -> None:
        self._rate = rate
        self._n = n

    def compute(self, population: Population) -> list:
        selection = []
        while len(selection) < population.size * self._rate:
            candidates = population.n_random_genomes(self._n)
            candidates.sort(key=lambda g: g.fitness)
            selection.append(candidates[-1])
        return selection


class RouletteWheel(SelStrategy):

    def __init__(self, rate) -> None:
        self._rate = rate

    def compute(self, population: Population) -> list:
        selection = []
        probabilities = [g.fitness / population.total_fitness() for g in population.genomes]
        while len(selection) < population.size * self._rate:
            selection.append(np.random.choice(population.genomes, p=probabilities))
        return selection


class RankBased(SelStrategy):

    def __init__(self, rate: int) -> None:
        self._rate = rate

    def compute(self, population: Population) -> list:
        selection = []
        probabilities = [(idx + 1) / population.size for idx, _ in enumerate(population.genomes)]
        while len(selection) < population.size * self._rate:
            selection.append(np.random.choice(population.genomes, p=probabilities))
        return selection

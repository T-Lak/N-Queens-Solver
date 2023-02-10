from Genetic_Algorithm.Operators.crossover import SinglePoint, CrossoverContext
from Genetic_Algorithm.Operators.mutation import SwapNeighbor, MutationContext
from Genetic_Algorithm.Operators.selection import Tournament, SelectionContext
from Genetic_Algorithm.population import Population


class GeneticAlgorithm:

    def __init__(self, pop_size: int, chrom_size: int):
        self._population    = Population(pop_size)
        self._sel_context   = SelectionContext(Tournament(20, 0.2))
        self._x_context     = CrossoverContext(SinglePoint(chrom_size))
        self._mut_context   = MutationContext(SwapNeighbor(0.05, chrom_size))
        self._ideal_fitness = chrom_size * (chrom_size - 1) // 2
        self._population.populate(chrom_size)

    def run(self):
        while not self._solution_found():
            parents = self._sel_context.execute(self._population)
            offset  = self._x_context.execute(parents, 20)
            offset  = self._mut_context.execute(offset)

    def _solution_found(self) -> bool:
        return self.population.fittest().fitness == self._ideal_fitness

    @property
    def population(self) -> Population:
        return self._population

    @property
    def selection_context(self):
        return self._sel_context

    @property
    def crossover_context(self):
        return self._x_context

    @property
    def mutation_context(self):
        return self._mut_context

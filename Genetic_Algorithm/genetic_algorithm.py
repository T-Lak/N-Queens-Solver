import copy

from Genetic_Algorithm.Operators.crossover import *
from Genetic_Algorithm.Operators.mutation import *
from Genetic_Algorithm.Operators.selection import *
from Genetic_Algorithm.genome import Genome
from Genetic_Algorithm.population import Population
from Utilities.board_utils import to_binary_string, display
from Utilities.ga_utils import derive_solutions_from
from Utilities.lookup_tables import ALL_SOLUTIONS_LUT


class GeneticAlgorithm:

    def __init__(self, pop_size: int, chrom_size: int):
        self._population    = Population(pop_size)
        self._history       = [copy.deepcopy(self.population)]
        self._sel_context   = SelectionContext(Tournament(15, .27))
        self._x_context     = CrossoverContext(TwoPoint(chrom_size, .67))
        self._mut_context   = MutationContext(Greedy(.9, chrom_size))
        self._ideal_fitness = chrom_size * (chrom_size - 1) // 2
        self._chrom_size    = chrom_size
        self._pop_size      = pop_size
        self._solutions     = set()
        self._population.populate(chrom_size)

    def run(self):
        while len(self._solutions) < ALL_SOLUTIONS_LUT[self._chrom_size]:
            parents = self._sel_context.execute(self._population)
            offset  = self._x_context.execute(parents, self._pop_size)
            offset  = SwapRandom(0.17, self._chrom_size).compute(offset)
            offset  = self._mut_context.execute(offset)
            genomes = []
            for chromosome in offset:
                genome = Genome(chromosome, self._chrom_size)
                genomes.append(genome)
                if genome.fitness == self._ideal_fitness and genome.chromosome not in self._solutions:
                    self._solutions.update(derive_solutions_from(chromosome, self._chrom_size))
            self._population.genomes = genomes
            self._history.append(copy.deepcopy(self._population))
            print(len(self._solutions))
        [display(to_binary_string(bb, self._chrom_size)) for bb in self._solutions]

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

import bisect
import copy

from Genetic_Algorithm.Operators.crossover import *
from Genetic_Algorithm.Operators.min_conflicts import MinConflicts
from Genetic_Algorithm.Operators.mutation import *
from Genetic_Algorithm.Operators.selection import *
from Genetic_Algorithm.genome import Genome
from Genetic_Algorithm.population import Population
from Utilities.ga_utils import derive_solutions_from
from Utilities.lookup_tables import ALL_SOLUTIONS_LUT


class GeneticAlgorithm:

    def __init__(self, pop_size: int, chrom_size: int):
        self._population    = Population(pop_size)
        self._population.populate(chrom_size)
        self._history       = [copy.deepcopy(self.population)]
        self._sel_context   = SelectionContext(RouletteWheel(.2))
        self._x_context     = CrossoverContext(SinglePoint(chrom_size, .75))
        self._mut_context   = MutationContext(SwapRandom(.01, chrom_size))
        self._min_conflicts = MinConflicts(.5, chrom_size, chrom_size)
        self._ideal_fitness = chrom_size * (chrom_size - 1) // 2
        self._chrom_size    = chrom_size
        self._pop_size      = pop_size
        self._unique_sols   = 0
        self._generations   = 1
        self._stagnation_count = 0
        self._stagnation_limit = 250
        self._stopping_cause = ""
        self._cur_num_sols = 0
        self._new_sol_found = False
        self._solutions     = set()

    def run(self):
        while len(self._solutions) != ALL_SOLUTIONS_LUT[self._chrom_size] and not self._is_converged():
            parents    = self._sel_context.execute(self._population)
            offspring  = self._x_context.execute(parents, self._pop_size)
            offspring  = self._mut_context.execute(offspring)
            offspring  = self._min_conflicts.execute(offspring)
            genomes = []
            for chromosome in offspring:
                genome = Genome(chromosome, self._chrom_size)
                bisect.insort(genomes, genome)
                if genome.fitness == self._ideal_fitness and genome.chromosome not in self._solutions:
                    self._solutions.update(derive_solutions_from(chromosome, self._chrom_size))
                    self._unique_sols += 1

            [bisect.insort(genomes, g) for g in parents[:self._pop_size - len(genomes)]]

            self._population.genomes = genomes
            self._generations += 1
            self._history.append(copy.deepcopy(self._population))
            print(len(self._solutions))

            if self._cur_num_sols != len(self._solutions):
                self._cur_num_sols = len(self._solutions)
                self._new_sol_found = True
            else:
                self._new_sol_found = False

    def _solution_found(self) -> bool:
        if self._population.fittest().fitness == self._ideal_fitness:
            self._stopping_cause = "optimum found"
            return True
        return False

    def _is_converged(self):
        if len(self._history) < 3:
            return False
        if not self._new_sol_found:
            self._stagnation_count += 1
            if self._stagnation_count == self._stagnation_limit:
                self._stopping_cause = "converged"
                return True
        else:
            self._stagnation_count = 0
        return False

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

    @property
    def min_conflicts(self):
        return self._min_conflicts

    @min_conflicts.setter
    def min_conflicts(self, value):
        self._min_conflicts = value

    @property
    def stagnation_limit(self):
        return self._stagnation_limit

    @property
    def stagnation_count(self):
        return self._stagnation_count

    @property
    def generations(self):
        return self._generations

    @property
    def stopping_cause(self):
        return self._stopping_cause

    @property
    def history(self):
        return self._history

    @property
    def unique_sols(self):
        return self._unique_sols

    @property
    def solutions(self):
        return self._solutions

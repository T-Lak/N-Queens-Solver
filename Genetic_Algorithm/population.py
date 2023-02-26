import random
import bisect

from Genetic_Algorithm.genome import Genome
from Utilities.bit_masks import BIT, ZERO
from Utilities.lookup_tables import FILE_SQUARE_LUT


class Population:

    def __init__(self, size, genomes=None):
        self._genomes = [] if genomes is None else genomes
        self._size = size

    def populate(self, chrom_size: int) -> None:
        for _ in range(self.size):
            bitboard = ZERO
            for i in range(chrom_size):
                squares   = FILE_SQUARE_LUT.get(i)
                square    = random.choice(squares)
                bitboard |= BIT << square
            self.genomes.append(Genome(bitboard, chrom_size))
        self._order()

    def _order(self):
        self._genomes.sort(key=lambda g: g.fitness)

    def contains_sub_optimal_solution(self) -> bool:
        return True if next(
            (genome.fitness for genome in self._genomes if genome.fitness == genome.ideal_fitness - 1), None
        ) else False

    def contains_optimal_solution(self) -> bool:
        return True if next(
            (genome.fitness for genome in self._genomes if genome.fitness == genome.ideal_fitness), None
        ) else False

    @property
    def genomes(self) -> list:
        return self._genomes

    @genomes.setter
    def genomes(self, value: list) -> None:
        self._genomes = value
        if len(self._genomes) < self._size:
            [bisect.insort(self._genomes, g) for g in self.n_random_genomes(self._size - len(self._genomes))]

    @property
    def size(self) -> int:
        return self._size

    def fittest(self) -> Genome:
        return self._genomes[-1]

    def n_fittest(self, n: int) -> list:
        return self._genomes[-n:]

    def worst(self) -> Genome:
        return self._genomes[0]

    def total_fitness(self) -> int:
        return sum(genome.fitness for genome in self.genomes)

    def random_genome(self) -> Genome:
        return random.choice(self._genomes)

    def n_random_genomes(self, n: int) -> list:
        return random.sample(self._genomes, n)

    def replace(self, old: Genome, new: Genome):
        self._genomes.remove(old)
        bisect.insort(self._genomes, new)


import random
import bisect

from Genetic_Algorithm.genome import Genome
from Utilities.lookup_tables import FILE_SQUARE_LUT


class Population:

    def __init__(self, size, genome_size):
        self.genomes = []
        self.size = size
        self.populate(genome_size)
        self.genomes.sort(key=lambda g: g.fitness)

    def populate(self, genome_size: int) -> None:
        for _ in range(self.size):
            bitboard = 0x0
            for i in range(genome_size):
                squares = FILE_SQUARE_LUT.get(i)
                square = random.choice(squares)
                bitboard |= 0x1 << square
            self.genomes.append(Genome(bitboard, genome_size))

    def get_genomes(self) -> list:
        return self.genomes

    def fittest(self) -> Genome:
        return self.genomes[-1]

    def n_fittest(self, n: int) -> list:
        return self.genomes[-n:]

    def worst(self) -> Genome:
        return self.genomes[0]

    def random_genome(self) -> Genome:
        return random.choice(self.genomes)

    def n_random_genomes(self, n: int) -> list:
        return random.sample(self.genomes, n)

    def replace(self, old: Genome, new: Genome):
        self.genomes.remove(old)
        bisect.insort(self.genomes, new)

    def size(self) -> int:
        return self.size

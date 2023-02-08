import random

from Genetic_Algorithm.genome import Genome
from Utilities.lookup_tables import FILE_SQUARE_LUT


class Population:

    def __init__(self, size):
        self.genomes = []
        self.size = size

    def populate(self, genome_size):
        for _ in range(self.size):
            bitboard = 0x0
            for i in range(genome_size):
                squares = FILE_SQUARE_LUT.get(i)
                square = random.choice(squares)
                bitboard |= 0x1 << square
            self.genomes.append(Genome(bitboard, genome_size))

    @property
    def genomes(self):
        return self._genomes

    @genomes.setter
    def genomes(self, genomes):
        self._genomes = genomes


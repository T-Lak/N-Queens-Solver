from Utilities.board_utils import to_binary_string, display, count_bits_set
from Utilities.lookup_tables import ATTACK_LUT, bit_length


class Genome:

    def __init__(self, chromosome, size):
        self.chromosome = chromosome
        self.size = size
        self.fitness = size * (size - 1) // 2
        self.eval_fitness()

    def __repr__(self) -> str:
        return 'Genome(chromosome: {} - fitness: {})'.format(to_binary_string(self.chromosome, self.size), self.fitness)

    def __lt__(self, other) -> bool:
        return self.fitness < other.fitness

    def eval_fitness(self):
        attacks = 0
        squares = bit_length(self.chromosome)
        for square in squares:
            attack_bb = ATTACK_LUT[square]
            attacks  += count_bits_set(attack_bb & self.chromosome)
        self.fitness -= attacks // 2

    def fitness(self):
        return self.fitness

    @property
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome(self, value):
        self._chromosome = value

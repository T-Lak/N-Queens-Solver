from Utilities.board_utils import to_binary_string, display, count_bits_set
from Utilities.lookup_tables import ATTACK_LUT


class Genome:

    def __init__(self, chromosome, size):
        self.chromosome = chromosome
        self.size = size
        self.fitness = size * (size - 1) // 2
        self.eval_fitness()

    def eval_fitness(self):
        chromosome = self.chromosome
        attacks = 0
        bit_idx = 0
        while chromosome:
            if chromosome & 1:
                attack_bb = ATTACK_LUT[bit_idx]
                attacks += count_bits_set(attack_bb & self.chromosome)
            chromosome >>= 1
            bit_idx += 1
        self.fitness -= attacks // 2
        print(self.fitness)
        if self.fitness >= 24:
            display(to_binary_string(self.chromosome, self.size))

    def get_fitness(self):
        return self.fitness

    @property
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome(self, value):
        self._chromosome = value

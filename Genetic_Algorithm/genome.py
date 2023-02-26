from Utilities.bit_masks import BIT
from Utilities.lookup_tables import ATTACK_LUT


class Genome:

    def __init__(self, chromosome, chrom_size):
        self._chromosome = chromosome
        self._size = chrom_size
        self._fitness = 0
        self._ideal_fitness = chrom_size * (chrom_size - 1) // 2
        self.eval_fitness()

    def __repr__(self) -> str:
        return 'Genome(chromosome: {} | fitness: {})'\
            .format(hex(self._chromosome), self._fitness)

    def __lt__(self, other) -> bool:
        return self._fitness < other.fitness

    @property
    def fitness(self) -> int:
        return self._fitness

    @property
    def ideal_fitness(self):
        return self._ideal_fitness

    @property
    def size(self) -> int:
        return self._size

    @property
    def chromosome(self) -> int:
        return self._chromosome

    @chromosome.setter
    def chromosome(self, value) -> None:
        self._chromosome = value

    def eval_fitness(self) -> None:
        temp_bb = self._chromosome
        attacks, bit_idx = 0, 0
        while temp_bb:
            if temp_bb & BIT:
                attack_bb = ATTACK_LUT[bit_idx]
                attacks  += bin(attack_bb & self._chromosome).count("1")
            temp_bb >>= BIT
            bit_idx  += BIT
        self._fitness = self._ideal_fitness - attacks // 2

import random
from abc import ABC, abstractmethod

from Utilities.bit_masks import BIT
from Utilities.lookup_tables import FILE_MASK_LUT


class MutStrategy(ABC):

    def __init__(self, rate, genome_size) -> None:
        self._rate = rate
        self._genome_size = genome_size

    @abstractmethod
    def compute(self, offset: list) -> list:
        pass

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


class MutationContext:

    def __init__(self, strategy: MutStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> MutStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def execute(self, offset: list) -> list:
        return self._strategy.compute(offset)


class SwapNeighbor(MutStrategy):

    def __init__(self, rate, genome_size) -> None:
        super().__init__(rate, genome_size)

    def compute(self, offset: list) -> list:
        for _ in range(int(len(offset) * self._rate)):
            chromosome  = offset.pop()
            file_idx_1  = random.randint(0, self._genome_size - 2)
            file_idx_2  = file_idx_1 + 1
            gene_1      = chromosome & FILE_MASK_LUT[file_idx_1]
            gene_2      = chromosome & FILE_MASK_LUT[file_idx_2]
            chromosome ^= gene_1 | gene_2
            chromosome |= gene_1 << BIT | gene_2 >> BIT
            offset.insert(0, chromosome)
        return offset


class SwapRandom(MutStrategy):

    def __init__(self, rate, genome_size) -> None:
        super().__init__(rate, genome_size)

    def compute(self, offset: list) -> list:
        for _ in range(int(len(offset) * self._rate)):
            chromosome  = offset.pop()
            file_idx_1  = random.randint(0, self._genome_size // 2)
            file_idx_2  = random.randint(self._genome_size // 2 + 1, self._genome_size - 1)
            bit_shift   = abs(file_idx_2 - file_idx_1)
            gene_1      = chromosome & FILE_MASK_LUT[file_idx_1]
            gene_2      = chromosome & FILE_MASK_LUT[file_idx_2]
            chromosome ^= gene_1 | gene_2
            chromosome |= gene_1 << bit_shift | gene_2 >> bit_shift
            offset.insert(0, chromosome)
        return offset

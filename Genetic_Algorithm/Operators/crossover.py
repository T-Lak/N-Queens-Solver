import copy
import random
from abc import ABC, abstractmethod

from Utilities.bit_masks import masked_west_files, invert, ZERO
from Utilities.lookup_tables import FILE_MASK_LUT


class XStrategy(ABC):

    def __init__(self, chrom_size, rate=.8) -> None:
        self._chrom_size = chrom_size
        self._rate = rate

    @abstractmethod
    def compute(self, parents: list, breed_limit: int) -> list:
        pass

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


class CrossoverContext:

    def __init__(self, strategy: XStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> XStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: XStrategy):
        self._strategy = strategy

    def execute(self, parents: list, breed_limit: int) -> list:
        return self._strategy.compute(parents, breed_limit)


class SinglePoint(XStrategy):

    def __init__(self, chrom_size, rate=.8) -> None:
        super().__init__(chrom_size, rate)

    def compute(self, parents: list, breed_limit: int) -> list:
        p = [g.chromosome for g in parents]
        offspring = []
        while len(offspring) < int(breed_limit * self._rate):
            x_point = random.randint(1, self._chrom_size)
            left_mask = masked_west_files(x_point, self._chrom_size)
            right_mask = invert(left_mask, self._chrom_size)
            parent_1, parent_2 = random.sample(p, 2)
            child_1 = (parent_1 & left_mask) | (parent_2 & right_mask)
            child_2 = (parent_2 & left_mask) | (parent_1 & right_mask)
            offspring += [child_1, child_2]
        return offspring


class TwoPoint(XStrategy):

    def __init__(self, chrom_size, rate=.8) -> None:
        super().__init__(chrom_size, rate)

    def compute(self, parents: list, breed_limit: int) -> list:
        p = [g.chromosome for g in parents]
        offspring = []
        while len(offspring) < int(breed_limit * self._rate):
            child_1,  child_2  = ZERO, ZERO
            parent_1, parent_2 = random.sample(p, 2)
            start = random.randint(1, self._chrom_size // 2)
            end   = random.randint(start + 1, self._chrom_size - 1)
            for file in range(self._chrom_size):
                file_mask = FILE_MASK_LUT[file]
                if file < start or file > end:
                    child_1 |= parent_1 & file_mask
                    child_2 |= parent_2 & file_mask
                else:
                    child_1 |= parent_2 & file_mask
                    child_2 |= parent_1 & file_mask
            offspring.extend([child_1, child_2])
        return offspring


class Uniform(XStrategy):

    def __init__(self, chrom_size, rate=.8) -> None:
        super().__init__(chrom_size, rate)

    def compute(self, parents: list, breed_limit: int) -> list:
        offspring = []
        while len(offspring) < int(breed_limit * self._rate):
            child_1,  child_2  = ZERO, ZERO
            parent_1, parent_2 = random.sample(parents, 2)
            for file in range(self._chrom_size):
                toss = random.randint(0, 1)
                file_mask = FILE_MASK_LUT[file]
                if toss == 1:
                    child_1 |= parent_2.chromosome & file_mask
                    child_2 |= parent_1.chromosome & file_mask
                else:
                    child_1 |= parent_1.chromosome & file_mask
                    child_2 |= parent_2.chromosome & file_mask
            offspring.extend([child_1, child_2])
        return offspring


class Shuffle(XStrategy):

    def __init__(self, chrom_size, rate=.8) -> None:
        super().__init__(chrom_size, rate)

    def compute(self, parents: list, breed_limit: int) -> list:
        offset = []
        p = [g.chromosome for g in parents]
        while len(offset) < 100 * self._rate:
            parent = random.choice(p)
            files = [parent & FILE_MASK_LUT[i] for i in range(self._chrom_size)]
            random.shuffle(files)
            child = ZERO
            for _, file in enumerate(files):
                child |= file
            offset.append(child)
        return offset

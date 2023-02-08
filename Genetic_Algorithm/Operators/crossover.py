import random
from abc import ABC, abstractmethod

from Utilities.bit_masks import masked_west_files, invert
from Utilities.lookup_tables import FILE_MASK_LUT


class XStrategy(ABC):

    @abstractmethod
    def compute(self, parents: list, breed_limit: int):
        pass


class CrossoverContext:

    def __init__(self, strategy: XStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> XStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: XStrategy):
        self._strategy = strategy

    def execute(self, parents: list, breed_limit: int):
        self._strategy.compute(parents, breed_limit)


class SinglePoint(XStrategy):

    def __init__(self, n) -> None:
        self._n = n

    def compute(self, parents: list, breed_limit: int):
        children = []
        while len(children) < breed_limit:
            x_point = random.randint(1, self._n)
            left_mask, right_mask = self._create_masks(x_point)
            parent_1, parent_2 = random.sample(parents, 2)
            child_1 = (parent_1 & left_mask) | (parent_2 & right_mask)
            child_2 = (parent_2 & left_mask) | (parent_1 & right_mask)
            children.extend([child_1, child_2])

    def _create_masks(self, x_point: int) -> tuple:
        left_mask  = masked_west_files(x_point, self._n)
        right_mask = invert(left_mask, self._n)
        return left_mask, right_mask


class TwoPoint(XStrategy):

    def __init__(self, n) -> None:
        self._n = n

    def compute(self, parents: list, breed_limit: int):
        children = []
        while len(children) < breed_limit:
            child_1,  child_2  = 0x0, 0x0
            parent_1, parent_2 = random.sample(parents, 2)
            x_point_1 = random.randint(1, self._n // 2)
            x_point_2 = random.randint(x_point_1, self._n - 1)
            for file in range(self._n):
                file_mask = FILE_MASK_LUT[file]
                if file < x_point_1 or file > x_point_2:
                    child_1 |= parent_1 & file_mask
                    child_2 |= parent_2 & file_mask
                else:
                    child_1 |= parent_2 & file_mask
                    child_2 |= parent_1 & file_mask
                children.extend([child_1, child_2])


class Uniform(XStrategy):

    def __init__(self, n) -> None:
        self._n = n

    def compute(self, parents: list, breed_limit: int):
        children = []
        while len(children) < breed_limit:
            child_1,  child_2  = 0x0, 0x0
            parent_1, parent_2 = random.sample(parents, 2)
            for file in range(self._n):
                toss = random.randint(0, 1)
                file_mask = FILE_MASK_LUT[file]
                if toss == 1:
                    child_1 |= parent_2 & file_mask
                    child_2 |= parent_1 & file_mask
                else:
                    child_1 |= parent_1 & file_mask
                    child_2 |= parent_2 & file_mask
            children.extend([child_1, child_2])

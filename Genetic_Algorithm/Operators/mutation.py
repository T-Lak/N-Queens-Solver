import random
from abc import ABC, abstractmethod

from Utilities.board_utils import file_idx
from Utilities.lookup_tables import ATTACK_LUT, FILE_SQUARE_LUT, CLEAR_FILE_LUT, FILE_MASK_LUT


class MutStrategy(ABC):

    @abstractmethod
    def compute(self, offset: list) -> list:
        pass


class MutationContext:

    def __init__(self, strategy: MutStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> MutStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def execute(self, offset: list):
        self._strategy.compute(offset)


class SwapNeighbor(MutStrategy):

    def __init__(self, rate, board_size) -> None:
        self._rate = rate
        self._board_size = board_size

    def compute(self, offset: list) -> list:
        for _ in range(len(offset) * self._rate):
            chromosome  = offset.pop()
            file_idx_1  = random.randint(0, self._board_size - 2)
            file_idx_2  = file_idx_1 + 1
            gene_1      = chromosome & FILE_MASK_LUT[file_idx_1]
            gene_2      = chromosome & FILE_MASK_LUT[file_idx_2]
            chromosome ^= gene_1 | gene_2
            chromosome |= gene_1 << 1 | gene_2 >> 1
            offset.append(chromosome)
        return offset


class SwapRandom(MutStrategy):

    def __init__(self, rate, board_size) -> None:
        self._rate = rate
        self._board_size = board_size

    def compute(self, offset: list) -> list:
        for _ in range(len(offset) * self._rate):
            chromosome  = offset.pop()
            file_idx_1  = random.randint(0, self._board_size // 2)
            file_idx_2  = random.randint(self._board_size // 2 + 1, self._board_size - 1)
            bit_shift   = file_idx_2 - file_idx_1
            gene_1      = chromosome & FILE_MASK_LUT[file_idx_1]
            gene_2      = chromosome & FILE_MASK_LUT[file_idx_2]
            chromosome ^= gene_1 | gene_2
            chromosome |= gene_1 << bit_shift | gene_2 >> bit_shift
            offset.append(chromosome)
        return offset


class Greedy(MutStrategy):

    def __init__(self, rate, board_size) -> None:
        self._rate = rate
        self._board_size = board_size

    def compute(self, offset: list) -> list:
        for _ in range(len(offset) * self._rate):
            chromosome  = offset.pop()
            queen_sq = self._greediest_queen(chromosome)
            sq_file, new_square = self._compute_new_position(queen_sq)
            chromosome = (chromosome & CLEAR_FILE_LUT[sq_file]) | (0x1 << new_square)
            offset.append(chromosome)
        return offset

    @staticmethod
    def _greediest_queen(bitboard: int) -> int:
        num_attacks, bit_idx, queen_sq = 0, 0, 0
        temp_bb = bitboard
        while temp_bb:
            if temp_bb & 1:
                attack_bb = ATTACK_LUT[bit_idx]
                attacks = bin(attack_bb & bitboard).count("1")
                if attacks > num_attacks:
                    num_attacks = attacks
                    queen_sq = bit_idx
            temp_bb >>= 1
            bit_idx  += 1
        return queen_sq

    def _compute_new_position(self, square: int) -> tuple:
        sq_file = file_idx(square, self._board_size)
        squares = FILE_SQUARE_LUT[sq_file]
        squares.remove(square)
        new_square = random.choice(squares)
        return sq_file, new_square

import copy
import random

from Genetic_Algorithm.genome import Genome
from Utilities.bit_masks import BIT
from Utilities.board_utils import file_idx
from Utilities.lookup_tables import CLEAR_FILE_LUT, ATTACK_LUT, FILE_SQUARE_LUT


class MinConflicts:

    def __init__(self, rate, genome_size) -> None:
        self._rate = rate
        self._genome_size = genome_size

    def execute(self, offset: list) -> list:
        for i in range(self._genome_size * (int(len(offset) * self._rate))):
            chromosome  = offset.pop()
            queen_sq = self._queen_with_most_attacks(chromosome)
            sq_file, new_square = self._compute_new_position(queen_sq)
            chromosome = (chromosome & CLEAR_FILE_LUT[sq_file]) | (BIT << new_square)
            # offset.insert(0, chromosome)
            # if i % self._genome_size == 0:
            #     offset.insert(0, chromosome)
            # else:
            offset.insert(0, chromosome)
        return offset

    @staticmethod
    def _queen_with_most_attacks(bitboard: int) -> int:
        num_attacks, bit_idx, queen_sq = 0, 0, 0
        temp_bb = bitboard
        while temp_bb:
            if temp_bb & BIT:
                attack_bb = ATTACK_LUT[bit_idx]
                attacks = bin(attack_bb & bitboard).count("1")
                if attacks > num_attacks:
                    num_attacks = attacks
                    queen_sq = bit_idx
            temp_bb >>= BIT
            bit_idx  += BIT
        return queen_sq

    def _compute_new_position(self, square: int) -> tuple:
        sq_file = file_idx(square, self._genome_size)
        squares = copy.deepcopy(FILE_SQUARE_LUT[sq_file])
        squares.remove(square)
        new_square = random.choice(squares)
        return sq_file, new_square

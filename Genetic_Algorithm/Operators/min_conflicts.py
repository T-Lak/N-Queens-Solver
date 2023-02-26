import copy
import operator
import random

from Genetic_Algorithm.chromosome import Chromosome
from Utilities.bit_masks import BIT, invert
from Utilities.board_utils import file_idx, count_bits_set, board_without_square, bitboard_repr, display
from Utilities.lookup_tables import ATTACK_LUT, FILE_SQUARE_LUT, attack_bitboard


class MinConflicts:

    def __init__(self, rate: float, num_it: int, n: int) -> None:
        self._rate = rate
        self._num_it = num_it
        self._n = n

    def execute(self, offspring: list) -> list:
        for _ in range(int(len(offspring) * self._rate)):
            chromosome = Chromosome(offspring.pop(), self._n)
            for _ in range(self._num_it):
                sequence = chromosome.sequence
                genes = chromosome.genes
                conflicting_squares = self.conflicting_squares(genes, sequence)
                if len(conflicting_squares) > 0:
                    conflicting_square  = random.choice(conflicting_squares)
                    new_bb, new_sq = self.compute_new_position(conflicting_square, sequence)
                    chromosome.update(new_bb, conflicting_square, new_sq)
                else:
                    break
            offspring.insert(0, chromosome.sequence)
        return offspring

    def compute_new_position(self, square: int, bb: int):
        file_squares = self.squares_and_attacks(square, bb)
        sq, num_attacks = min(file_squares, key=operator.itemgetter(1))
        _file_idx = file_idx(sq, self._num_it)
        return (bb & invert(BIT << square, self._n)) | (BIT << sq), sq

    @staticmethod
    def conflicting_squares(squares: list, bb: int) -> list:
        conflicting_queens = []
        for square in squares:
            attack_bb   = attack_bitboard(square, bb)
            if attack_bb != 0:
                conflicting_queens.append(square)
        return conflicting_queens

    def squares_and_attacks(self, square: int, bb: int) -> list:
        square_and_attacks = []
        _file_idx = file_idx(square, self._n)
        _file_squares = copy.deepcopy(FILE_SQUARE_LUT[_file_idx])
        _file_squares.remove(square)
        for sq in _file_squares:
            attack_bb = ATTACK_LUT[sq] & board_without_square(sq, bb)
            num_attacks = count_bits_set(attack_bb)
            square_and_attacks.append((sq, num_attacks))
        return square_and_attacks

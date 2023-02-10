import unittest

from Utilities.board_utils import rotate_90_deg_clockwise
from Utilities.lookup_tables import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.bitboard = 0x1E2222120E0A1222
        self.n = 8
        create_attack_lut(self.n)
        create_file_masks(self.n)
        create_rank_masks(self.n)
        create_file_square_lut(self.n)

    def test_vertical_mirroring(self):
        vertically_mirrored = mirror_vertically(self.bitboard, self.n)
        redo_mirroring = mirror_vertically(vertically_mirrored, self.n)
        self.assertEqual(self.bitboard, redo_mirroring)

    def test_horizontal_mirroring(self):
        horizontally_mirrored = mirror_horizontally(self.bitboard, self.n)
        redo_mirroring = mirror_horizontally(horizontally_mirrored, self.n)
        self.assertEqual(self.bitboard, redo_mirroring)

    def test_clockwise_rotation(self):
        valid_bb_90_deg  = 0x00ff888c92610000
        valid_bb_180_deg = 0x4448507048444478
        valid_bb_270_deg = 0x000086493111ff00

        bb_90_deg  = rotate_90_deg_clockwise(self.bitboard, self.n)
        bb_180_deg = rotate_90_deg_clockwise(bb_90_deg, self.n)
        bb_270_deg = rotate_90_deg_clockwise(bb_180_deg, self.n)

        self.assertEqual(valid_bb_90_deg, bb_90_deg)
        self.assertEqual(valid_bb_180_deg, bb_180_deg)
        self.assertEqual(valid_bb_270_deg, bb_270_deg)


if __name__ == '__main__':
    unittest.main()

from Utilities.board_utils import rotate_90_deg_clockwise
from Utilities.lookup_tables import mirror_vertically, mirror_horizontally


def derive_solutions_from(bitboard: int, n: int) -> set:
    solutions = {bitboard}

    solutions.update(mirrored_derivations(bitboard, n))

    bb_90_deg  = rotate_90_deg_clockwise(bitboard, n)
    solutions.update([bb_90_deg] + mirrored_derivations(bb_90_deg, n))

    bb_180_deg = rotate_90_deg_clockwise(bb_90_deg, n)
    solutions.update([bb_180_deg] + mirrored_derivations(bb_180_deg, n))

    bb_270_deg = rotate_90_deg_clockwise(bb_180_deg, n)
    solutions.update([bb_270_deg] + mirrored_derivations(bb_270_deg, n))

    return solutions


def mirrored_derivations(bitboard: int, n: int) -> list:
    bb_mv = mirror_vertically(bitboard, n)
    bb_mh = mirror_horizontally(bitboard, n)
    return [bb_mv, bb_mh]

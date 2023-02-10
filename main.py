from Utilities.board_utils import display, to_binary_string, rotate_90_deg_clockwise
from Utilities.lookup_tables import *


if __name__ == '__main__':
    bitboard = 0x0
    size = 5
    create_attack_lut(size)
    create_file_masks(size)
    create_rank_masks(size)
    create_file_square_lut(size)

    five_q_solutions = set()

    bb = 0x814081
    five_q_solutions.add(bb)
    bb_mv = mirror_vertically(bb, size)
    five_q_solutions.add(bb_mv)
    bb_mh = mirror_horizontally(bb, size)
    five_q_solutions.add(bb_mh)

    bb_90_deg = rotate_90_deg_clockwise(bb, size)
    five_q_solutions.add(bb_90_deg)
    bb_90_deg_mv = mirror_vertically(bb_90_deg, size)
    five_q_solutions.add(bb_90_deg_mv)
    bb_90_deg_mh = mirror_horizontally(bb_90_deg, size)
    five_q_solutions.add(bb_90_deg_mh)

    bb_180_deg = rotate_90_deg_clockwise(bb_90_deg, size)
    five_q_solutions.add(bb_180_deg)
    bb_180_deg_mv = mirror_vertically(bb_180_deg, size)
    five_q_solutions.add(bb_180_deg_mv)
    bb_180_deg_mh = mirror_horizontally(bb_180_deg, size)
    five_q_solutions.add(bb_180_deg_mh)

    bb_270_deg = rotate_90_deg_clockwise(bb_180_deg, size)
    five_q_solutions.add(bb_270_deg)
    bb_270_deg_mv = mirror_vertically(bb_270_deg, size)
    five_q_solutions.add(bb_270_deg_mv)
    bb_270_deg_mh = mirror_horizontally(bb_270_deg, size)
    five_q_solutions.add(bb_270_deg_mh)

    bb_2 = 0x281028
    bb_2_mv = mirror_vertically(bb_2, size)
    bb_2_mh = mirror_horizontally(bb_2, size)
    display(to_binary_string(bb_2, size))
    display(to_binary_string(bb_2_mv, size))
    display(to_binary_string(bb_2_mh, size))

    # for bb in five_q_solutions:
    #     display(to_binary_string(bb, size))

    # display(to_binary_string(bb, size))
    # display(to_binary_string(bb_mv, size))
    # display(to_binary_string(bb_mh, size))
    # display(to_binary_string(bb_90_deg, size))
    # display(to_binary_string(bb_180_deg, size))
    # display(to_binary_string(bb_270_deg, size))

    print(len(five_q_solutions))
    # gen_algo = GeneticAlgorithm(10, size)
    # print(gen_algo.population.genomes)


from Utilities.board_utils import *
from Utilities.lookup_tables import *


if __name__ == '__main__':
    size = 8
    create_attack_lut(size)
    create_file_masks(size)
    display(to_binary_string((ATTACK_LUT[0] | ATTACK_LUT[23]) & FILE_MASK_LUT[1], size))
    display(to_binary_string(ATTACK_LUT[0], size))
    display(to_binary_string(ATTACK_LUT[23], size))
    # for square in range(size**2):
    #     display(to_binary_string(size, ATTACK_LUT[square]))

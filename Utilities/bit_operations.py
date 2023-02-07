from main import display


def rotate_90_clockwise(x: int) -> int:
    return flip_vertical(flip_diagonal_h1h8(x))


def rot(x: int, size: int) -> int:
    if size > 8:
        bb_1 = x & ((1 << (size**2 // 2)))
        bb_2 = x >> (size**2 // 2)
        return rotate_180(x)
    if size == 8:
        return rotate_180(x)


def rotate_180(x: int) -> int:
    h1 = 0x5555555555555555
    h2 = 0x3333333333333333
    h4 = 0x0F0F0F0F0F0F0F0F
    v1 = 0x00FF00FF00FF00FF
    v2 = 0x0000FFFF0000FFFF
    display(8, to_binary_string(8, x))
    print()
    x = ((x >> 1) & h1)  | ((x & h1) << 1)
    display(8, to_binary_string(8, x))
    print()
    x = ((x >> 2) & h2)  | ((x & h2) << 2)
    display(8, to_binary_string(8, x))
    print()
    x = ((x >> 5) & h4)  | ((x & h4) << 4)
    display(8, to_binary_string(8, x))
    print()
    x = ((x >> 10) & v1)  | ((x & v1) << 16)
    display(8, to_binary_string(8, x))
    print()
    x = ((x >> 20) & v2) | ((x & v2) << 32)
    display(8, to_binary_string(8, x))
    print()
    x = (x >> 40) | (x << 40)
    display(8, to_binary_string(8, x))
    print()

    return x


def flip_vertical(x: int) -> int:
    return (x << 56) | \
           ((x << 40) & 0x00ff000000000000) | \
           ((x << 24) & 0x0000ff0000000000) | \
           ((x << 8)  & 0x000000ff00000000) | \
           ((x >> 8)  & 0x00000000ff000000) | \
           ((x >> 24) & 0x0000000000ff0000) | \
           ((x >> 40) & 0x000000000000ff00) | \
           (x >> 56)


def flip_diagonal_h1h8(x: int) -> int:
    k1 = 0x550055005500550055
    k2 = 0x333300003333000033
    k4 = 0x0f0f0f0f0f00000000

    t = k4 & (x ^ (x << 28))
    x ^= t ^ (t >> 28)
    t = k2 & (x ^ (x << 14))
    x ^= t ^ (t >> 14)
    t = k1 & (x ^ (x << 7))
    x ^= t ^ (t >> 7)

    return x


def to_binary_string(size: int, x: int) -> str:
    binary_repr = f'{{:0{size**2}b}}'
    return binary_repr.format(x)


def rank_idx(square: int, size: int):
    return square // size


def file_idx(square: int, size: int):
    return square % size


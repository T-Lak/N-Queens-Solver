def rotate_90_clockwise(x: int) -> int:
    return flip_vertical(flip_diagonal_h1h8(x))


def rotate_180(x: int) -> int:
    h1 = 0x5555555555555555
    h2 = 0x3333333333333333
    h4 = 0x0F0F0F0F0F0F0F0F
    v1 = 0x00FF00FF00FF00FF
    v2 = 0x0000FFFF0000FFFF

    x = ((x >> 1) & h1) | ((x & h1) << 1)
    x = ((x >> 2) & h2) | ((x & h2) << 2)
    x = ((x >> 4) & h4) | ((x & h4) << 4)
    x = ((x >> 8) & v1) | ((x & v1) << 8)
    x = ((x >> 16) & v2) | ((x & v2) << 16)
    x = (x >> 32) | (x << 32)

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
    k1 = 0x5500550055005500
    k2 = 0x3333000033330000
    k4 = 0x0f0f0f0f00000000

    t = k4 & (x ^ (x << 28))
    x ^= t ^ (t >> 28)
    t = k2 & (x ^ (x << 14))
    x ^= t ^ (t >> 14)
    t = k1 & (x ^ (x << 7))
    x ^= t ^ (t >> 7)

    return x


def to_binary_string(x: int) -> str:
    return '{:064b}'.format(x)

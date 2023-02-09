BIT  = 0x1
ZERO = 0x0


def create_north_mask(n: int) -> int:
    mask = ZERO
    for i in range(1, n):
        mask |= 2**(i * n)
    return mask


def create_south_mask(n: int) -> int:
    mask = BIT << (n * n - 1)
    for i in range(1, n - 1):
        mask |= mask >> n
    return mask >> n


def create_east_mask(n: int) -> int:
    mask = BIT
    for i in range(1, n - 1):
        mask |= mask << BIT
    return mask << 1


def create_west_mask(n: int) -> int:
    mask = BIT << (n ** 2 - n)
    for i in range(1, n - 1):
        mask |= mask << BIT
    return mask


def create_north_east_mask(n: int) -> int:
    mask = ZERO
    for i in range(1, n + 1):
        mask |= 2**(i * (n + 1))
    return mask


def create_north_west_mask(n: int) -> int:
    mask = BIT << n - 1
    for i in range(1, n):
        mask |= 2**(i * (n - 1))
    return mask << (n - 1)


def create_south_east_mask(n: int) -> int:
    mask = BIT << (n * n - n)
    for i in range(1, n - 1):
        mask |= mask >> (n - 1)
    return mask >> (n - 1)


def masked_west_files(rank_idx: int, n: int) -> int:
    if rank_idx == 0:
        return ZERO
    mask = create_north_mask(n) | 0x1
    for i in range(1, rank_idx):
        mask |= mask << BIT
    return mask


def invert(bitboard: int, n: int):
    mask = create_one_mask(n)
    return bitboard ^ mask


def create_south_west_mask(n: int) -> int:
    mask = BIT << (n * n - 1)
    for i in range(1, n - 1):
        mask |= mask >> (n + 1)
    return mask >> (n + 1)


def create_one_mask(n: int) -> int:
    mask = BIT
    for i in range(n * n - 1):
        mask |= mask << BIT
    return mask

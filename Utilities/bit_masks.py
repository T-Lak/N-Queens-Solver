def create_north_mask(x: int) -> int:
    mask = 0x0
    for i in range(1, x):
        mask |= 2**(i * x)
    return mask


def create_south_mask(x: int) -> int:
    mask = 0x1 << (x * x - 1)
    for i in range(1, x - 1):
        mask |= mask >> x
    return mask >> x


def create_east_mask(x: int) -> int:
    mask = 0x1
    for i in range(1, x - 1):
        mask |= mask << 1
    return mask << 1


def create_west_mask(x: int) -> int:
    mask = 0x1 << (x**2 - x)
    for i in range(1, x - 1):
        mask |= mask << 1
    return mask


def create_north_east_mask(x: int) -> int:
    mask = 0x0
    for i in range(1, x + 1):
        mask |= 2**(i * (x + 1))
    return mask


def create_north_west_mask(x: int) -> int:
    mask = 0x1 << x-1
    for i in range(1, x):
        mask |= 2**(i * (x - 1))
    return mask << (x - 1)


def create_south_east_mask(x: int) -> int:
    mask = 0x1 << (x * x - x)
    for i in range(1, x - 1):
        mask |= mask >> (x - 1)
    return mask >> (x - 1)


def masked_west_files(rank_idx: int, size: int) -> int:
    if rank_idx == 0:
        return 0x0
    mask = create_north_mask(size) | 0x1
    for i in range(1, rank_idx):
        mask |= mask << 1
    return mask


def create_south_west_mask(x: int) -> int:
    mask = 0x1 << (x * x - 1)
    for i in range(1, x - 1):
        mask |= mask >> (x + 1)
    return mask >> (x + 1)


def create_one_mask(x: int) -> int:
    mask = 0x1
    for i in range(x*x + 1):
        mask |= mask << 1
    return mask



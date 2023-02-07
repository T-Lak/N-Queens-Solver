





def to_binary_string(size: int, x: int) -> str:
    binary_repr = f'{{:0{size**2}b}}'
    return binary_repr.format(x)


def rank_idx(square: int, size: int):
    return square // size


def file_idx(square: int, size: int):
    return square % size


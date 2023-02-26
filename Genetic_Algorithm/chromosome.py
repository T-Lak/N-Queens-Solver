from Utilities.board_utils import bit_scan_forward


class Chromosome:

    def __init__(self, sequence: int, size: int):
        self._sequence = sequence
        self._gene_indices = bit_scan_forward(sequence)
        self._size = size

    def __and__(self, other):
        return self._sequence & other

    def __or__(self, other):
        return self._sequence | other

    def __xor__(self, other):
        return self._sequence ^ other

    @property
    def sequence(self):
        return self._sequence

    @property
    def genes(self):
        return self._gene_indices

    @property
    def size(self):
        return self._size

    def update(self, sequence: int, old_gene: int, new_gene: int) -> None:
        self._sequence = sequence
        self._gene_indices.remove(old_gene)
        self._gene_indices.append(new_gene)

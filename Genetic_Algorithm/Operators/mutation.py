from abc import ABC, abstractmethod


class MutStrategy(ABC):

    @abstractmethod
    def compute(self):
        pass


class MutationContext:

    def __init__(self, strategy: MutStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> MutStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy) -> None:
        self._strategy = strategy

    def execute(self):
        self._strategy.compute()


class SwapNeighbor(MutStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass


class SwapRandom(MutStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass


class ShuffleSequence(MutStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass

from abc import ABC, abstractmethod


class SelStrategy(ABC):

    @abstractmethod
    def compute(self):
        pass


class SelectionContext:

    def __init__(self, strategy: SelStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> SelStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SelStrategy):
        self._strategy = strategy

    def execute(self):
        self._strategy.compute()


class DeterministicTruncation(SelStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass


class Tournament(SelStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass


class RouletteWheel(SelStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass


class RankBased(SelStrategy):

    def __init__(self) -> None:
        pass

    def compute(self):
        pass

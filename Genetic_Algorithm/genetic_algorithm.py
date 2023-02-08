from Genetic_Algorithm.population import Population


class GeneticAlgorithm:

    def __init__(self, pop_size: int, genome_size: int):
        self._population = Population(pop_size, genome_size)

    @property
    def population(self) -> Population:
        return self._population

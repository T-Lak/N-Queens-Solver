from Genetic_Algorithm.population import Population


class GeneticAlgorithm:

    def __init__(self, pop_size: int, genome_size: int):
        self.pop_size = pop_size
        self.genome_size = genome_size
        self.population = Population(pop_size, genome_size)
        print(self.population.get_genomes())

    def population(self) -> Population:
        return self.population

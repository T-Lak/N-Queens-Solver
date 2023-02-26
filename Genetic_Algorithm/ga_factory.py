from Genetic_Algorithm.Operators.crossover import SinglePoint, TwoPoint
from Genetic_Algorithm.Operators.min_conflicts import MinConflicts
from Genetic_Algorithm.Operators.mutation import SwapNeighbor, SwapRandom
from Genetic_Algorithm.Operators.selection import Tournament, RouletteWheel, RankBased
from Genetic_Algorithm.genetic_algorithm import GeneticAlgorithm
from Utilities.lookup_tables import create_file_masks, create_attack_lut, create_rank_masks, create_file_square_lut


def create_ga(parameters: dict, pop_size: int, n: int) -> GeneticAlgorithm:
    create_attack_lut(n)
    create_file_masks(n)
    create_rank_masks(n)
    create_file_square_lut(n)

    ga = GeneticAlgorithm(pop_size, n)
    for operator, parameter in parameters.items():
        if operator == "TM":
            ga.selection_context.strategy = Tournament(int(parameter[0] * pop_size), float(parameter[1]))
        if operator == "RW":
            ga.selection_context.strategy = RouletteWheel(float(parameter))
        if operator == "RB":
            ga.selection_context.strategy = RankBased(float(parameter))
        if operator == "OP":
            ga.crossover_context.strategy = SinglePoint(n, float(parameter))
        if operator == "TP":
            ga.crossover_context.strategy = TwoPoint(n, float(parameter))
        if operator == "SN":
            ga.mutation_context.strategy = SwapNeighbor(float(parameter), n)
        if operator == "SR":
            ga.mutation_context.strategy = SwapRandom(float(parameter), n)
        if operator == "MC":
            ga.min_conflicts = MinConflicts(float(parameter[0]), int(parameter[1]), n)
    return ga

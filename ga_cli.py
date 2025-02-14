import argparse

from Genetic_Algorithm.ga_factory import create_ga
from Genetic_Algorithm.genetic_algorithm import GeneticAlgorithm
from Utilities.board_utils import bitboard_repr, display
from Utilities.lookup_tables import create_attack_lut, create_file_masks, create_rank_masks, create_file_square_lut


def main():
    parser = argparse.ArgumentParser(description="Solve N-Queens using a Genetic Algorithm.")
    parser.add_argument("--n", type=int, required=True, help="Size of the chessboard (N).")
    parser.add_argument("--population", type=int, required=True, help="Size of the population.")
    parser.add_argument("--generations", type=int, required=True, help="Number of generations.")

    # Optional selection, crossover, mutation params
    parser.add_argument("--TM", type=float, nargs=2, metavar=("TOURNAMENT_SIZE", "PROB"), help="Tournament selection parameters.")
    parser.add_argument("--RW", type=float, help="Roulette wheel selection probability.")
    parser.add_argument("--RB", type=float, help="Rank-based selection probability.")
    parser.add_argument("--OP", type=float, help="One-point crossover probability.")
    parser.add_argument("--TP", type=float, help="Two-point crossover probability.")
    parser.add_argument("--SN", type=float, help="Swap neighbor mutation probability.")
    parser.add_argument("--SR", type=float, help="Swap random mutation probability.")
    parser.add_argument("--MC", type=float, nargs=2, metavar=("MC_PROB", "MC_ITER"), help="Min-conflicts parameters.")

    args = parser.parse_args()

    # Convert args to dictionary for GA creation
    params = {k: v for k, v in vars(args).items() if v is not None and k not in ["n", "population", "generations"]}

    ga = create_ga(params, args.population, args.n)
    ga.run()

    for solution in ga.solutions:
        display(bitboard_repr(solution, args.n))

if __name__ == "__main__":
    main()
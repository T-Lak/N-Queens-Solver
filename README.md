## Overview
This project implements a hybrid approach combining a Genetic Algorithm (GA) with the Min-Conflicts heuristic to solve the N-Queens problem efficiently. 
The implementation is designed for performance optimization, using [bitboards](https://www.chessprogramming.org/Bitboards)
instead of arrays for representing chessboards, enabling efficient computations via bitwise operations.

## Features
- **🧬 Chromosome Representation:** Bitboards representing queens' positions.
- **🎯 Selection Methods:** Tournament Selection (TM) & Roulette-Wheel Selection (RW).
- **🔀 Crossover:** One-Point (OP) & Two-Point (TP) crossover.
- **🔄 Mutation:** Swap Random (SR) & Swap Neighbor (SN) mutations.
- **📊 Fitness Function:** Based on the number of conflicts between queens.
- **🧩 Min-Conflicts:** to guide solutions towards feasibility.
- **♟️ Bitboard Representation:** for highly efficient board state manipulation

## Methodology
The algorithm follows these steps:

1. **Chromosome Representation:** Boards are encoded using bitboards, allowing rapid conflict detection and manipulation through bitwise operations.
2. **Selection Methods:** Tournament Selection (10% pool) and Roulette-Wheel Selection (20% rate)
3. **Crossover:** One-Point and Two-Point crossover (90% probability)
4. **Mutation:** Swap-based mutation (3% probability)
5. **Min-Conflicts Application:** Applied with a probability of 10% per selected chromosome
6. **Termination Criteria:** Solution found or maximum of 250 generations reached

## Experimental Results

Three experimental phases were conducted:

- **Phase 1 - Evaluation of different GA configurations on n=8:** Results showed that Tournament Selection and Two-Point Crossover yielded the best performance. Min-Conflicts significantly improved success rates, achieving up to 100% success rate in some configurations.
- **Phase 2 - Testing the hybrid approach on larger board sizes (n=10, 20, 30, 40, 50):** The bitboard-based representation allowed the algorithm to scale efficiently, consistently finding solutions in fewer than 5 generations for all tested board sizes.
- **Phase 3 - Assessing the ability to find all possible solutions for n=8–11:** Results indicated that Roulette-Wheel Selection consistently found 100% of all possible solutions, while Tournament Selection was slightly less consistent for larger n.

## Usage
```bash
python n_queens_ga.py --n 8 --population 200 --generations 250
```

## Dependencies
- Python 3.x
- NumPy

## Future Improvements
- ⚙️ Fine-tuning Parameters - experiment with adaptive selection/mutation rates.
- 🔄 Exploring alternative selection and mutation strategies.
- 📌 Applying the approach to other combinatorial optimization problems.

---
✨ **Contributions welcome!** Feel free to fork and enhance this project.

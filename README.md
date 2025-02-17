## Overview
This project implements a hybrid approach combining a Genetic Algorithm (GA) with the Min-Conflicts heuristic to solve the [**N-Queens Problem**](https://developers.google.com/optimization/cp/queens) efficiently. 
The implementation is designed for performance optimization, using [bitboards](https://www.chessprogramming.org/Bitboards)
instead of arrays for representing chessboards, enabling efficient computations via bitwise operations.

## Features
- **🧬 Chromosome Representation:** Bitboards representing queens' positions.
- **🎯 Selection Methods:** Tournament Selection (TM) & Roulette-Wheel Selection (RW).
- **🔀 Crossover:** One-Point (OP) & Two-Point (TP) crossover.
- **🔄 Mutation:** Swap Random (SR) & Swap Neighbor (SN) mutations.
- **📊 Fitness Function:** Based on the number of conflicts between queens.
- **🧩 Min-Conflicts:** To guide solutions towards feasibility.

## Algorithm Workflow
The hybrid approach combines a **Genetic Algorithm (GA)** with the **Min-Conflicts heuristic** to iteratively refine solutions for the N-Queens problem. The process consists of the following steps:

- **Initialization:**  
Generate an initial population of random board configurations. Each board is represented as a bitboard, enabling fast state manipulation.  

- **Selection:**  
Choose parents for the next generation using **`Tournament Selection (10% pool)`** or **`Roulette-Wheel Selection (20% rate)`**.  

- **Crossover:**  
Apply **`One-Point (90% probability)`** or **`Two-Point crossover`**, exchanging partial board states between parents.  

- **Mutation:**  
Introduce diversity using **`Swap Random (SR)`** or **`Swap Neighbor (SN)`** mutations, occurring with a **`3% probability`**.  

- **Conflict Reduction (Min-Conflicts Heuristic):**  
With a **`10% probability`**, the algorithm applies **`Min-Conflicts`** to adjust queen positions toward a conflict-free solution.  

- **Termination:**  
**`All valid solutions`** (conflict-free board) were found or the maximum limit of **`250 generations`** is reached.

## Experimental Results

Three experimental phases were conducted:

- **Phase 1 - Evaluation of different GA configurations on n=8:**  
Results showed that Tournament Selection and Two-Point Crossover yielded the best performance. Min-Conflicts significantly improved success rates, achieving up to 100% success rate in some configurations.
  
- **Phase 2 - Testing the hybrid approach on larger board sizes (n=10, 20, 30, 40, 50):**  
The bitboard-based representation allowed the algorithm to scale efficiently, consistently finding solutions in fewer than 5 generations for all tested board sizes.
  
- **Phase 3 - Assessing the ability to find all possible solutions for n=8–11:**  
Results indicated that Roulette-Wheel Selection consistently found 100% of all possible solutions, while Tournament Selection was slightly less consistent for larger n.

## Installation
Ensure you have Python installed. Then, create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Optional Parameters
Customize the algorithm with selection, crossover and mutation strategies:

| Argument         | Type        | Description                                  |
|-----------------|------------|----------------------------------------------|
| `--n`          | int        | Size of the chessboard (N-Queens)           |
| `--population` | int        | Number of individuals in the population      |
| `--generations`| int        | Number of generations to evolve             |
| `--TM size prob` | float, float | Tournament selection (size ratio, probability) |
| `--RW prob`    | float      | Roulette Wheel selection probability        |
| `--RB prob`    | float      | Rank-based selection probability            |
| `--OP prob`    | float      | One-point crossover probability             |
| `--TP prob`    | float      | Two-point crossover probability             |
| `--SN prob`    | float      | Swap neighbor mutation probability          |
| `--SR prob`    | float      | Swap random mutation probability            |
| `--MC prob iter` | float, int | Min-conflicts (probability, max iterations)  |

### Example Usage
```bash
python ga_cli.py --n 6 --population 200 --generations 250 --TM 0.2 0.8 --OP 0.9 --SN 0.1
```

### Printed Results
```bash
   _ Q _ _ _ _    _ _ _ _ Q _
   _ _ _ Q _ _    _ _ Q _ _ _
   _ _ _ _ _ Q    Q _ _ _ _ _
   Q _ _ _ _ _    _ _ _ _ _ Q
   _ _ Q _ _ _    _ _ _ Q _ _
   _ _ _ _ Q _    _ Q _ _ _ _   ...
```

## Project Structure
```plaintext
│── Genetic_Algorithm   # Core GA classes (e.g., chromosome, population)
│   │── Operators       # Selection, crossover, mutation strategies
│── Tests               # Unit tests for correctness
│── Utilities           # Bitboard representations and helper functions
│── ga_cli.py
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

---

## License
This project is licensed under the MIT License.

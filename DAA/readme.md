# SPPU BE Projects Semester 7 - Design and Analysis of Algorithms (DAA)
This repository contains implementations for Design and Analysis of Algorithms (DAA) assignments as part of the Semester 7 BE (Bachelor of Engineering) curriculum at Savitribai Phule Pune University (SPPU). The assignments cover various algorithmic techniques including recursion, greedy methods, dynamic programming, and backtracking. Only source code files are included. 

## Assignments Overview
### Assignment 1: Fibonacci Numbers with Step Count
- **Files**:
  - `Fibononrecur.cpp` (Non-recursive implementation)
  - `Fiborecur.cpp` (Recursive implementation)
- **Description**: Calculate Fibonacci numbers and track the number of steps taken using both non-recursive and recursive approaches.
- **Tasks**: Implement Fibonacci series generation and measure step count for performance analysis.
- **Output**: Displays the Fibonacci series and total steps taken.

**Complexity Analysis**:
| Version | Time Complexity | Space Complexity | Best Case | Worst Case | Average Case | Notes |
|---------|-----------------|------------------|-----------|------------|--------------|-------|
| **Iterative (Non-recursive)** | O(n) | O(1) | O(n) | O(n) | O(n) | Linear time due to single loop; constant space (only a few variables). All cases identical as input size n determines loops. |
| **Recursive** | O(2^n) | O(n) | O(2^n) | O(2^n) | O(2^n) | Exponential time due to redundant recursive calls (fibonacci tree); O(n) stack space. All cases identical; degrades rapidly for n > 30 (stack overflow). |

### Assignment 2: Fractional Knapsack Problem
- **Files**:
  - `knapsack.py` (Python implementation)
- **Description**: Solve the fractional knapsack problem using a greedy method to maximize profit within a given capacity.
- **Tasks**: Sort items by value-to-weight ratio, greedily select items, and compute the maximum price.
- **Output**: Displays the maximum profit achievable.

**Complexity Analysis**:
| Aspect | Time Complexity | Space Complexity | Best Case | Worst Case | Average Case | Notes |
|--------|-----------------|------------------|-----------|------------|--------------|-------|
| **Overall** | O(N log N) | O(N) | O(N log N) | O(N log N) | O(N log N) | Dominated by sorting (Timsort in Python); linear scan for selection. Space for temporary sorted array. All cases similar as sorting is stable and input-independent for complexity. |

### Assignment 3: 0-1 Knapsack Problem
- **Files**:
  - `knapsack01.cpp`
- **Description**: Solve the 0-1 knapsack problem using dynamic programming to maximize profit without fractional items.
- **Tasks**: Use a 2D DP table to compute the maximum value for a given capacity.
- **Output**: Displays the maximum profit earned.

**Complexity Analysis**:
| Aspect | Time Complexity | Space Complexity | Best Case | Worst Case | Average Case | Notes |
|--------|-----------------|------------------|-----------|------------|--------------|-------|
| **Overall** | O(N * W) | O(N * W) | O(N * W) | O(N * W) | O(N * W) | Pseudo-polynomial; double nested loops fill the DP table. Space for 2D array (optimizable to O(W) with 1D array). All cases identical as it's deterministic and exhaustive. |

### Assignment 4: 8-Queens Problem with Backtracking
- **Files**:
  - `nqueens.py` (Python implementation)
- **Description**: Design an 8x8 chessboard with the first queen placed, using backtracking to place the remaining queens such that no two queens threaten each other.
- **Tasks**: Implement backtracking to find valid configurations, starting with a user-specified first queen position.
- **Output**: Displays all possible 8-Queens solutions with the first queen fixed.

**Complexity Analysis**:
| Aspect | Time Complexity | Space Complexity | Best Case | Worst Case | Average Case | Notes |
|--------|-----------------|------------------|-----------|------------|--------------|-------|
| **Overall** | O(N!) | O(N) | O(1) (if pre-placed queen leads to quick failure) | O(N!) (full permutation exploration) | O(N!/2) (with pruning) | Backtracking explores permutations with pruning for conflicts; 1D board uses O(N) space (recursion stack). Best case: Invalid start prunes early; worst: Dense solutions require full search. |

## Requirements
To run the code, you'll need the following:
- **C++**: A C++ compiler (e.g., g++) for `Fibononrecur.cpp`, `Fiborecur.cpp`, and `knapsack01.cpp`.
- **Python**: Python 3.x with no additional libraries required for `knapsack.py` and `nqueens.py`.

## How to Run
1. Clone the repository:
   ```
   git clone https://github.com/AB2511/SPPU-BE-Practicals-Sem-7.git
   ```
2. Navigate to the DAA folder:
   ```
   cd SPPU-BE-Practicals-Sem-7/DAA 
   ```

### For C++ Files (`Fibononrecur.cpp`, `Fiborecur.cpp`, `knapsack01.cpp`)
- Compile:
  ```
  g++ Fibononrecur.cpp -o fib_non_recur
  g++ Fiborecur.cpp -o fib_recur
  g++ knapsack01.cpp -o knapsack01
  ```
- Run:
  ```
  ./fib_non_recur
  ./fib_recur
  ./knapsack01
  ```
- Input the number of elements when prompted for Fibonacci files; `knapsack01.cpp` uses predefined values.

### For Python Files (`knapsack.py`, `nqueens.py`)
- Run:
  ```
  python knapsack.py
  python nqueens.py
  ```
- For `nqueens.py`, enter the row and column (0-7) for the first queen when prompted.

## Notes
- Outputs may vary based on input values (e.g., number of Fibonacci elements, first queen position).
- These assignments are for educational purposes only.
- Complexity analyses are based on standard asymptotic notations (Big-O) and consider input-dependent behaviors where applicable. 

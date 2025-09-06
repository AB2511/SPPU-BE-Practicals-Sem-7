# SPPU BE Projects Semester 7 - Design and Analysis of Algorithms (DAA)

This repository contains implementations for Design and Analysis of Algorithms (DAA) assignments as part of the Semester 7 BE (Bachelor of Engineering) curriculum at Savitribai Phule Pune University (SPPU). The assignments cover various algorithmic techniques including recursion, greedy methods, dynamic programming, and backtracking. Only source code files and Word documents (.docx) with code and outputs are included. Datasets or additional resources are not required unless specified.

## Assignments Overview

### Assignment 1: Fibonacci Numbers with Step Count
- **Files**: 
  - `Fibononrecur.cpp` (Non-recursive implementation)
  - `Fiborecur.cpp` (Recursive implementation)
  - `DAAassignment1.docx` (includes code and output screenshots)
- **Description**: Calculate Fibonacci numbers and track the number of steps taken using both non-recursive and recursive approaches.
- **Tasks**: Implement Fibonacci series generation and measure step count for performance analysis.
- **Output**: Displays the Fibonacci series and total steps taken (screenshots in `DAAassignment1.docx`).

### Assignment 2: Fractional Knapsack Problem
- **Files**: 
  - `knapsack.py` (Python implementation)
  - `DAAassignment2.docx` (includes code and output screenshot)
- **Description**: Solve the fractional knapsack problem using a greedy method to maximize profit within a given capacity.
- **Tasks**: Sort items by value-to-weight ratio, greedily select items, and compute the maximum price.
- **Time Complexity**: O(N * log N)
- **Auxiliary Space**: O(N)
- **Output**: Displays the maximum profit achievable (screenshot in `DAAassignment2.docx`).

### Assignment 3: 0-1 Knapsack Problem
- **Files**:
  - `knapsack01.cpp` 
  - `DAAassignment3.docx` (includes C++ code and output screenshot)
- **Description**: Solve the 0-1 knapsack problem using dynamic programming to maximize profit without fractional items.
- **Tasks**: Use a 2D DP table to compute the maximum value for a given capacity.
- **Time Complexity**: O(N * W) where N is the number of items and W is the capacity.
- **Auxiliary Space**: O(N * W)
- **Output**: Displays the maximum profit earned (screenshot in `DAAassignment3.docx`).

### Assignment 4: 8-Queens Problem with Backtracking
- **Files**: 
  - `nqueens.py` (Python implementation)
  - `DAAassignment4.docx` (includes code and output screenshots)
- **Description**: Design an 8x8 chessboard with the first queen placed, using backtracking to place the remaining queens such that no two queens threaten each other.
- **Tasks**: Implement backtracking to find valid configurations, starting with a user-specified first queen position.
- **Output**: Displays all possible 8-Queens solutions with the first queen fixed (screenshots in `DAAassignment4.docx`).

## Requirements
To run the code, you'll need the following:
- **C++**: A C++ compiler (e.g., g++) for `Fibononrecur.cpp` and `Fiborecur.cpp`.
- **Python**: Python 3.x with no additional libraries required for `knapsack.py` and `nqueens.py`.

## How to Run
1. Clone the repository:  
   ```
   git clone [https://github.com/AB2511/SPPU-BE-Practicals-Sem-7.git]
   ```
2. Navigate to the DAA folder:  
   ```
   cd SPPU-BE-Practicals-Sem-7/DAA assignemnt
   ```

### For C++ Files (`Fibononrecur.cpp`, `Fiborecur.cpp`)
- Compile:  
  ```
  g++ Fibononrecur.cpp -o fib_non_recur
  g++ Fiborecur.cpp -o fib_recur
  ```
- Run:  
  ```
  ./fib_non_recur
  ./fib_recur
  ```
- Input the number of elements when prompted.

### For Python Files (`knapsack.py`, `nqueens.py`)
- Run:  
  ```
  python knapsack.py
  python nqueens.py
  ```
- For `nqueens.py`, enter the row and column (0-7) for the first queen when prompted.

## Notes
- The `.docx` files contain code, explanations, and output screenshots for reference.
- Outputs may vary based on input values (e.g., number of Fibonacci elements, first queen position).
- These assignments are for educational purposes only.

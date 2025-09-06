#include <iostream>

// Global variable to count the number of steps (function calls)
long long step_count = 0;

// Recursive function to calculate the nth Fibonacci number
long long fibonacciRecursive(int n) {
    // A step is counted for every function call
    step_count++;

    // Base cases
    if (n <= 1) {
        return n;
    }

    // Recursive calls
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

int main() {
    int number;

    std::cout << "Enter the number of elements: ";
    std::cin >> number;

    if (number <= 0) {
        std::cout << "Number of elements must be greater than 0." << std::endl;
        return 1;
    }

    std::cout << "Fibonacci Series: ";

    for (int i = 0; i < number; ++i) {
        std::cout << fibonacciRecursive(i) << " ";
    }

    std::cout << "\nTotal steps taken: " << step_count << std::endl;

    return 0;
}


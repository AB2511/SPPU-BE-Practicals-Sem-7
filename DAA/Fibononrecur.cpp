#include <iostream>

int main() {
    long long n1 = 0, n2 = 1, n3, i, number;
    long long step_count = 0;

    std::cout << "Enter the number of elements: ";
    std::cin >> number;

    if (number <= 0) {
        std::cout << "Number of elements must be greater than 0." << std::endl;
        return 1;
    }

    // Step count for printing the first two elements
    if (number >= 1) {
        std::cout << n1 << " ";
        step_count++;
    }
    if (number >= 2) {
        std::cout << n2 << " ";
        step_count++;
    }

    // Loop to calculate the rest of the elements
    for (i = 2; i < number; ++i) {
        n3 = n1 + n2;
        std::cout << n3 << " ";
        n1 = n2;
        n2 = n3;
        step_count++; // Increment step count for each calculation
    }

    std::cout << "\nTotal steps taken: " << step_count << std::endl;

    return 0;
}

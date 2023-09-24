#include<iostream>

int main() {
    int sides;
    int rolled_number;

    std::cout << "Enter the number of sides of the die: ";
    std::cin >> sides;

    // Generate a random number between 1 and sides
    srand(time(NULL));
    rolled_number = rand() % sides + 1;
    std::cout << "You rolled a " << rolled_number << std::endl;

    return 0;
}
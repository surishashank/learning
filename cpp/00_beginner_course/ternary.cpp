#include<iostream>

int main() {
    std::cout << "Enter a number: ";
    int number;
    std::cin >> number;

    number % 2 == 0 ? std::cout << "EVEN" << std::endl : std::cout << "ODD" << std::endl;

    return 0;
}
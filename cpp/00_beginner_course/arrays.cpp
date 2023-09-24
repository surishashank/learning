#include<iostream>

int main() {
    int size;
    std::string foods[] = {"Pizza", "Burger", "Pasta", "Fries", "Sandwich"};

    // std::cout << "Enter the size of the array: ";
    // std::cin >> size;
    // fill(foods, foods + size, "Pizza");

    // print the array
    for (int i = 0; i < foods->length(); i++) {
        std::cout << foods[i] << std::endl;
    }

    std::cout << "The size of the array is: " << sizeof(foods)/sizeof(foods[0]) << std::endl;

    return 0;
}
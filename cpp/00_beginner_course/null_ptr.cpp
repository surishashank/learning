#include<iostream>

int main() {
    int *pointer = nullptr;
    int number = 5;
    pointer = &number;

    if (pointer) {
        std::cout << "The value of pointer is: " << *pointer << std::endl;
    } else {
        std::cout << "The pointer is a null pointer" << std::endl;
    }
}
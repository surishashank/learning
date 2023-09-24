#include<iostream>

int main() {
    int month;
    std::cout << "Enter month number: ";
    std::cin >> month;

    switch (month)
    {
    case 1:
        std::cout << "January" << std::endl;
        break;
    case 2:
        std::cout << "February" << std::endl;
        break;
    case 3:
        std::cout << "March" << std::endl;
        break;
    case 4:
        std::cout << "April" << std::endl;
        break;
    default:
        std::cout << "Invalid month" << std::endl;
        break;
    }

    return 0;
}
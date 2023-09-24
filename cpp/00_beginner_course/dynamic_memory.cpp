#include <iostream>

int main() {
    char *grades = NULL;
    int num_grades;

    std::cout << "How many grades do you want to enter? ";
    std::cin >> num_grades;

    grades = new char[num_grades];

    for (int i = 0; i < num_grades; i++) {
        char grade;
        std::cout << "Enter grade #" << i + 1 << ": ";
        std::cin >> grade;
        grades[i] = grade;
    }

    std::cout << "The grades you entered are: " << std::endl;
    for (int i = 0; i < num_grades; i++) {
        std::cout << grades[i] << std::endl;
    }

    delete[] grades;

    return 0;
}
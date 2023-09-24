#include<iostream>

int main() {
    float a;
    float b;
    float c;

    std::cout << "Enter the first side of the triangle: ";
    std::cin >> a;
    std::cout << "Enter the second side of the triangle: ";
    std::cin >> b;

    c = sqrt(a * a + b * b);
    std::cout << "The hypotenuse is: " << c << std::endl;
    
    return 0;
}
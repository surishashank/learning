#include<iostream>
#include <vector>

// typedef std::string text_t;
using text_t = std::string;
// typedef int number_t;
using number_t = int;


int main() {
    text_t text = "Hello World";
    number_t number = 5;

    std::cout << text << std::endl;
    std::cout << number << std::endl;
    return 0;
}
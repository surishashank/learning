#include <iostream>
#include <thread>

void function1(char symbol) {
    for(int i = 0; i < 200; i++)
        std::cout << symbol;
}

void function2() {
    for(int i = 0; i < 200; i++)
        std::cout << "-";
}

int main() {

    std::thread worker1(function1, 'x');
    std::thread worker2(function1, '=');
    
    worker1.join();
    worker2.join();
    
    system("pause>nul");

    // return 0;
}
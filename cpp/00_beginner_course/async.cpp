#include<iostream>
#include<future>

int square(int x) {
    int retval = x * x;
    std::string msg = "The answer will be: " + std::to_string(retval) + "\n";
    // msg.append(std::to_string(retval));
    // msg.append("\n");
    std::cout << msg;
    return retval;
}

int main() {
    std::future<int> result = std::async(square, 12);

    for(int i = 0; i < 10; i++) {
        std::cout << square(i) << std::endl;
    }

    std::cout << "Result: " << result.get() << std::endl;

    return 0;
}


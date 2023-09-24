#include <iostream>

template <typename T, typename U>
auto max(T a, U b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << max(6, 6.33) << std::endl;

    return 0;
}


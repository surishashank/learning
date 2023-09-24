#include <iostream>
using namespace std;


namespace first {
    int x = 5;
}

namespace second {
    double x = 3.1416;
}

// Print "hello world"
int main() {
    cout << first::x << endl;
    cout << second::x << endl;
    bool x = true;
    cout << x << endl;
    return 0;
}
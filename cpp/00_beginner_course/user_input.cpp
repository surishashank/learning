#include<iostream>
using namespace std;

int main() {
    cout << "What's your name?" << endl;
    string name;
    getline(cin, name);

    cout << "How old are you?" << endl;
    float age;
    cin >> age;

    cout << "Hello " << name << endl;
    cout << "You are " << age << " years old" << endl;

    return 0;
}
#include <iostream>
#include <map>

void modifyMap(std::map<int, std::string> myMap) {
    myMap[1] = "Modified";
}

int main() {
    std::map<int, std::string> myMap;
    myMap[1] = "Original";
    
    modifyMap(myMap);

    std::cout << myMap[1] << std::endl; // Output: Original
    return 0;
}

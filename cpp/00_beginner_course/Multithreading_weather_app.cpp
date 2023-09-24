#include <iostream>
#include <map>
#include <thread>


void increment_temperatures(std::map<std::string, int>& forecastMap) {
    // while (true) {
    for (int i = 0; i < 2; i++) {
        for (auto& pair : forecastMap) {
            pair.second++;
        }

        // print the map
        for (auto& pair : forecastMap) {
            std::cout << pair.first << ": " << pair.second << std::endl;
        }

        // sleep for 2 seconds
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
}

int main() {
    std::map<std::string, int> forecastMap = {
        {"New York", 32}, 
        {"Chicago", 28}, 
        {"Minneapolis", 25}, 
        {"Denver", 22}
    };

    std::thread worker(increment_temperatures, std::ref(forecastMap));
    worker.join();
    // char temp;
    // std::cin >> temp;
    // system("pause>nul");
}
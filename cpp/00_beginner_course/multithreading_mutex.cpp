#include <iostream>
#include <thread>
#include <mutex>

std::mutex lock;
int shared_value = 0;

void increment_shared_value() {
    std::lock_guard<std::mutex> guard(lock);
    shared_value++;
}

int main() {
    std::vector<std::thread> threads;
    for (size_t i = 0; i < 10000; i++) {
        threads.push_back(std::thread(increment_shared_value));
    }

    for (auto& thread : threads) {
        thread.join();
    }

    std::cout << "shared_value: " << shared_value << std::endl;

    return 0;
}
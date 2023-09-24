#ifndef BOOKLEVEL_HPP
#define BOOKLEVEL_HPP

#include <iostream>

class BookLevel {
   private:
    double price;
    double volume;
    int timestamp;

   public:
    BookLevel(double price, double volume, int timestamp) {
        this->price = price;
        this->volume = volume;
        this->timestamp = timestamp;
    }
    double getPrice() { return price; }
    double getVolume() { return volume; }
    int getTimestamp() { return timestamp; }
    void print() {
        std::string msg = std::to_string(volume) + " @ " +
                          std::to_string(price) + "\t [" +
                          std::to_string(timestamp) + "]\n";
        std::cout << msg;
    }
};

#endif  // BOOKLEVEL_HPP
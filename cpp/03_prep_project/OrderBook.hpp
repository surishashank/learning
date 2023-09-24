#ifndef ORDERBOOK_HPP
#define ORDERBOOK_HPP

#include <iostream>
#include <mutex>
#include <nlohmann/json.hpp>
#include "BookLevel.hpp"

class OrderBook {
   private:
    std::vector<BookLevel> bids;
    std::vector<BookLevel> asks;
    std::mutex ob_mutex;

   public:
    void update(std::vector<BookLevel> bids, std::vector<BookLevel> asks);
    void print(int levels);
    std::vector<BookLevel> get_bids();
    std::vector<BookLevel> get_asks();
};

#endif  // ORDERBOOK_HPP
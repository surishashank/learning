#include "OrderBook.hpp"

void OrderBook::update(std::vector<BookLevel> bids,
                       std::vector<BookLevel> asks) {
    std::lock_guard<std::mutex> lock(ob_mutex);
    this->bids = bids;
    this->asks = asks;
}

void OrderBook::print(int levels) {
    std::lock_guard<std::mutex> lock(ob_mutex);
    std::cout << "Asks:" << std::endl;
    for (int i = std::min(levels, (int)asks.size()) - 1; i >= 0; i--) {
        asks[i].print();
    }
    std::cout << "Bids:" << std::endl;
    for (int i = 0; i < levels && i < bids.size(); i++) {
        bids[i].print();
    }
}

std::vector<BookLevel> OrderBook::get_bids() {
    std::lock_guard<std::mutex> lock(ob_mutex);
    return bids;
}

std::vector<BookLevel> OrderBook::get_asks() {
    std::lock_guard<std::mutex> lock(ob_mutex);
    return asks;
}
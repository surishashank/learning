#ifndef ORDERBOOKANALYZER_HPP
#define ORDERBOOKANALYZER_HPP

#include <iostream>
#include <thread>
#include <mutex>
#include "OrderBook.hpp"
#include "Constants.hpp"

class OrderBookAnalyzer {
    private:
        std::string symbol;
        OrderBook order_book;

        std::string get_request_url(int levels = kConsts::MAX_LEVELS);
        std::pair<std::vector<BookLevel>, std::vector<BookLevel>> get_bids_and_asks_from_response(nlohmann::json response);

    public:
        OrderBookAnalyzer(std::string symbol) {
            this->symbol = symbol;
        }

        // Starts a thread that updates the order book every update_freq seconds
        void run_service(int update_freq_sec, int levels, double order_size_usd, double order_size_coins);
        void print_order_book(int levels);
        void fill_usd_order(double order_size_usd);
        void fill_coin_order(double order_size_coins);
};

#endif // ORDERBOOKANALYZER_HPP
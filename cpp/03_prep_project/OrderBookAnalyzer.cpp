#include "OrderBookAnalyzer.hpp"
#include "Constants.hpp"
#include "JSONFetcher.hpp"

std::string OrderBookAnalyzer::get_request_url(int levels) {
    std::string url = kConsts::KRAKEN_BASE_URL +
                      kConsts::KRAKEN_ORDER_BOOK_ENDPOINT + "?pair=" + symbol +
                      "&count=" + std::to_string(levels);
    return url;
}

void OrderBookAnalyzer::run_service(int update_freq_sec, int display_levels, double order_size_usd,
                                    double order_size_coins) {
    // Get the URL to send the request to
    std::string url = get_request_url(kConsts::MAX_LEVELS);

    while (true) {
        nlohmann::json response = JSONFetcher::getJSONDataFromURL(url);

        std::pair<std::vector<BookLevel>, std::vector<BookLevel>> bids_and_asks = get_bids_and_asks_from_response(response);

        // std::vector
        order_book.update(bids_and_asks.first, bids_and_asks.second);
        print_order_book(display_levels);
        fill_usd_order(order_size_usd);
        fill_coin_order(order_size_coins);

        // Sleep for update_freq seconds
        std::this_thread::sleep_for(std::chrono::seconds(update_freq_sec));
    }
}

std::pair<std::vector<BookLevel>, std::vector<BookLevel>> OrderBookAnalyzer::get_bids_and_asks_from_response(nlohmann::json response) {
    std::vector<BookLevel> bid_levels;
    std::vector<BookLevel> ask_levels;

    // if error, then return empty json
    if (response[kConsts::KEY_ERROR].size() > 0) {
        std::cerr << "ERROR: " << response[kConsts::KEY_ERROR] << std::endl;
        return std::pair<std::vector<BookLevel>, std::vector<BookLevel>>(bid_levels, ask_levels);
    }

    // ensure that result only has one key
    if (response[kConsts::KEY_RESULT].size() != 1) {
        std::cerr << "ERROR: Response has more than one key in result" << std::endl;
        return std::pair<std::vector<BookLevel>, std::vector<BookLevel>>(bid_levels, ask_levels);
    }

    nlohmann::json bid_ask_map = response[kConsts::KEY_RESULT].begin().value();
    nlohmann::json bids = bid_ask_map[kConsts::KRAKEN_ORDER_BOOK_BIDS_KEY];
    nlohmann::json asks = bid_ask_map[kConsts::KRAKEN_ORDER_BOOK_ASKS_KEY];

    // iterate over bids
    for (auto& bid : bids) {
        double price = std::stod(bid[0].get<std::string>());
        double volume = std::stod(bid[1].get<std::string>());
        int timestamp = bid[2].get<int>();
        BookLevel level(price, volume, timestamp);
        bid_levels.push_back(level);
    }

    // iterate over asks
    for (auto& ask : asks) {
        double price = std::stod(ask[0].get<std::string>());
        double volume = std::stod(ask[1].get<std::string>());
        int timestamp = ask[2].get<int>();
        BookLevel level(price, volume, timestamp);
        ask_levels.push_back(level);
    }

    return std::pair<std::vector<BookLevel>, std::vector<BookLevel>>(bid_levels, ask_levels);
}

void OrderBookAnalyzer::print_order_book(int levels) {
    order_book.print(levels);
}

void OrderBookAnalyzer::fill_usd_order(double order_size_usd) {
    double remaining_usd = order_size_usd;
    double fill_qty = 0.0;
    double order_cost = 0.0;
    double avg_price = 0.0;
    if (order_size_usd > 0) {
        std::vector<BookLevel> asks = order_book.get_asks();
        for (int i = 0; i < asks.size() && remaining_usd > 0; i++) {
            BookLevel level = asks[i];
            double max_fill_usd = level.getPrice() * level.getVolume();
            double fill_cost_usd = std::min(remaining_usd, max_fill_usd);
            fill_qty += (fill_cost_usd / level.getPrice());
            order_cost += fill_cost_usd;
            remaining_usd -= fill_cost_usd;
        }
        avg_price = order_cost / fill_qty;
    } else if (order_size_usd < 0) {
        remaining_usd = -remaining_usd;
        std::vector<BookLevel> bids = order_book.get_bids();
        for (int i = 0; i < bids.size() && remaining_usd > 0; i++) {
            BookLevel level = bids[i];
            double max_fill_usd = level.getPrice() * level.getVolume();
            double fill_cost_usd = std::min(remaining_usd, max_fill_usd);
            fill_qty += (fill_cost_usd / level.getPrice());
            order_cost += fill_cost_usd;
            remaining_usd -= fill_cost_usd;
        }
        avg_price = order_cost / fill_qty;
    }
    std::cout << "USD Fill Details: DesiredSizeUSD: " << order_size_usd << " FillQtyCoins: " << fill_qty
              << " FillCostUSD: " << order_cost << " AvgPriceUSD: " << avg_price << std::endl;
}

void OrderBookAnalyzer::fill_coin_order(double order_size_coins) {
    double remaining_coins = order_size_coins;
    double fill_qty = 0.0;
    double order_cost = 0.0;
    double avg_price = 0.0;
    if (order_size_coins > 0) {
        std::vector<BookLevel> asks = order_book.get_asks();
        for (int i = 0; i < asks.size() && remaining_coins > 0; i++) {
            BookLevel level = asks[i];
            double max_fill_coins = level.getVolume();
            double num_filled_coins = std::min(remaining_coins, max_fill_coins);
            fill_qty += num_filled_coins;
            order_cost += (num_filled_coins * level.getPrice());
            remaining_coins -= num_filled_coins;
        }
        avg_price = order_cost / fill_qty;
    } else if (order_size_coins < 0) {
        remaining_coins = -remaining_coins;
        std::vector<BookLevel> bids = order_book.get_bids();
        for (int i = 0; i < bids.size() && remaining_coins > 0; i++) {
            BookLevel level = bids[i];
            double max_fill_coins = level.getVolume();
            double num_filled_coins = std::min(remaining_coins, max_fill_coins);
            fill_qty += num_filled_coins;
            order_cost += (num_filled_coins * level.getPrice());
            remaining_coins -= num_filled_coins;
        }
        avg_price = order_cost / fill_qty;
    }
    std::cout << "Coin Fill Details: DesiredSizeCoins: " << order_size_coins << " FillQtyCoins: " << fill_qty
              << " FillCostUSD: " << order_cost << " AvgPriceUSD: " << avg_price << std::endl;
}

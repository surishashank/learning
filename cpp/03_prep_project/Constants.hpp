#ifndef CONSTANTS_HPP
#define CONSTANTS_HPP

#include <iostream>

namespace kConsts {
    const int MAX_LEVELS = 500;
    const std::string KRAKEN_BASE_URL = "https://api.kraken.com/0/";
    const std::string KRAKEN_ORDER_BOOK_ENDPOINT = "public/Depth";
    const std::string KRAKEN_ORDER_BOOK_SYMBOL_PARAM = "pair";
    const std::string KRAKEN_ORDER_BOOK_COUNT_PARAM = "count";

    const std::string KEY_ERROR = "error";
    const std::string KEY_RESULT = "result";
    const std::string KRAKEN_ORDER_BOOK_BIDS_KEY = "bids";
    const std::string KRAKEN_ORDER_BOOK_ASKS_KEY = "asks";
}

#endif // CONSTANTS_HPP
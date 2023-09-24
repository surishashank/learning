#include <iostream>
#include <string>
#include <map>
#include <thread>
#include "arg_parser.hpp"
#include "OrderBookAnalyzer.hpp"


int main(int argc, char* argv[]) {
    std::vector<std::string> required_params = {"-s"};
    std::vector<std::string> optional_params = {"-l", "-d", "-c"};

    std::string symbol;
    int display_levels = 5;
    double order_size_usd = 0.0;
    double order_size_coins = 0.0;

    // Create a map to store flag-value pairs
    std::map<std::string, std::string> argMap = get_argument_map(argc, argv, required_params, optional_params);

    // Make sure only one of -d or -c is entered
    // if (argMap.count("-d") && argMap.count("-c")) {
    //     std::cerr << "ERROR: Only one of -d or -c can be entered" << std::endl;
    //     print_help();
    // }

    symbol = argMap["-s"];
    if (argMap.count("-l")) display_levels = std::stoi(argMap["-l"]);
    if (argMap.count("-d")) order_size_usd = std::stod(argMap["-d"]);
    if (argMap.count("-c")) order_size_coins = std::stod(argMap["-c"]);

    std::cout << "Symbol: " << symbol << std::endl;
    std::cout << "Levels: " << display_levels << std::endl;
    std::cout << "Order size (USD): " << std::fixed << std::setprecision(3) << order_size_usd << std::endl;
    std::cout << "Order size (coins): " << order_size_coins << std::endl;

    OrderBookAnalyzer oba(symbol);

    // start a thread that updates the order book every 5 seconds
    std::thread service_thread = std::thread(&OrderBookAnalyzer::run_service, &oba, 5, display_levels,
                                             order_size_usd, order_size_coins);

    service_thread.join();
    return 0;
}

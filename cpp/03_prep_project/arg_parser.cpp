#include "arg_parser.hpp"

void print_help(bool exit_program) {
    std::cout << "****************************************************************" << std::endl;
    std::cout << "To run this program:" << std::endl;
    std::cout << "  ./main -s BTCUSD -l 5 -d 100000" << std::endl;
    std::cout << "Required params:" << std::endl;
    std::cout << "  -s <symbol>           Symbol to query" << std::endl;
    std::cout << "Optional params:" << std::endl;
    std::cout << "  -l <levels>           Number of levels to display (def = 5)" << std::endl;
    std::cout << "  -d <usd order size>   Order size in USD (positive = buy, negative = sell) [enter only one of -d or -c]" << std::endl;
    std::cout << "  -c <coins order size> Order size in coins (positive = buy, negative = sell) [enter only one of -d or -c]" << std::endl;
    std::cout << "****************************************************************" << std::endl << std::endl;
    if (exit_program) exit(1);
}

std::map<std::string, std::string> get_argument_map(int argc, char* argv[], std::vector<std::string> reqd_params, std::vector<std::string> optional_params) {
    std::map<std::string, std::string> arg_map;

    // Iterate through the command-line arguments
    for (int i = 1; i < argc; i += 2) {
        std::string flag = argv[i];
        std::string value = (i + 1 < argc) ? argv[i + 1] : ""; // Ensure there's a value

        // Check if the argument starts with a hyphen (flag)
        if (flag[0] == '-' && i + 1 < argc) {
            arg_map[flag] = value;
        } else {
            std::cerr << "ERROR: Invalid argument format: " << flag << " " << value << std::endl;
            print_help();
        }
    }

    // Make sure all required params exist
    for (std::string param : reqd_params) {
        if (!arg_map.count(param)) {
            std::cerr << "ERROR: Missing required param: " << param << std::endl;
            print_help();
        }
    }

    // Make sure all params are either required or optional
    for (auto const& [flag, value] : arg_map) {
        if (!std::count(reqd_params.begin(), reqd_params.end(), flag) &&
            !std::count(optional_params.begin(), optional_params.end(), flag)) {
            std::cerr << "ERROR: Unrecognized param: " << flag << " passed with value: " << value << std::endl;
            print_help();
        }
    }

    return arg_map;
}
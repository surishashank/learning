#ifndef ARG_PARSER_HPP
#define ARG_PARSER_HPP

#include <iostream>
#include <string>
#include <map>

void print_help(bool exit_program = true);
std::map<std::string, std::string> get_argument_map(int argc, char* argv[], std::vector<std::string> reqd_params, std::vector<std::string> optional_params);

#endif // ARG_PARSER_HPP
#include<iostream>
#include<fstream>
#include<nlohmann/json.hpp>

using namespace nlohmann;

int main() {
    std::ifstream jsonFileStream("./test_file.json");
    nlohmann::json jsonData = nlohmann::json::parse(jsonFileStream);

    // Pretty print to console
    std::cout << "**********************" << std::endl;
    std::cout << std::setw(4) << jsonData << std::endl << std::endl;
    std::cout << "**********************" << std::endl;

    // Accessing individual elements
    std::cout << std::endl << std::endl << "**********************" << std::endl;
    std::string version = jsonData["version"].get<std::string>();
    std::string server_host = jsonData["server"]["host"].get<std::string>();
    int server_port = jsonData["server"]["port"].get<int>();

    std::cout << "Version: " << version << std::endl;
    std::cout << "Server Host: " << server_host << std::endl;
    std::cout << "Server Port: " << server_port << std::endl;
    std::cout << "**********************" << std::endl;

    // Iterate over jsonData
    std::cout << std::endl << std::endl << "**********************" << std::endl;
    for (auto& element : jsonData.items()) {
        auto key = element.key();
        auto value = element.value();
        std::string type;
        if (value.is_array()) {
            type = "array";
        } else if (value.is_object()) {
            type = "map";
        }
        else {
            type = "other";
        }
        std::cout << "Key: " << key << " Value: " << value << " Type: " << type << std::endl;
    }
    std::cout << "**********************" << std::endl;

    // To find a particular key
    std::cout << std::endl << std::endl << "**********************" << std::endl;
    auto item = jsonData.find("server");
    std::cout << "We found the key: " << item.key() << " with value: " << item.value() << std::endl;
    std::cout << "**********************" << std::endl;

    // Pretty Write to a json file
    nlohmann::json jsonNew;
    jsonNew["name"] = "John Doe";
    jsonNew["age"] = 27;
    jsonNew["address"] = {
        {"street", "123 Main Street"},
        {"city", "New York"}
    };
    jsonNew["kids_names"] = {"John", "Jane", "Joe"};
    jsonNew["married"] = true;

    std::ofstream jsonOutStream("./test_file_out.json");
    jsonOutStream << std::setw(4) << jsonNew << std::endl;

    return 0;
}
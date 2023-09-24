#ifndef JSONFETCHER_HPP
#define JSONFETCHER_HPP

#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>


class JSONFetcher {
    private:
        static size_t writeCallBack(void *content, size_t size, size_t nmemb, std::string* output);

    public:
        static nlohmann::json getJSONDataFromURL(std::string url);
};

#endif // JSONFETCHER_HPP
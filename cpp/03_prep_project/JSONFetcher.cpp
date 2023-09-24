#include "JSONFetcher.hpp"

size_t JSONFetcher::writeCallBack(void *content, size_t size, size_t nmemb, std::string* output) {
    size_t total_size = size * nmemb;
    // Copy the data from content to output
    output->append((char*)content, total_size);
    return total_size;
}

nlohmann::json JSONFetcher::getJSONDataFromURL(std::string url) {
    CURL *curl = curl_easy_init();
    CURLcode res;
    nlohmann::json json_data;

    if (curl) {
        std::string response_data;

        // Set the URL
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        // Set the callback function
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeCallBack);
        // Set the data object (userdata)
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_data);
        // Set verbose to true so we can get more details about the request
        // curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
        // Perform the request
        res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: "
                      << curl_easy_strerror(res) << std::endl;
        } else {
            // Parse the json data using nlohmann/json library
            json_data = nlohmann::json::parse(response_data);
        }

        curl_easy_cleanup(curl);
    }

    return json_data;
}
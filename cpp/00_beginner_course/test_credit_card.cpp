#include <iostream>

bool test_luhn_algorithm(std::string card_number);

int main() {
    std::string card_number;
    bool is_valid_card_number = true;

    do {
        is_valid_card_number = true;
        std::cout << "Enter credit card number: ";
        std::getline(std::cin, card_number);
        std::cin.clear();
        fflush(stdin);

        // make sure that the card number is 16 digits long
        if (card_number.length() != 16) {
            std::cout << "Invalid card number. Must be 16 digits long"
                      << std::endl;
            is_valid_card_number = false;
            continue;
        }

        // make sure all characters are digits
        for (int i = 0; i < card_number.length(); i++) {
            if (!isdigit(card_number[i])) {
                std::cout << "Invalid card number. Must be all digits"
                          << std::endl;
                is_valid_card_number = false;
                break;
            }
        }
        if (!is_valid_card_number) continue;;

        // test for valid card number
        if (test_luhn_algorithm(card_number)) {
            std::cout << "Card number passes Luhn Algorithm" << std::endl;
            is_valid_card_number = true;
        } else {
            std::cout << "Card number fails Luhn Algorithm" << std::endl;
            is_valid_card_number = false;
        }
    } while (!is_valid_card_number);

    return 0;
}

bool test_luhn_algorithm(std::string card_number) {
    int sum = 0;

    for (int i = card_number.length() - 1; i >= 0; i--) {
        int digit_num_from_right = card_number.length() - i;
        // for even numbers from right
        if (digit_num_from_right % 2 == 0) {
            int doubled_num = (card_number[i] - '0') * 2;
            while (doubled_num > 0) {
                sum += doubled_num % 10;
                doubled_num /= 10;
            }
        }
        else {
            sum += card_number[i] - '0';
        }
    }

    return sum % 10 == 0;
}

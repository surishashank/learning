#include <iostream>
#include <iomanip>

void showBalance(float balance);
float deposit(float balance);
float withdraw(float balance);

int main() {
    float balance = 0;
    int choice;

    do {
        showBalance(balance);
        std::cout << "*******************\n"
                  << "Enter your choice:\n"
                  << "*******************"
                  << std::endl;
        std::cout << "1. Show Balance\n";
        std::cout << "2. Deposit\n";
        std::cout << "3. Withdraw\n";
        std::cout << "4. Exit\n";
        std::cin >> choice;

        std::cin.clear();
        fflush(stdin);

        switch (choice) {
            case 1:
                showBalance(balance);
                break;
            case 2:
                balance = deposit(balance);
                break;
            case 3:
                balance = withdraw(balance);
                break;
            case 4:
                std::cout << "Thank you for using our app" << std::endl;
                break;
            default:
                std::cout << "Invalid choice" << std::endl;
                break;
        }
    } while (choice != 4);

    return 0;
}

void showBalance(float balance) {
    // Display balance with 2 decimal places
    std::cout << "Your balance is: $" << std::fixed << std::setprecision(2)
              << balance << std::endl;
}

float deposit(float balance) {
    float amount;
    std::cout << "Enter amount to deposit: ";
    std::cin >> amount;
    if (amount <= 0) {
        std::cout << "Invalid amount" << std::endl;
        return balance;
    }

    balance += amount;
    std::cout << "Successfully deposited: $" << amount << std::endl;
    return balance;
}

float withdraw(float balance) {
    float amount;
    std::cout << "Enter amount to withdraw: ";
    std::cin >> amount;

    if (balance < amount) {
        std::cout << "Insufficient balance to withdraw $" << amount
                  << std::endl;
        return balance;
    }
    balance -= amount;
    std::cout << "Successfully withdrawn: $ " << amount << std::endl;
    return balance;
}

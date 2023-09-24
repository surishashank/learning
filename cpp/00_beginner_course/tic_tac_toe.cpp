#include <iostream>

void draw_board(char *spaces);
void player_move(char *spaces, char player);
void computer_move(char *spaces, char computer);
char check_winner(char *spaces, char player, char computer);
bool check_tie(char *spaces);
bool is_game_over(char *spaces, char player, char computer);

int main() {
    char spaces[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    char player = 'X';
    char computer = 'O';

    draw_board(spaces);
    while (true) {
        player_move(spaces, player);
        draw_board(spaces);
        if (is_game_over(spaces, player, computer)) break;

        computer_move(spaces, computer);
        draw_board(spaces);
        if (is_game_over(spaces, player, computer)) break;
    }

    return 0;
}

void draw_board(char *spaces) {
    std::cout << "     |     |     " << std::endl;
    std::cout << "  " << spaces[0] << "  |  " << spaces[1] << "  |  "
              << spaces[2] << std::endl;
    std::cout << "_____|_____|_____" << std::endl;
    std::cout << "     |     |     " << std::endl;
    std::cout << "  " << spaces[3] << "  |  " << spaces[4] << "  |  "
              << spaces[5] << std::endl;
    std::cout << "_____|_____|_____" << std::endl;
    std::cout << "     |     |     " << std::endl;
    std::cout << "  " << spaces[6] << "  |  " << spaces[7] << "  |  "
              << spaces[8] << std::endl;
    std::cout << "     |     |     " << std::endl << std::endl;
}

void player_move(char *spaces, char player) {
    int number;
    do {
        std::cout << "Enter a number between 1 and 9: ";
        std::cin >> number;
        std::cin.clear();
        fflush(stdin);
    } while (number < 1 || number > 9 || spaces[number - 1] != ' ');
    spaces[number - 1] = player;
}

void computer_move(char *spaces, char computer) {
    // generate a random number between 1 - 9
    srand(time(NULL));
    int number;
    do {
        number = rand() % 9 + 1;
    } while (spaces[number - 1] != ' ');
    spaces[number - 1] = computer;
}

char check_winner(char *spaces, char player, char computer) {
    // check for horizontal wins
    if (spaces[0] == spaces[1] && spaces[1] == spaces[2]) {
        if (spaces[0] == player || spaces[0] == computer) return spaces[0];
    }
    if (spaces[3] == spaces[4] && spaces[4] == spaces[5]) {
        if (spaces[3] == player || spaces[3] == computer) return spaces[3];
    }
    if (spaces[6] == spaces[7] && spaces[7] == spaces[8]) {
        if (spaces[6] == player || spaces[6] == computer) return spaces[6];
    }

    // check for vertical wins
    if (spaces[0] == spaces[3] && spaces[3] == spaces[6]) {
        if (spaces[0] == player || spaces[0] == computer) return spaces[0];
    }
    if (spaces[1] == spaces[4] && spaces[4] == spaces[7]) {
        if (spaces[1] == player || spaces[1] == computer) return spaces[1];
    }
    if (spaces[2] == spaces[5] && spaces[5] == spaces[8]) {
        if (spaces[2] == player || spaces[2] == computer) return spaces[2];
    }

    // check for diagonal wins
    if (spaces[0] == spaces[4] && spaces[4] == spaces[8]) {
        if (spaces[0] == player || spaces[0] == computer) return spaces[0];
    }
    if (spaces[2] == spaces[4] && spaces[4] == spaces[6]) {
        if (spaces[2] == player || spaces[2] == computer) return spaces[2];
    }

    return 0;
}

bool check_tie(char *spaces) {
    for (int i = 0; i < 9; i++) {
        if (spaces[i] == ' ') return false;
    }
    return true;
}

bool is_game_over(char *spaces, char player, char computer) {
    char winner = check_winner(spaces, player, computer);
    if (winner == player || winner == computer) {
        std::cout << winner << " wins!" << std::endl;
        return true;
    }
    if (check_tie(spaces)) {
        std::cout << "It's a tie!" << std::endl;
        return true;
    }
    return false;
}
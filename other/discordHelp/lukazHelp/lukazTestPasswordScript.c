#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h> // for isalpha()

#define SPECIAL_CHARS "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
#define SPECIAL_CHAR_COUNT strlen(SPECIAL_CHARS)

char random_special_char() {
    return SPECIAL_CHARS[rand() % SPECIAL_CHAR_COUNT];
}

char replace_with_number(char c) {
    switch (c) {
        case 'a': case 'A': return '4';
        case 'e': case 'E': return '3';
        case 'i': case 'I': return '1';
        case 'o': case 'O': return '0';
        case 's': case 'S': return '5';
        default: return c;
    }
}

void generate_password(char *input, char *related_word, char *password) {
    int len_input = strlen(input);
    int len_related = strlen(related_word);

    char temp_password[200];

    // Copy the original input to the temporary password
    strcpy(temp_password, input);

    // Apply transformations to each character in the primary word (input)
    for (int i = 0; i < len_input; i++) {
        int random_choice = rand() % 4; // Adjusted to 4 choices now

        switch (random_choice) {
            case 0:
                temp_password[i] = temp_password[i] ^ 32; // Toggle case
                break;
            case 1:
                temp_password[i] = replace_with_number(temp_password[i]); // Replace with a similar number
                break;
            case 2:
                temp_password[i] = random_special_char(); // Replace with a special character
                break;
            case 3:
                // Swap characters randomly (example: swap with next character)
                if (i < len_input - 1) {
                    char temp = temp_password[i];
                    temp_password[i] = temp_password[i + 1];
                    temp_password[i + 1] = temp;
                }
                break;
            default:
                break;
        }
    }
    // Randomize case for each character in related_word
    for (int i = 0; i < len_related; i++) {
        if (isalpha(related_word[i])) {
            if (rand() % 2 == 0) {
                related_word[i] = toupper(related_word[i]); // Randomly uppercase
            } else {
                related_word[i] = tolower(related_word[i]); // Randomly lowercase
            }
        }
    }

    // Generate special characters for prefix and suffix
    char prefix = random_special_char();
    char suffix = random_special_char();

    // Generate a random number (0-9)
    char random_digit = '0' + (rand() % 10);

    // Combine everything into the final password
    sprintf(password, "%c%s%c%s%c%c", prefix, temp_password, related_word[0], related_word + 1, suffix, random_digit);
}

int main() {
    srand(time(0));

    char input[100];
    char related_word[100];
    char password[300];

    printf("Enter the primary word: ");
    scanf("%s", input);

    printf("Enter the related word: ");
    scanf("%s", related_word);

    generate_password(input, related_word, password);

    printf("Generated Password: %s\n", password);

    return 0;
}
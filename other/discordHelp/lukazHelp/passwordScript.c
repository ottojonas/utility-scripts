#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>

// Function to generate a stronger password
void generatePassword(char *theme, char *newPassword) {
    // Example: Append "!2023" to the theme to make it stronger
    sprintf(newPassword, "%s!2023", theme);
}

// Function to hash the password using SHA-256
void hashPassword(char *password, unsigned char *hashedPassword) {
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password, strlen(password));
    SHA256_Final(hashedPassword, &sha256);
}

int main() {
    char theme[100];
    char newPassword[110]; // Assuming the new password won't exceed the length of theme + 10
    unsigned char hashedPassword[SHA256_DIGEST_LENGTH];
    int i;

    printf("Enter a theme for your password: ");
    fgets(theme, 100, stdin);
    theme[strcspn(theme, "\n")] = 0; // Remove newline character

    generatePassword(theme, newPassword);

    hashPassword(newPassword, hashedPassword);

    printf("Hashed Password: ");
    for(i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        printf("%02x", hashedPassword[i]);
    }
    printf("\n");

    return 0;
}
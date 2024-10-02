const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const randomNumber = Math.floor(Math.random() * 50) + 1;

function guessNumber() {
  readline.question("Guess a number between 1 and 50: ", (guess) => {
    const userGuess = Number(guess);

    if (userGuess == randomNumber) {
      console.log("Congratulations! You have guessed the number.");
      readline.close();
    } else if (userGuess > randomNumber) {
      console.log("Too high. Try again.");
      guessNumber();
    } else if (userGuess < randomNumber) {
      console.log("Too low. Try again.");
      guessNumber();
    }
  });
}

guessNumber();

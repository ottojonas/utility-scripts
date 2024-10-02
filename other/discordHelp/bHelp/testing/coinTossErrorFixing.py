import random

if __name__ == "__main__":
    score = int(0)
    for i in range(5):
        userChoice = input("Heads or Tails?")
        result = random.randint(1, 2)
        if result == 1:
            result = "heads"
        else:
            result = "tails"
        if result == "heads":
            if userChoice == result:
                print("You picked the right side! +1 Point")
                score = score + 1
            elif userChoice != result:
                print("unlucky it was heads")
        if result == "tails":
            if userChoice == result:
                print("You picked the right side! +1 Point")
                score = score + 1
            elif userChoice != result:
                print("unlucky it was tails")
    print("Your final score is", score)

import random

if __name__ == "__main__":
    score = int(0)
    for i in range(5):
        user_choice = input("enter choice (heads or tails): ")
        result = random.randint(1, 2)
        if result == 1:
            result = "heads"
        else:
            result = "tails"
        if result == "heads":
            if user_choice == result:
                print("correct")
                score += 1
            else:
                print("wrong result was tails")
        if result == "tails":
            if user_choice == result:
                print("correct")
                score += 1
            else:
                print("wrong, result was heads")

    print("thank you for playing")

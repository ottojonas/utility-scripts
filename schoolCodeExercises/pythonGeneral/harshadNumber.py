def isHarshad(number):
    digitSum = 0
    for digit in str(number):
        digitSum += int(digit)
    return number % digitSum == 0


def nthHarshad(number):
    count = 0
    num = 1
    while True:
        if isHarshad(num):
            count += 1
            if count == number:
                return num
        num += 1


number = int(input("Enter a number: "))
print("The " + str(number) + "th Harshad number is " + str(nthHarshad(number)))
# testing input 600 gave the output 3102

import random

c = []
d = []
s = []
t = []
while c < 3 and d < 3:
    t += 1
    randomNumber1 = random.randint(1, 6)
    randomNumber2 = random.randint(1, 6)
    print(f"randomNumber1: {randomNumber1}")
    print(f"randomNumber2: {randomNumber2}")
    s = s + randomNumber1 + randomNumber2
    if randomNumber1 or randomNumber2 == 6:
        c += 1
    if randomNumber1 == randomNumber2:
        d += 1
a = s // (t * 2)
print(c, d, a)

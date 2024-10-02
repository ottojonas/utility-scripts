data = ["A", "+", "B", "*", "C", "/", "D", "-", "E"]
left = [None, 0, None, 2, None, 1, None, 6, None]
right = [None, 3, None, 4, None, 7, None, 8, None]
root = 5


def P(T):
    # print(data[T])
    if left[T] is not None:
        P(left[T])
    # print(data[T])
    if right[T] is not None:
        P(right[T])
    print(data[T])


P(root)

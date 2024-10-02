left = [1, 3, 5, 7, None, 9, None, 11, None, None, None, None, None]
data = ["/", "+", "+", "*", "D", "+", "G", "+", "C", "E", "F", "A", "B"]
right = [2, 4, 6, 8, None, 10, None, 12, None, None, None, None, None]
root = 0


def P(T):
    # print(data[T])
    if left[T] is not None:
        P(left[T])
    # print(data[T])
    if right[T] is not None:
        P(right[T])
    print(data[T])


P(root)

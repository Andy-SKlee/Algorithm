def hanoi(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print(from_bar, " -> ", to_bar)
        return
    hanoi(n - 1, from_bar, aux_bar, to_bar)
    print(from_bar, " -> ", to_bar)
    hanoi(n - 1, aux_bar, to_bar, from_bar)
print("n = 1")
hanoi(1, 1, 3, 2)
print("n = 2")
hanoi(2, 1, 3, 2)
print("n = 3")
hanoi(3, 1, 3, 2)
print("n = 4")
hanoi(4, 1, 3, 2)
with open("01-input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

print([x * y for x in numbers for y in numbers if x + y == 2020][0])
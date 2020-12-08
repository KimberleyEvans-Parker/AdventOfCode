with open("01-input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

print([x * y * z for x in numbers for y in numbers for z in numbers if x + y + z == 2020][0])
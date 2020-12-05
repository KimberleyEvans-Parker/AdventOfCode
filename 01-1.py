with open("01-1-input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

for number in numbers:
    for number2 in numbers:
        if number + number2 == 2020:
            ans = number * number2
            break

print(ans)
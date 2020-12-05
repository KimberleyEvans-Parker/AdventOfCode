with open("01-input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

for number in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if number + number2 + number3 == 2020:
                ans = number * number2 * number3
                break

print(ans)
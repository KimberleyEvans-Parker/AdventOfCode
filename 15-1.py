with open("15-input.txt", "r") as f:
    numbers = list(map(int, f.readline().split(",")))

def getLastAppearance(num, numbers):
    for i in range(len(numbers) - 1, - 1, - 1):
        if numbers[i] == num:
            return i

for i in range(len(numbers), 2021):
    if numbers[i - 1] not in numbers[:i - 1]:
        numbers.append(0)
    else:
        numbers.append(i - 1 - getLastAppearance(numbers[i - 1], numbers[:i - 1]))

print(numbers[2019])

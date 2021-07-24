with open("01-input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

YEAR = 2020
checked = [0] * (YEAR // 2)

for number in numbers:
    place = min(number, YEAR - number)
    if checked[place]:
        print(place * (YEAR - place))
        break
    checked[place] = 1
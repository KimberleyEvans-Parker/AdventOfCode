import itertools
with open("08-input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = [0, lines[i]]

i = 0
acc = 0

while lines[i][0] == 0:
    lines[i][0] = 1
    command, value = lines[i][1].split()
    if command == "nop":
        i += 1
    elif command == "acc":
        acc += int(value)
        i += 1
    else:
        i += int(value)

print(acc)
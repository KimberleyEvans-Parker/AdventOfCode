import copy
with open("08-input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = [0, lines[i]]

def printLines(lines):
    for line in lines:
        print(line[1])

for j in range(len(lines)):
    i = 0
    acc = 0
    correct_lines = copy.deepcopy(lines)
    command, value = lines[j][1].split()
    if command == "acc": continue
    if command == "jmp":
        correct_lines[j][1] = "nop " + value
    else:
        correct_lines[j][1] = "jmp " + value

    program_terminates = False
    while correct_lines[i][0] == 0:
        correct_lines[i][0] = 1
        command, value = correct_lines[i][1].split()
        if command == "nop":
            i += 1
        elif command == "acc":
            acc += int(value)
            i += 1
        else:
            i += int(value)
        if i == len(correct_lines):
            program_terminates = True
            break
    if program_terminates:
        break

print(acc)
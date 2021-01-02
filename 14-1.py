with open("14-input.txt", "r") as f:
    lines = f.readlines()

total = 0
used_addresses = []
lines.reverse()
new_lines = []

# remove duplicate registers so that only the latter are used
for line in lines:
    if line.split()[0] == "mask":
        new_lines.append(line)
    else:
        address = (line[line.find("[") + 1:line.find("]")])
        if address not in used_addresses:
            used_addresses.append(address)
            new_lines.append(line)

new_lines.reverse()

for line in new_lines:
    if line.split()[0] == "mask":
        mask = line.split()[-1]
        mask = "".join(reversed(mask))
    else:
        value = int(line.split()[-1])
        reversed_binary_value = "".join(reversed(bin(value)[2:]))
        used_addresses.append(address)
        for i in range(len(mask)):
            if mask[i] == "X":
                continue
            if i >= len(reversed_binary_value):
                if mask[i] == "1":
                    value += 2 ** i
            elif mask[i] != reversed_binary_value[i]:
                if mask[i] == "1":
                    value += 2 ** i
                else:
                    value -= 2 ** i
        total += value

print(total)

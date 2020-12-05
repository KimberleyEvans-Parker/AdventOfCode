with open("03-1-input.txt", "r") as f:
    rows = f.readlines()

count = 0
x_pos = 0

for row in rows:
    if row[x_pos] == "#":
        count += 1
    x_pos = (x_pos + 3) % (len(row) - 1)

print(count)
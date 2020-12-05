with open("03-input.txt", "r") as f:
    rows = f.readlines()

total = 1

for x_inc in [1, 3, 5, 7, 0.5]:
    count = 0
    x_pos = 0
    for row in rows:
        if x_pos % 1 == 0:
            if row[int(x_pos)] == "#":
                count += 1
        x_pos = (x_pos + x_inc) % (len(row) - 1)
    total *= count

print(total)
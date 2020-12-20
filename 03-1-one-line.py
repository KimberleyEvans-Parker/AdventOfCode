with open("03-input.txt", "r") as f:
    rows = f.readlines()

print(sum(1 for i in range(len(rows)) if rows[i][int((i * 3) % (len(rows[0]) - 1))] == "#"))
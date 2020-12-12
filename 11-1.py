import copy
with open("11-input.txt", "r") as f:
    seat_map = f.readlines()

for i in range(len(seat_map)):
    seat_map[i] = seat_map[i].strip()
prev_seat_map = []

def numAdjacentSeats(prev_seat_map, row, col):
    count = 0
    if row > 0:
        if prev_seat_map[row - 1][col] == "#": # up
            count += 1
        if col > 0:
            if prev_seat_map[row - 1][col - 1] == "#": # up left
                count += 1
        if col < len(seat_map[0]) - 1:
            if prev_seat_map[row - 1][col + 1] == "#": # up right
                count += 1
    if row < len(seat_map) - 1:
        if prev_seat_map[row + 1][col] == "#": # down
            count += 1
        if col > 0:
            if prev_seat_map[row + 1][col - 1] == "#": # down left
                count += 1
        if col < len(seat_map[0]) - 1:
            if prev_seat_map[row + 1][col + 1] == "#": # down right
                count += 1
    if col > 0:
        if prev_seat_map[row][col - 1] == "#": # left
            count += 1
    if col < len(seat_map[0])  - 1:
        if prev_seat_map[row][col + 1] == "#": # right
            count += 1
    return count
    

while seat_map != prev_seat_map:
    prev_seat_map = copy.copy(seat_map)
    for row_num in range(len(seat_map)):
        new_row = ""
        for col_num in range(len(seat_map)):
            space_type = prev_seat_map[row_num][col_num]
            num_adjacent_seats = numAdjacentSeats(prev_seat_map, row_num, col_num)
            if space_type == ".":
                new_row += "."
            if space_type == "L":
                if num_adjacent_seats == 0:
                    new_row += "#"
                else:
                    new_row += "L"
            if space_type == "#":
                if num_adjacent_seats >= 4:
                    new_row += "L"
                else:
                    new_row += "#"
        seat_map[row_num] = new_row

print(sum([1 for row in seat_map for space in row if space == "#"]))
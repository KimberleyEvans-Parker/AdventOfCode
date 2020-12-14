import copy
with open("11-input.txt", "r") as f:
    seat_map = f.readlines()

for i in range(len(seat_map)):
    seat_map[i] = seat_map[i].strip()
prev_seat_map = []

def checkInDirection(prev_seat_map, row, col, row_direction, col_direction):
    if row + row_direction < 0 or row + row_direction >= len(prev_seat_map):
        return 0
    if col + col_direction < 0 or col + col_direction >= len(prev_seat_map[0]):
        return 0
    if prev_seat_map[row + row_direction][col + col_direction] == "#":
        return 1
    if prev_seat_map[row + row_direction][col + col_direction] == "L":
        return 0
    return checkInDirection(prev_seat_map, row + row_direction, col + col_direction, row_direction, col_direction)

def numAdjacentSeats(prev_seat_map, row, col):
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    count = 0
    for row_direction, col_direction in directions:
        count += checkInDirection(prev_seat_map, row, col, row_direction, col_direction)
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
                if num_adjacent_seats >= 5:
                    new_row += "L"
                else:
                    new_row += "#"
        seat_map[row_num] = new_row

print(sum([1 for row in seat_map for space in row if space == "#"]))
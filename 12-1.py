with open("12-input.txt", "r") as f:
    directions = f.readlines()

ship_facing = 0

compass_to_num = {"E": 0, "S": 1, "W": 2, "N": 3}

coords = [0,0]

for direction in directions:
    direction_type, amount = direction[0], int(direction[1:])
    if direction_type == "R":
        ship_facing = (ship_facing + amount / 90) % 4
    elif direction_type == "L":
        ship_facing = (ship_facing - amount / 90) % 4
    else:
        if direction_type == "F":
            movement_direction = ship_facing
        else:
            movement_direction = compass_to_num[direction_type]
        if movement_direction == 0:
            coords[0] += amount
        elif movement_direction == 1:
            coords[1] += amount
        elif movement_direction == 2:
            coords[0] -= amount
        elif movement_direction == 3:
            coords[1] -= amount

print(sum(coords))
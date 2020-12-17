with open("12-input.txt", "r") as f:
    directions = f.readlines()

ship_facing = 0 # East

ship_coords = [0, 0]
waypoint = [10, 1]

for direction in directions:
    direction_type, amount = direction[0], int(direction[1:])
    if direction_type == "R":
        for i in range(amount // 90):
            waypoint = [waypoint[1], -waypoint[0]] 
    elif direction_type == "L":
        for i in range(amount // 90):
            waypoint = [-waypoint[1], waypoint[0]]
    elif direction_type == "F":
        ship_coords[0] += waypoint[0] * amount
        ship_coords[1] += waypoint[1] * amount
    elif direction_type == "E":
        waypoint[0] += amount
    elif direction_type == "N":
        waypoint[1] += amount
    elif direction_type == "W":
        waypoint[0] -= amount
    elif direction_type == "S":
        waypoint[1] -= amount

print(sum(map(abs, ship_coords)))
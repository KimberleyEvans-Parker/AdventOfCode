with open("13-input.txt", "r") as f:
    time, bus_string = f.readlines()

time = int(time)
buses = []
for bus in bus_string.split(","):
    if bus != "x": buses.append(int(bus))
shortest_wait_time = buses[0] - time % buses[0]
earliest_bus = buses[0]

for bus in buses:
    bus_time = bus - time % bus
    if bus_time < shortest_wait_time:
        earliest_bus = bus
        shortest_wait_time = bus_time

print(earliest_bus * shortest_wait_time)
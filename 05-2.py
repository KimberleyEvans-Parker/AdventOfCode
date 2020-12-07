with open("05-input.txt", "r") as f:
    seats = f.readlines()

def get_seat_number(partition):
    partition = partition.replace("B", "1")
    partition = partition.replace("F", "0")
    partition = partition.replace("R", "1")
    partition = partition.replace("L", "0")
    seat_number = 0
    for i in range(0, len(partition)):
        if partition[9 - i] == "1":
            seat_number += 2 ** (i)
    return seat_number

seat_numbers = []
for seat in seats:
    seat_numbers.append(get_seat_number(seat))

seat_numbers.sort()
for i in range(1, len(seat_numbers)):
    if seat_numbers[i - 1] == seat_numbers[i] - 2:
        print(seat_numbers[i] - 1)
        break

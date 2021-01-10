with open("15-input.txt", "r") as f:
    numbers = list(map(int, f.readline().split(",")))

import time

start = time.time()

numbers_dict = {}
for i in range(len(numbers) - 1):
    numbers_dict[numbers[i]] = i

i = len(numbers)
curr_num = numbers[-1]

while i < 30000000: # 30000000:
    if curr_num not in numbers_dict.keys():
        numbers_dict[curr_num] = i - 1
        curr_num = 0
    else:
        new_num = i - numbers_dict[curr_num] - 1
        numbers_dict[curr_num] = i - 1
        curr_num = new_num
    i += 1

finish = time.time()

print("time:", finish - start)

print(curr_num)

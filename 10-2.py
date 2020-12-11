with open("10-input.txt", "r") as f:
    nums = list(map(int, f.readlines()))

nums.append(0)
nums.sort()

current_paths = {0:1}
count = 0

while len(current_paths) > 0:
    curr = min(current_paths.keys())
    amount = current_paths.pop(curr)
    if curr == nums[-1]:
        count += amount
    else:
        for num in nums:
            if num > curr and num <= curr + 3:
                if num in current_paths.keys():
                    current_paths[num] += amount
                else:
                    current_paths[num] = amount

print(count)

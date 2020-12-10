with open("10-input.txt", "r") as f:
    nums = list(map(int, f.readlines()))

nums.append(0)
nums.sort()
# print(nums[-1])

current_paths = {0:1}
count = 0

while len(current_paths) > 0:
    # print(current_paths)
    curr = min(current_paths.keys())
    amount = current_paths.pop(curr)
    # print(curr, nums[-1])
    if curr == nums[-1]:
        count += amount
    else:
        for num in nums:
            if num > curr and num <= curr + 3:
                # print(curr, num)
                if num in current_paths.keys():
                    current_paths[num] += amount
                else:
                    current_paths[num] = amount

print(count)

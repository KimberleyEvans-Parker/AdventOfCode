with open("10-input.txt", "r") as f:
    nums = list(map(int, f.readlines()))

nums.append(0)
nums.sort()

num_1s = 0
num_3s = 1
for i in range(1, len(nums)):
    if nums[i] - 1 == nums[i - 1]:
        num_1s += 1
    elif nums[i] - 3 == nums[i - 1]:
        num_3s += 1

print(num_1s * num_3s)

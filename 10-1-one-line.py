with open("10-input.txt", "r") as f:
    nums = list(map(int, f.readlines()))

print(sum([1 for i in range(1, len(nums) + 1) if sorted(nums + [0])[i] - 1 == sorted(nums + [0])[i - 1]]) * (1 + sum([1 for i in range(1, len(nums) + 1) if sorted(nums + [0])[i] - 3 == sorted(nums + [0])[i - 1]])))

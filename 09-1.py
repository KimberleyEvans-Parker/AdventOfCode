with open("09-input.txt", "r") as f:
    nums = list(map(int, f.readlines()))


for i in range(25, len(nums)):
    valid = False
    for j in range(25):
        for k in range(j, 25):
            if nums[i] == nums[i - j - 1] + nums[i - k - 1]:
                valid = True
                break
        if valid: break
    if valid: continue
    print(nums[i])
    break
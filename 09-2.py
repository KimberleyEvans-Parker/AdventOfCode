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
    invalid_number = nums[i]
    break

start_pointer = 0
end_pointer = 1
while True:
    if sum(nums[start_pointer:end_pointer]) == invalid_number:
        print(min(nums[start_pointer:end_pointer]) + max(nums[start_pointer:end_pointer]))
        break
    elif sum(nums[start_pointer:end_pointer]) < invalid_number:
        end_pointer += 1
    else:
        start_pointer += 1
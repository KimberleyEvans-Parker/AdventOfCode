with open("02-1-input.txt", "r") as f:
    policies = f.readlines()

count = 0

for policy in policies:
    letter = policy.split()[1][0]
    index1, index2 = map(int, policy.split()[0].split("-"))
    code = policy.split()[-1]
    correct_policy = False
    if code[index1 - 1] == letter:
        correct_policy = not correct_policy
    if code[index2 - 1] == letter:
        correct_policy = not correct_policy
    if correct_policy:
        count += 1

print(count)
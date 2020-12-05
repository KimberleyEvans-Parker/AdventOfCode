with open("02-input.txt", "r") as f:
    policies = f.readlines()

count = 0

for policy in policies:
    letter = policy.split()[1][0]
    min_num, max_num = map(int, policy.split()[0].split("-"))
    code = policy.split()[-1]
    if code.count(letter) >= min_num and code.count(letter) <= max_num:
        count += 1

print(count)
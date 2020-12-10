with open("02-input.txt", "r") as f:
    policies = f.readlines()

count = 0

for policy in policies:
    letter = policy.split()[1][0]
    index1, index2 = map(int, policy.split()[0].split("-"))
    code = policy.split()[-1]
    if abs((code[index1 - 1] == letter) - (code[index2 - 1] == letter)): # xor
        count += 1

print(count)

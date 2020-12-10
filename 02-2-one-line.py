with open("02-input.txt", "r") as f:
    policies = f.readlines()

print(sum([1 for policy in policies if abs((policy.split()[-1][int(policy.split()[0].split("-")[0]) - 1] == policy.split()[1][0]) - (policy.split()[-1][int(policy.split()[0].split("-")[1]) - 1] == policy.split()[1][0]))]))
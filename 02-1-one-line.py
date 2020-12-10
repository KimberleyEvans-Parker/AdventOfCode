with open("02-input.txt", "r") as f:
    policies = f.readlines()

print(sum([1 for policy in policies if policy.split()[-1].count(policy.split()[1][0]) >= int(policy.split()[0].split("-")[0]) and policy.split()[-1].count(policy.split()[1][0]) <= int(policy.split()[0].split("-")[1])]))
with open("04-input.txt", "r") as f:
    credentials = f.readlines()

credentials = "".join(credentials).split("\n\n")
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0

for credential in credentials:
    credential = credential.split()
    fields = []
    valid = True
    for field in credential:
        fields.append(field.split(":")[0])
    for required_field in required_fields:
        if required_field not in fields:
            valid = False
            break
    if valid:
        count += 1

print(count)
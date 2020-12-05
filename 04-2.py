with open("04-input.txt", "r") as f:
    credentials = f.readlines()

credentials = "".join(credentials).split("\n\n")
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0

for credential in credentials:
    credential = credential.split()
    fields = {}
    valid = True
    for field in credential:
        fields[field.split(":")[0]] = field.split(":")[1]
    for required_field in required_fields:
        # print(fields)
        # print(list(fields.keys()))
        if required_field not in list(fields.keys()):
            valid = False
            break
    if not valid:
        continue
    if int(fields["byr"]) < 1920 or int(fields["byr"]) > 2002:
        continue
    if int(fields["iyr"]) < 2010 or int(fields["iyr"]) > 2020:
        continue
    if int(fields["eyr"]) < 2020 or int(fields["eyr"]) > 2030:
        continue
    height = fields["hgt"]
    if height[-2:] == "cm":
        if int(height[:-2]) < 150 or int(height[:-2]) > 193:
            continue
    elif height[-2:] == "in": 
        if int(height[:-2]) < 59 or int(height[:-2]) > 76:
            continue
    else:
        continue
    if fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    if len(fields["pid"]) != 9:
        continue
    if not fields["pid"].isdigit():
        continue
    hair = fields["hcl"]
    if len(hair) != 7:
        continue
    if hair[0] != "#":
        continue
    for i in range(1, 7):
        if hair[i] not in "0123456789abcdef":
            valid = False
    if valid:
        count += 1

print(count)
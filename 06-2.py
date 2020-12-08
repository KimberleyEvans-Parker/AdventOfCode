with open("06-input.txt", "r") as f:
    answers = f.readlines()


answers = "".join(answers).split("\n\n")

total = 0

for answer in answers:
    responses = answer.split("\n")
    for char in responses[0]:
        all_answered_yes = True
        for response in responses:
            if char not in response:
                all_answered_yes = False
                break
        if all_answered_yes:
            total += 1

print(total)
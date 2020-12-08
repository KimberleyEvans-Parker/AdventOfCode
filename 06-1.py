with open("06-input.txt", "r") as f:
    answers = f.readlines()


answers = "".join(answers).split("\n\n")

total = 0

for answer in answers:
    unique_answer = "".join(set(answer)).replace("\n", "")
    total += len(unique_answer)

print(total)
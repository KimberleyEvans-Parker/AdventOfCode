import numpy
with open("13-input.txt", "r") as f:
    _, bus_string = f.readlines()

buses = bus_string.strip().split(",")
         
def modInverse(num2, num1):
    inverse = 1
    while True:
        if (num1 * inverse) % num2 == 1:
            return inverse
        inverse += 1

product = 1
for num in buses:
    if num == "x": continue
    product *= int(num)

nums = []
modInverses = []
final_array = []
for i in range(len(buses)):
    if buses[i] == "x": continue
    num = (product // int(buses[i]))
    mi = modInverse(int(buses[i]), num)
    modInverses.append(mi)
    nums.append(num)
    final_array.append((int(buses[i]) - i) * num * mi)


print(sum(final_array) % product)
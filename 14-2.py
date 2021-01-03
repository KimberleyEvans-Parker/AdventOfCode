with open("14-input.txt", "r") as f:
    lines = f.readlines()

total = 0
address_dict = {}


for line in lines:
    if line.split()[0] == "mask":
        mask = line.split()[-1]
        mask = "".join(reversed(mask))
    else:
        address = int((line[line.find("[") + 1:line.find("]")]))
        value = int(line.split()[-1])
        reversed_binary_address = "".join(reversed(bin(address)[2:]))
        for i in range(len(mask)):
            if mask[i] == "0":
                continue
            if i >= len(reversed_binary_address):
                if mask[i] == "1":
                    address += 2 ** i
            elif mask[i] == "1" and reversed_binary_address[i] == "0":
                address += 2 ** i
            elif mask[i] == "X" and reversed_binary_address[i] == "1":
                address -= 2 ** i
        written_addresses = [address]
        for i in range(len(mask)):
            new_addresses = []
            if mask[i] =="X":
                for written_address in written_addresses:
                    new_addresses.append(written_address + 2 ** i)
            written_addresses.extend(new_addresses)
        for written_address in written_addresses:
            address_dict[written_address] = value

print(sum(address_dict.values()))

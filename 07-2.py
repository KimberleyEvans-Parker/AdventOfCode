with open("07-input.txt", "r") as f:
    rules = f.readlines()

rules_dict = {}

for rule in rules:
    rules_dict[rule[:rule.find(" bags contain ")]] = rule[rule.find(" bags contain ")+14:].strip().split(", ")

class Bag:
    def __init__(self, name):
        self.name = name
        self.inside_bags = []
        self.outside_bags = []
        self.count = None

    def addInsideBags(self, inside_bags):
        self.inside_bags = inside_bags

    def count_bags(self):
        if self.count: return self.count # if we've already calculated it, no need to recalculate
        count = 1 # to include the current bag
        for inside_bag in self.inside_bags:
            count += inside_bag[0] * inside_bag[1].count_bags()
        self.count = count
        return self.count

    def __repr__(self):
        return "Bag " + self.name

bags_dict = {}

for bag_name in rules_dict.keys():
    bags_dict[bag_name] = Bag(bag_name)

for bag_name in rules_dict.keys():
    if rules_dict[bag_name] != ["no other bags."]:
        inside_bags = [(int(inside_bag[:inside_bag.find(" ") + 1]), bags_dict[inside_bag[inside_bag.find(" ") + 1:inside_bag.rfind(" ")]]) for inside_bag in rules_dict[bag_name]]
        bags_dict[bag_name].addInsideBags(inside_bags)

print(bags_dict["shiny gold"].count_bags() - 1) # minus 1 to exclude the gold bag

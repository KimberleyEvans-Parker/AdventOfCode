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

    def addInsideBags(self, inside_bags):
        self.inside_bags = inside_bags
        for inside_bag in inside_bags:
            inside_bag.addOutsideBags(self)

    def addOutsideBags(self, outside_bag):
        self.outside_bags.append(outside_bag)

    def __repr__(self):
        return "Bag " + self.name

bags_dict = {}

for bag_name in rules_dict.keys():
    bags_dict[bag_name] = Bag(bag_name)

for bag_name in rules_dict.keys():
    if rules_dict[bag_name] != ["no other bags."]:
        inside_bags = [bags_dict[inside_bag[inside_bag.find(" ") + 1:inside_bag.rfind(" ")]] for inside_bag in rules_dict[bag_name]]
        bags_dict[bag_name].addInsideBags(inside_bags)

import copy
outer_bags = copy.copy(bags_dict["shiny gold"].outside_bags)
unchecked_bags = copy.copy(bags_dict["shiny gold"].outside_bags)

while len(unchecked_bags) != 0:
    next_bag = unchecked_bags.pop()
    outer_bags.extend(next_bag.outside_bags)
    unchecked_bags.extend(next_bag.outside_bags)

print(set(outer_bags))
print(len(set(outer_bags)))
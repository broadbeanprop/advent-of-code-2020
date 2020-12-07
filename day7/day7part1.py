import copy

with open('day7/input.txt', 'r') as file:
    rules = file.read().splitlines()

    def get_possible_outer_bags(bag):
        possible_outer_bags = []

        for rule in rules:
            rule_parts = rule.split(" contain ")

            outer_bag = str(rule_parts[0])
            inner_bags = rule_parts[1]

            if bag in inner_bags:
                index = outer_bag.find(" bag")
                bag_or_bags = len(outer_bag) - index
                bag_color = outer_bag[:-bag_or_bags]
                possible_outer_bags.append(bag_color)
        
        return possible_outer_bags

    all_possible_outer_bags = set()
    outer_bags = ["shiny gold"]

    while len(outer_bags) > 0:
        next_outer_bags = set()

        for bag in outer_bags:
            possible_outer_bags = get_possible_outer_bags(bag)
            
            for outer_bag in possible_outer_bags:
                all_possible_outer_bags.add(outer_bag)
                next_outer_bags.add(outer_bag)
        
        outer_bags = copy.copy(next_outer_bags)

    print("The amount of possible outer bags is: " + str(len(all_possible_outer_bags)))
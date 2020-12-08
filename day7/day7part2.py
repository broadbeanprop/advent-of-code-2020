with open('day7/input.txt', 'r') as file:
    rules = file.read().splitlines()

    def get_bag_color(bag):
        index = bag.find(" bag")
        bag_or_bags = len(bag) - index
        return bag[:-bag_or_bags]

    def get_inner_bags(bag):
        inner_bags = {}

        for rule in rules:
            rule_parts = rule.split(" contain ")

            outer_bag = str(rule_parts[0])

            if get_bag_color(outer_bag) != bag:
                continue

            inner_bags_line = rule_parts[1].split(", ")

            for inner_bag in inner_bags_line:
                if inner_bag == 'no other bags.':
                    continue

                inner_bag_parts = inner_bag.split(" ")
                amount = int(inner_bag_parts[0])
                color = get_bag_color(" ".join(inner_bag_parts[1:]))
                
                if inner_bags.get(color) == None:
                    inner_bags[color] = amount
                else:
                    inner_bags[color] += amount
        
        return inner_bags

    def loop(bag):
        amount = 0
        inner_bags = get_inner_bags(bag)

        for inner_bag in inner_bags:
            amount += (loop(inner_bag) + 1) * inner_bags[inner_bag]
        
        return amount
    
    total = loop("shiny gold")

    print("Total amount of bags: " + str(total))
import string


def get_priorities(items):

    total_priority = 0
    for item in items:
        if item.islower():
            total_priority = total_priority + string.ascii_lowercase.index(item) + 1
        elif item.isupper():
            total_priority = total_priority + string.ascii_uppercase.index(item) + 27

    return total_priority


def first_part():

    with open('data/input.txt', 'r') as inf:

        total_priorities = 0
        for r in inf:
            rucksack_size = len(r.strip())
            rucksack_half_size = int(rucksack_size/2)

            first_half = r[0:rucksack_half_size]
            second_half = r[rucksack_half_size:rucksack_size]

            same_in_both = list(set(first_half).intersection(set(second_half)))

            rucksack_priorities = get_priorities(same_in_both)
            total_priorities = total_priorities + rucksack_priorities

        print(total_priorities)


def second_part():

    with open('data/input.txt', 'r') as inf:

        total_priorities = 0
        rows = inf.readlines()
        for i in range(0, len(rows), 3):

            first_elf = set(rows[i].strip())
            second_elf = set(rows[i + 1].strip())
            third_elf = set(rows[i + 2].strip())

            shared_item = first_elf.intersection(second_elf).intersection(third_elf)

            shared_item_priority = get_priorities(shared_item)
            total_priorities = total_priorities + shared_item_priority

        print(total_priorities)

second_part()
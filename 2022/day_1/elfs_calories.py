

def get_elfs_calories(input_path):

    elfs = []
    with open(input_path, 'r') as inf:

        elf = {
            'id': 0,
            'calories': [],
            'calories_total': 0
        }

        rows = inf.readlines()

        for i, r in enumerate(rows):
            if r.strip() != '':
                elf['calories'].append(int(r.strip()))
            if r.strip() == '' or i == len(rows) - 1:
                elf['calories_total'] = sum(elf['calories'])
                elfs.append(elf.copy())
                elf['id'] = elf['id'] + 1
                elf['calories'] = []

        return elfs

def get_elf_most_calories(elfs_calories, top_elfs_count):

    elfs_calories_sorted = sorted(elfs_calories, key=lambda x: x['calories_total'], reverse=True)

    return elfs_calories_sorted[:top_elfs_count]

def get_total_calories(elfs_calories):

    return sum(ec['calories_total'] for ec in elfs_calories)


elfs_calories = get_elfs_calories('data/calories.csv')
elf_most_calories = get_elf_most_calories(elfs_calories, 1)
elf_top_3_calories = get_elf_most_calories(elfs_calories, 3)
elfs_total = get_total_calories(elf_top_3_calories)

print(elf_most_calories)
print(elf_top_3_calories)
print(elfs_total)

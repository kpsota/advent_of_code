
def section_id_to_numbers(section_id):

    numbers = list(range(int(section_id.split('-')[0]), int(section_id.split('-')[1]) + 1))
    return numbers


def overlap(set_a, set_b, overlap_condition):

    if overlap_condition == 'any' and (len(set_a.intersection(set_b)) > 0 or len(set_b.intersection(set_a)) > 0):
        return True
    elif overlap_condition == 'all' and (len(set_a.intersection(set_b)) == len(set_b) or len(set_b.intersection(set_a)) == len(set_a)):
        return True
    else:
        return False


def get_overlaped_sections(condition):

    with open('data/input.txt', 'r') as inf:

        rows = inf.readlines()
        total_overlaped_pairs = 0
        for r in rows:
            first_section_numbers = set(section_id_to_numbers(r.split(',')[0]))
            second_section_numbers = set(section_id_to_numbers(r.split(',')[1]))

            if overlap(first_section_numbers, second_section_numbers, condition):
                total_overlaped_pairs = total_overlaped_pairs + 1

        return total_overlaped_pairs


print(get_overlaped_sections('all'))
print(get_overlaped_sections('any'))

def get_marker(file, length):

    with open(file, 'r') as inf:
        datastream = inf.read().rstrip()
        current_marker = []
        for c in datastream:

            current_marker.append(c)
            if len(current_marker) == length and len(set(current_marker)) == length:
                return ''.join(current_marker)
            elif len(current_marker) == length and len(set(current_marker)) < length:
                current_marker.pop(0)

        return None


def get_position_after_marker(file, marker):

    with open(file, 'r') as inf:
        datastream = inf.read().rstrip()
        return datastream.index(marker) + len(marker)


# file = 'data/sample.txt'
file = 'data/input.txt'

# first part
marker = get_marker(file, 4)
print(marker)
print(get_position_after_marker(file, marker))

# second part
marker = get_marker(file, 14)
print(marker)
print(get_position_after_marker(file, marker))
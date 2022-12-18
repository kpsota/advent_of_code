from collections import deque
import string
import numpy as np

class Grid:

    def __init__(self, data):

        self.grid = data
        self.grid_np = np.array(data)
        self.start = self.get_char_coords('S')
        self.end = self.get_char_coords('E')

    def get_char_coords(self, char):

        xy = []
        for i, m in enumerate(self.grid):
            for j, n in enumerate(m):
                if n == char:
                    xy.append((j, i))

        return xy


    def get_bfs(self, start_xy, end_xy, start_end_elev):

        height = len(self.grid)
        width = len(self.grid[0])

        queue = deque([[start_xy]])
        seen = set([start_xy])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (x, y) == end_xy:
                return path
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:

                    from_char = self.grid[y][x]
                    to_char = self.grid[y2][x2]

                    #print('{} >>> {}'.format(from_char, to_char))

                    if from_char in start_end_elev.keys():
                        from_char = start_end_elev[from_char]
                    elif to_char in start_end_elev.keys():
                        to_char = start_end_elev[to_char]

                    # game rule - we can only ascend to the next letter
                    from_char_idx = string.ascii_lowercase.index(from_char)
                    to_char_idx = string.ascii_lowercase.index(to_char)
                    if to_char_idx - from_char_idx <= 1:
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))

        return []

def parse_input(path):

    data = []
    with open(path, 'r') as inf:
        for line in inf:
            data.append(list(line.strip()))

    return data


data = parse_input('data/input.txt')

grid = Grid(data)

start_end_elev = {
    'S': 'a',
    'E': 'z'
}

# part 1
start = grid.get_char_coords('S')[0]
end_point = grid.get_char_coords('E')[0]
path = grid.get_bfs(start, end_point, start_end_elev)
print(len(path) - 1)


# part 2
starts = grid.get_char_coords('a')
end_point = grid.get_char_coords('E')[0]

paths = []
for s in starts:
    path = grid.get_bfs(s, end_point, start_end_elev)
    paths.append({
            'start': s,
            #'path': path,
            'dist': len(path) - 1
        }
    )

print(sorted(filter(lambda x:x != - 1, [p['dist'] for p in paths]))[0])
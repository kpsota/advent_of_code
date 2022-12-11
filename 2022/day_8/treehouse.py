import numpy as np

def get_nearest_gte(trees, cur_tree):

    for i, n in enumerate(trees):
        if n >= cur_tree:
            return i + 1

    return len(trees)

def main(file):

    with open(file, 'r') as inf:
        trees_grid = []
        for line in inf:
            trees_grid.append(list(line.strip()))

    trees_grid_np = np.array(trees_grid)

    visible_trees = []
    distances = []
    for iy, ix in np.ndindex(trees_grid_np.shape):
        cur_tree = trees_grid_np[iy, ix]
        if iy == 0 or ix == 0 or iy == trees_grid_np.shape[0] - 1 or ix == trees_grid_np.shape[1] - 1:
            # edge tree
            visible_trees.append(cur_tree)
        else:
            left_trees = trees_grid_np[iy, :ix]
            right_trees = trees_grid_np[iy, ix+1:]
            bottom_trees = trees_grid_np[iy+1:, ix]
            upper_trees = trees_grid_np[:iy, ix]

            # part 1
            neighbors = [left_trees, right_trees, bottom_trees, upper_trees]
            for neighbor in neighbors:
                if all(n < cur_tree for n in neighbor):
                    visible_trees.append(cur_tree)
                    break

            # part 2
            cur_tree_dist = {
                'tree': [iy, ix],
                'left_gte': get_nearest_gte(np.flip(left_trees), cur_tree),
                'right_gte': get_nearest_gte(right_trees, cur_tree),
                'bottom_gte': get_nearest_gte(bottom_trees, cur_tree),
                'upper_gte': get_nearest_gte(np.flip(upper_trees), cur_tree)
            }
            cur_tree_dist['total_score'] = cur_tree_dist['left_gte'] * cur_tree_dist['right_gte'] * cur_tree_dist['bottom_gte'] * cur_tree_dist['upper_gte']
            distances.append(cur_tree_dist)

    print(len(visible_trees))
    print(max([d['total_score'] for d in distances]))


main('data/sample.txt')
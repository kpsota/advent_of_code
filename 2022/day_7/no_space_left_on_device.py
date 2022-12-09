import re

class Node:

    def __init__(self, name, filesize=0):

        self.name = name
        self.filesize = filesize
        self.totalsize = filesize
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):

        return str(self.get_as_dict())

    def get_as_dict(self):

        return {
            'name': self.name,
            'children': self.children,
            'filesize': self.filesize,
            'totalsize': self.totalsize
        }


def get_node(tree, node_name):

    if tree.name == node_name:
        yield tree
    else:
        for ch in tree.children:
            yield from get_node(ch, node_name)

def traverse_tree(tree, return_prop=None):

    if return_prop:
        yield getattr(tree, return_prop)
    else:
        yield tree
    for ch in tree.children:
        yield from traverse_tree(ch, return_prop)


def parse_dirs(lines):

    dirs = []
    dir_path = []
    for line in lines:
        line = line.strip()
        if line.startswith('$ cd') and line != '$ cd ..':
            dir_name = line.replace('$ cd', '').strip()
            dir_path.append(dir_name)
            cur_dir = {
                'dir_path': '/'.join(dir_path),
                'lines': []
            }
            dirs.append(cur_dir.copy())
        elif line == '$ cd ..' or (line.startswith('$ cd') and line != cur_dir['cd']):
            cur_dir['lines'] = []
            dir_path.pop()
        else:
            cur_dir['lines'].append(line)

    return dirs

def parsed_clean(dirs_parsed):

    dirs = []
    for dir in dirs_parsed:
        dirs.append({
            'name': dir['dir_path'],
            'subdirs': ['{}/{}'.format(dir['dir_path'], d.replace('dir ', '')) for d in dir['lines'] if d.startswith('dir')],
            'filesize': sum([int(re.findall(r'\d+', l)[0]) for l in dir['lines'] if l[0].isdigit()])
        })

    for dir in dirs:
        dir['subdirs'] = [{'name': d['name'], 'filesize': d['filesize']} for d in dirs if d['name'] in dir['subdirs']]

    return dirs

def get_dirs_tree(dirs):

    root = [d for d in dirs if d['name'] == '/'][0]
    tree = Node(root['name'], root['filesize'])

    for dir in dirs:
        node = next(get_node(tree, dir['name']))
        for sd in dir['subdirs']:
            node.add_child(Node(sd['name'], sd['filesize']))

    return tree

def main(file):

    with open(file, 'r') as inf:
        lines = inf.readlines()

        parsed = parse_dirs(lines)
        clean = parsed_clean(parsed)

        dirs_tree = get_dirs_tree(clean)

        # calc total sizes
        for node in traverse_tree(dirs_tree):
            node.totalsize = sum(traverse_tree(node, 'filesize'))

        # part 1
        # dirs_under_100k = list(filter(lambda x: x.totalsize <= 100000, traverse_tree(dirs_tree)))
        # print(sum([d.totalsize for d in dirs_under_100k]))

        # part 2
        used_space = sum(traverse_tree(dirs_tree, 'filesize'))
        cur_free_space = 70000000 - used_space
        space_needed = 30000000 - cur_free_space
        dirs_over_limit = list(filter(lambda x: x.totalsize >= space_needed, traverse_tree(dirs_tree)))
        dirs_over_limit_sorted = sorted(dirs_over_limit, key=lambda x: x.totalsize)
        for d in dirs_over_limit_sorted:
            print(d.name, d.totalsize)


main('data/input.txt')
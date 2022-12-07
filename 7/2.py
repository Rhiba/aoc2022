import sys

class DirNode:
    def __init__(self, dirname):
        self.dirname = dirname
        self.dirs = {}
        self.parent = None
        self.files = []
        self.total = 0

    def __repr__(self):
        return f"{self.dirname} {self.total} {self.files} ({self.dirs})"

def main(in_string):
    commands = in_string.splitlines()

    root = DirNode('/')
    current = root
    for command in commands:
        spl = command.split(" ")
        if spl[0] == '$':
            comm = spl[1]
            if comm == 'cd':
                loc = spl[2]
                if loc == '/':
                    current = root
                elif loc == '..':
                    current = current.parent
                else:
                    current = current.dirs[loc]
            elif comm == 'ls':
                pass
        elif spl[0] == 'dir':
            d = spl[1]
            d_node = DirNode(d)
            d_node.parent = current
            current.dirs[d] = d_node
        else:
            size = int(spl[0])
            name = spl[1]
            current.files.append((size,name))
            tmp = current
            while tmp:
                tmp.total += size
                tmp = tmp.parent

    current_free = 70000000 - root.total
    need_to_free = 30000000 - current_free

    to_check = [root]
    possibilities = []
    while len(to_check) > 0:
        curr = to_check.pop()
        if curr.total >= need_to_free:
            possibilities.append(curr.total)
        for k,v in curr.dirs.items():
            to_check.append(v)

    possibilities = sorted(possibilities)
    print(possibilities)
    print(possibilities[0])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

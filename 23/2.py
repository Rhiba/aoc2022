import sys

class Elf:
    def __init__(self):
        # 0 = north, 1 = south, 2 = west, 3 = easy
        self.consider = 0

    def __repr__(self):
        return f"(Next dir - {self.consider})"

def print_elves(elves):
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    elf_count = 0
    for y in elves.keys():
        for x in elves[y].keys():
            elf_count += 1
            if min_x is None or x < min_x:
                min_x = x
            if max_x is None or x > max_x:
                max_x = x
            if min_y is None or y < min_y:
                min_y = y
            if max_y is None or y > max_y:
                max_y = y
    grid = [['.' for x in range(min_x,max_x+1)] for y in range(min_y, max_y+1)]

    for y in elves.keys():
        for x in elves[y].keys():
            grid_y = y - min_y
            grid_x = x - min_x
            grid[grid_y][grid_x] = '#'

    for row in grid:
        print(''.join(row))

    print((len(grid)*len(grid[0]))-elf_count)
    print()

def main(in_string):
    elves = {}
    for y, line in enumerate(in_string.splitlines()):
        for x, entry in enumerate(line):
            if entry == '#':
                elf = Elf()
                if not y in elves:
                    elves[y] = {}
                elves[y][x] = elf


    rnd = 0
    noone_moved = False
    while not noone_moved:
        noone_moved = True
        moving_elves = []
        unmoving_elves = []
        for elfy in elves.keys():
            for elfx in elves[elfy].keys():
                elf = elves[elfy][elfx]
                moving = False
                for i in range(-1,2):
                    for j in range(-1,2):
                        if not (i==0 and j==0):
                            test_x = elfx + j
                            test_y = elfy + i
                            if test_y in elves and test_x in elves[test_y]:
                                moving = True
                                break
                    if moving:
                        break
                if moving:
                    moving_elves.append((elfx, elfy, elf))
                else:
                    unmoving_elves.append((elfx, elfy, elf))

        proposal = {}

        for (x,y,elf) in unmoving_elves:
            if not y in proposal:
                proposal[y] = {}
            proposal[y][x] = [(x,y,elf)]

        for (x,y,elf) in moving_elves:
            dir0 = [(-1,-1),(0,-1),(1,-1)]
            dir1 = [(-1,1),(0,1),(1,1)]
            dir2 = [(-1,-1),(-1,0),(-1,1)]
            dir3 = [(1,-1),(1,0),(1,1)]

            if elf.consider == 0:
                dirs = [dir0, dir1, dir2, dir3]
            elif elf.consider == 1:
                dirs = [dir1, dir2, dir3, dir0]
            elif elf.consider == 2:
                dirs = [dir2, dir3, dir0, dir1]
            else:
                dirs = [dir3, dir0, dir1, dir2]

            for d_set in dirs:
                can_move = True
                for d in d_set:
                    if d[1]+y in elves and d[0]+x in elves[d[1]+y]:
                        can_move = False
                if can_move:
                    to_move = d_set[1]
                    if not y+to_move[1] in proposal:
                        proposal[y+to_move[1]] = {}
                    if not x+to_move[0] in proposal[y+to_move[1]]:
                        proposal[y+to_move[1]][x+to_move[0]] = []
                    proposal[y+to_move[1]][x+to_move[0]].append((x,y,elf))
                    break

            if not can_move:
                if not y in proposal:
                    proposal[y] = {}
                if not x in proposal[y]:
                    proposal[y][x] = []
                
                proposal[y][x].append((x,y,elf))

        new_elves = {}
        for y in proposal.keys():
            for x in proposal[y].keys():
                if len(proposal[y][x]) == 1:
                    elf = proposal[y][x][0][2]
                    if not y in new_elves:
                        new_elves[y] = {}
                    new_elves[y][x] = elf
                    if not (proposal[y][x][0][0] == x and proposal[y][x][0][1] == y):
                        noone_moved = False
                else:
                    for old_elf in proposal[y][x]:
                        old_y = old_elf[1]
                        old_x = old_elf[0]
                        old_elf_atom = old_elf[2]
                        if not old_y in new_elves:
                            new_elves[old_y] = {}
                        new_elves[old_y][old_x] = old_elf_atom

        elves = new_elves
        for y in elves.keys():
            for x in elves[y].keys():
                elves[y][x].consider = 0 if elves[y][x].consider == 3 else elves[y][x].consider + 1

        rnd += 1

    print_elves(elves)
    print(rnd)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

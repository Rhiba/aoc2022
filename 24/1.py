import sys

class Blizzard:
    def __init__(self, face):
        self.face = face

    def __repr__(self):
        return f"(Facing: {self.face})"

    def __eq__(self, other):
        if self.face == other.face:
            return True
        return False

def main(in_string):
    grid = []
    blizzards = {}
    start = None
    finish = None
    for idy, line in enumerate(in_string.splitlines()):
        grid_line = []
        for idx, entry in enumerate(line):
            if idy == 0 and entry =='.':
                start = (idx,idy)

            if idy == len(in_string.splitlines())-1 and entry == '.':
                finish = (idx, idy)

            face = None
            if entry == '^':
                face = 0
            elif entry == '>':
                face = 1
            elif entry == 'v':
                face = 2
            elif entry == '<':
                face = 3

            if face is not None:
                if idy not in blizzards:
                    blizzards[idy] = {}
                blizzards[idy][idx] = [Blizzard(face)]

            if entry == '#':
                to_add = '#'
            else:
                to_add = '.'

            grid_line.append(to_add)
        grid.append(grid_line)

    end = len(grid[0])
    width = len(grid[0])-2
    height = len(grid)-2
    top = len(grid)

    timestep_blizzards = []
    timestep_blizzards.append(blizzards)
    for timestep in range(width*height):
        new_blizzards = {}
        last_blizzards = timestep_blizzards[-1]
        for y in last_blizzards.keys():
            for x in last_blizzards[y].keys():
                for blizz in last_blizzards[y][x]:
                    if blizz.face == 0:
                        new_x = x
                        if y-1 < 1:
                            new_y = top-2
                        else:
                            new_y = y-1
                    elif blizz.face == 1:
                        new_y = y
                        if x+1 > end-2:
                            new_x = 1
                        else:
                            new_x = x+1
                    elif blizz.face == 2:
                        new_x = x
                        if y+1 > top-2:
                            new_y = 1
                        else:
                            new_y = y+1
                    else:
                        new_y = y
                        if x-1 < 1:
                            new_x = end-2
                        else:
                            new_x = x-1

                    if not new_y in new_blizzards:
                        new_blizzards[new_y] = {}
                    if not new_x in new_blizzards[new_y]:
                        new_blizzards[new_y][new_x] = []
                    new_blizzards[new_y][new_x].append(blizz)

        timestep_blizzards.append(new_blizzards)

    print("finished processing blizzards")
    # x, y, timestep, mins
    to_explore = [(start[0], start[1], 0, 0)]
    count = -1
    while len(to_explore) > 0:
        count += 1
        x, y, timestep, mins = to_explore.pop(0)
        if count % 100 == 0:
            print(x,y,timestep,mins)

        if x == finish[0] and y == finish[1]:
            print(mins)
            break
        # get blizzards at next timestep
        blizzards = timestep_blizzards[(timestep+1) % (width*height)]
        # stay
        if not (y in blizzards and x in blizzards[y]):
            new_state = (x, y, timestep+1, mins+1)
            if new_state not in to_explore:
                to_explore.append(new_state)

        # go up
        if not (y-1 in blizzards and x in blizzards[y-1]) and grid[y-1][x] == '.':
            new_state = (x, y-1, timestep+1, mins+1)
            if new_state not in to_explore:
                to_explore.append(new_state)

        # go down
        if not (y+1 in blizzards and x in blizzards[y+1]) and grid[y+1][x] == '.':
            new_state = (x, y+1, timestep+1, mins+1)
            if new_state not in to_explore:
                to_explore.append(new_state)

        # go left
        if not (y in blizzards and x-1 in blizzards[y]) and grid[y][x-1] == '.':
            new_state = (x-1, y, timestep+1, mins+1)
            if new_state not in to_explore:
                to_explore.append(new_state)

        # go right
        if not (y in blizzards and x+1 in blizzards[y]) and grid[y][x+1] == '.':
            new_state = (x+1, y, timestep+1, mins+1)
            if new_state not in to_explore:
                to_explore.append(new_state)

        to_explore = sorted(to_explore, key=lambda x: x[3])
        



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

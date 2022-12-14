import sys

def main(in_string):

    min_x = None
    max_x = None
    min_y = None
    max_y = None

    for line in in_string.splitlines():
        splt = line.split(' -> ')
        for s in splt:
            x = int(s.split(',')[0])
            y = int(s.split(',')[1])
            if min_x == None or x < min_x:
                min_x = x
            if max_x == None or x > max_x:
                max_x = x
            if min_y == None or y < min_y:
                min_y = y
            if max_y == None or y > max_y:
                max_y = y

    if 500 > max_x:
        max_x = 500
    if 500 < min_x:
        min_x = 500

    if 0 < min_y:
        min_y = 0
    if 0 > max_y:
        max_y = 0

    grid_width = max_x - min_x + 1
    grid_height = max_y - min_y + 1

    grid = [['.' for i in range(grid_width)] for j in range(grid_height)]

    source_x = 500-min_x
    source_y = 0 - min_y
    grid[source_y][source_x] = '+'

    for line in in_string.splitlines():
        splt = line.split(' -> ')
        for i in range(len(splt)-1):
            start = [int(c) for c in splt[i].split(',')]
            start = [start[0]-min_x, start[1]-min_y]
            end = [int(c) for c in splt[i+1].split(',')]
            end = [end[0]-min_x, end[1]-min_y]
            if abs(start[0]-end[0]) > 0:
                # change in x
                index = 0
            else:
                # change in y
                index = 1
            if start[index] < end[index]:
                s = start[index]
                e = end[index]
            else:
                s = end[index]
                e = start[index]
            for k in range(s, e+1):
                if index == 0:
                    grid[start[1]][k] = '#'
                else:
                    grid[k][start[0]] = '#'
    print_grid(grid)
    print()

    endless = False
    stationary = 0
    while not endless:
        sand = [source_x,source_y]
        moving = True
        while moving:
            if sand[1] == len(grid)-1:
                moving = False
                endless = True
            elif grid[sand[1]+1][sand[0]] == '.':
                sand = [sand[0],sand[1]+1]
            elif sand[0] == 0:
                moving = False
                endless = True
            elif grid[sand[1]+1][sand[0]-1] == '.':
                sand = [sand[0]-1,sand[1]+1]
            elif sand[0] == len(grid[0]) - 1:
                moving = False
                endless = True
            elif grid[sand[1]+1][sand[0]+1] == '.':
                sand = [sand[0]+1,sand[1]+1]
            else:
                moving = False
                grid[sand[1]][sand[0]] = 'o'
                stationary += 1

    print_grid(grid)
    print(stationary)


def print_grid(grid):
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

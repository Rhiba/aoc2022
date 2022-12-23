import sys
import numpy as np

def main(in_string):
    split = in_string.split('\n\n')
    grid_str = split[0].splitlines()
    instructions_str = split[1].strip()

    instructions = []
    gather = ''
    for i in instructions_str:
        if i.isnumeric():
            gather += i
        else:
            if gather != '':
                instructions.append(gather)
                gather = ''
            instructions.append(i)
    if gather != '':
        instructions.append(gather)

    max_row_len = max([len(x) for x in grid_str])
    grid = []
    #min_max[row] = (min, max)
    min_max_row = {}
    for idx,g in enumerate(grid_str):
        g = list(g)
        if '#' in g and '.' in g:
            first_idx = min(g.index('.'),g.index('#'))
            last_idx = len(g)-min(g[::-1].index('.'),g[::-1].index('#'))-1
        elif '.' in g:
            first_idx = g.index('.')
            last_idx = len(g)-g[::-1].index('.')-1
        elif '#' in g:
            first_idx = g.index('#')
            last_idx = len(g)-g[::-1].index('#')-1

        min_max_row[idx] = (first_idx,last_idx)
        if len(g) < max_row_len:
            g += [' ' for i in range(max_row_len-len(g))]
        grid.append(g)

    transposed = np.transpose(grid)
    min_max_col = {}
    for idx, g in enumerate(transposed):
        g = list(g)
        if '#' in g and '.' in g:
            first_idx = min(g.index('.'),g.index('#'))
            last_idx = len(g)-min(g[::-1].index('.'),g[::-1].index('#'))-1
        elif '.' in g:
            first_idx = g.index('.')
            last_idx = len(g)-g[::-1].index('.')-1
        elif '#' in g:
            first_idx = g.index('#')
            last_idx = len(g)-g[::-1].index('#')-1

        min_max_col[idx] = (first_idx,last_idx)

    pos = (min_max_row[0][0],min_max_col[min_max_row[0][0]][0])

    # 0 = north, 1 = east, 2 = south 3 = west
    face = 1

    for ins in instructions:
        if ins.isnumeric():
            move = int(ins)
            if face == 0:
                while move > 0:
                    new_x = pos[0]
                    if pos[1]-1 < min_max_col[new_x][0]:
                        new_y = min_max_col[new_x][1]
                    else:
                        new_y = pos[1]-1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x,new_y)
                    move -= 1
                
            elif face == 1:
                while move > 0:
                    new_y = pos[1]
                    if pos[0]+1 > min_max_row[new_y][1]:
                        new_x = min_max_row[new_y][0]
                    else:
                        new_x = pos[0]+1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x, new_y)
                    move -= 1

            elif face == 2:
                while move > 0:
                    new_x = pos[0]
                    if pos[1]+1 > min_max_col[new_x][1]:
                        new_y = min_max_col[new_x][0]
                    else:
                        new_y = pos[1]+1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x,new_y)
                    move -= 1

            elif face == 3:
                while move > 0:
                    new_y = pos[1]
                    if pos[0]-1 < min_max_row[new_y][0]:
                        new_x = min_max_row[new_y][1]
                    else:
                        new_x = pos[0]-1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x, new_y)
                    move -= 1

        else:
            if ins == 'R':
                if face == 3:
                    face = 0
                else:
                    face += 1
            elif ins == 'L':
                if face == 0:
                    face = 3
                else:
                    face -= 1

    print(pos[1]+1, pos[0]+1, face-1 if face > 0 else 3)
    print((1000*(pos[1]+1)) + (4*(pos[0]+1)) + (face-1 if face > 0 else 3))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read()
            main(in_string)

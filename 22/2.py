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
    egde_match = {}
    grid = []
    
    for g in grid_str:
        g = list(g)
        if len(g) < max_row_len:
            g += [' ' for i in range(max_row_len-len(g))]
        grid.append(g)

    square_size = 50
    # up right down left
    square_conns = {}
    if square_size == 4:
        square_conns[0] = [[1, 0, 2], [5, 1, 3],[3, 0, 2], [2, 0, 2]]
        square_conns[1] = [[0, 0, 2], [2, 3, 1],[4, 2, 0], [5, 2, 0]]
        square_conns[2] = [[0, 3, 1], [3, 3, 1],[4, 3, 1], [1, 1, 3]]
        square_conns[3] = [[0, 2, 0], [5, 0, 2],[4, 0, 2], [2, 1, 3]]
        square_conns[4] = [[3, 2, 0], [5, 3, 1],[1, 2, 0], [2, 2, 0]]
        square_conns[5] = [[3, 1, 3], [0, 1, 3],[1, 3, 1], [4, 1, 3]]
    else:
        square_conns[0] = [[5, 3, 1], [1, 3, 1], [2, 0, 2], [3, 3, 1]]
        square_conns[1] = [[5, 2, 0],[4, 1, 3],[2, 1, 3],[0, 1, 3]]
        square_conns[2] = [[0, 2, 0],[1, 2, 0],[4, 0, 2],[3, 0, 2]]
        square_conns[3] = [[2, 3, 1],[4, 3, 1],[5, 0, 2],[0, 3, 1]]
        square_conns[4] = [[2, 2, 0],[1, 1, 3],[5, 1, 3],[3, 1, 3]]
        square_conns[5] = [[3, 2, 0],[4, 2, 0],[1, 0, 2],[0, 0, 2]]

    square_boundaries = {}

    square_id = 0
    for idy,row in enumerate(grid):
        if idy % square_size == 0:
            # read all squares from this row
            first_index = 0
            while first_index < len(row):
                subset = []
                bad = False
                for i in range(square_size):
                    part = grid[idy+i][first_index:first_index+square_size]
                    if ' ' in part:
                        bad = True
                        break
                if not bad:
                    square_boundaries[square_id] = (first_index, first_index+square_size-1, idy, idy+square_size-1)
                    square_id += 1
                first_index += square_size

    pos = (square_boundaries[0][0],square_boundaries[0][2])

    # 0 = north, 1 = east, 2 = south 3 = west
    face = 1

    for ins in instructions:
        if ins.isnumeric():
            move = int(ins)
            while move > 0:
                if face == 0:
                    new_x = pos[0]
                    square = is_within(pos[0],pos[1],square_boundaries)
                    new_face = face
                    if pos[1]-1 < square_boundaries[square][2]:
                        rel_x = pos[0] - square_boundaries[square][0]
                        conn_square = square_conns[square][0][0]
                        #print(f"out of {square}, into {conn_square}")
                        conn_side = square_conns[square][0][1]
                        new_face = square_conns[square][0][2]
                        new_bound = square_boundaries[conn_square]
                        if conn_side == 0:
                            new_y = new_bound[2]
                            new_x = new_bound[1] - rel_x
                        elif conn_side == 1:
                            new_y = new_bound[3] - rel_x
                            new_x = new_bound[1]
                        elif conn_side == 2:
                            new_y = new_bound[3]
                            new_x = new_bound[0] + rel_x
                        else:
                            new_y = new_bound[2] + rel_x
                            new_x = new_bound[0]
                    else:
                        new_y = pos[1]-1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x,new_y)
                        face = new_face
                        #print("new pos:", pos, "new face:", face)
                    
                elif face == 1:
                    new_y = pos[1]
                    square = is_within(pos[0],pos[1],square_boundaries)
                    new_face = face
                    if pos[0]+1 > square_boundaries[square][1]:
                        rel_y = pos[1] - square_boundaries[square][2]
                        conn_square = square_conns[square][1][0]
                        #print(f"out of {square}, into {conn_square}")
                        conn_side = square_conns[square][1][1]
                        new_face = square_conns[square][1][2]
                        new_bound = square_boundaries[conn_square]
                        if conn_side == 0:
                            new_y = new_bound[2]
                            new_x = new_bound[1] - rel_y
                        elif conn_side == 1:
                            new_x = new_bound[1]
                            new_y = new_bound[3] - rel_y
                        elif conn_side == 2:
                            new_y = new_bound[3]
                            new_x = new_bound[0] + rel_y
                        else:
                            new_x = new_bound[0]
                            new_y = new_bound[2] + rel_y
                    else:
                        new_x = pos[0]+1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x,new_y)
                        face = new_face
                        #print("new pos:", pos, "new face:", face)

                elif face == 2:
                    new_x = pos[0]
                    square = is_within(pos[0],pos[1],square_boundaries)
                    new_face = face
                    if pos[1]+1 > square_boundaries[square][3]:
                        rel_x = pos[0] - square_boundaries[square][0]
                        conn_square = square_conns[square][2][0]
                        #print(f"out of {square}, into {conn_square}")
                        conn_side = square_conns[square][2][1]
                        new_face = square_conns[square][2][2]
                        new_bound = square_boundaries[conn_square]
                        if conn_side == 0:
                            new_y = new_bound[2]
                            new_x = new_bound[0] + rel_x
                        elif conn_side == 1:
                            new_y = new_bound[2] + rel_x
                            new_x = new_bound[1]
                        elif conn_side == 2:
                            new_y = new_bound[3]
                            new_x = new_bound[1] - rel_x
                        else:
                            new_y = new_bound[3] - rel_x
                            new_x = new_bound[0]
                    else:
                        new_y = pos[1]+1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x,new_y)
                        face = new_face
                        #print("new pos:", pos, "new face:", face)

                elif face == 3:
                    new_y = pos[1]
                    square = is_within(pos[0],pos[1],square_boundaries)
                    new_face = face
                    if pos[0]-1 < square_boundaries[square][0]:
                        rel_y = pos[1] - square_boundaries[square][2]
                        conn_square = square_conns[square][3][0]
                        #print(f"out of {square}, into {conn_square}")
                        conn_side = square_conns[square][3][1]
                        new_face = square_conns[square][3][2]
                        new_bound = square_boundaries[conn_square]
                        if conn_side == 0:
                            new_y = new_bound[2]
                            new_x = new_bound[0] + rel_y
                        elif conn_side == 1:
                            new_x = new_bound[1]
                            new_y = new_bound[2] + rel_y
                        elif conn_side == 2:
                            new_y = new_bound[3]
                            new_x = new_bound[1] - rel_y
                        else:
                            new_x = new_bound[0]
                            new_y = new_bound[3] - rel_y
                    else:
                        new_x = pos[0]-1
                    if grid[new_y][new_x] == '#':
                        break
                    else:
                        pos = (new_x,new_y)
                        face = new_face
                        #print("new pos:", pos, "new face:", face)
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
        #print(pos, face)

    print(pos[1]+1, pos[0]+1, face-1 if face > 0 else 3)
    print((1000*(pos[1]+1)) + (4*(pos[0]+1)) + (face-1 if face > 0 else 3))

def is_within(x,y,square_boundaries):
    for square, bound in square_boundaries.items():
        if x >= bound[0] and x <= bound[1] and y >= bound[2] and y <= bound[3]:
            return square
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read()
            main(in_string)

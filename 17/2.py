import sys
from collections import OrderedDict

def main(in_string):
    jets = in_string
    high_point = -1

    block = '█'

    log = [['█', '█', '█', '█']]
    plus = [['.', '█', '.'],
            ['█', '█', '█'],
            ['.', '█', '.']]
    ell = [['.', '.', '█'],
           ['.', '.', '█'],
           ['█', '█', '█']]
    vlog = [['█'],
            ['█'],
            ['█'],
            ['█']]
    square = [['█', '█'],
              ['█', '█']]

    shapes = [log, plus, ell, vlog, square]

    room = [['.' for i in range(7)]]
    top_3_rows = OrderedDict({})
    indexes = []

    counter = 0
    push_counter = 0
    iterations = 70000
    loop_end = None
    loop_start = None
    loop_idx = None
    loop_start_height = None
    loop_end_height = None
    loop_heights = {}
    while counter < iterations:
        shape_num = counter % 5
        shape = shapes[shape_num]
        
        # investigating

        x = 2
        y = high_point + 3 + (len(shape))

        if y >= len(room):
            expand = (y+1)-len(room)
            for e in range(expand):
                room.append(['.' for i in range(7)])

        falling = True
        while falling:
            push_num = push_counter % len(jets)
            push = jets[push_num]
            # push first
            is_blocked_lr = False
            for idy, row in enumerate(shape):
                y_val = y - idy
                first_idx = row.index(block)
                last_idx = len(row) - 1 - row[::-1].index(block)
                lhs = x + first_idx
                rhs = x + last_idx
                if push == '<':
                    if lhs-1 < 0:
                        is_blocked_lr = True
                    else:
                        if room[y_val][lhs-1] == block:
                            is_blocked_lr = True
                elif push == '>':
                    if rhs+1 >= len(room[0]):
                        is_blocked_lr = True
                    else:
                        if room[y_val][rhs+1] == block:
                            is_blocked_lr = True

            if not is_blocked_lr:
                if push == '<':
                    x -= 1
                elif push == '>':
                    x += 1

            # now move downwards
            is_blocked_down = False

            for idy, row in enumerate(shape):
                for idx, entry in enumerate(row):
                    if entry == block:
                        y_val = y - idy
                        x_val = x + idx
                        if y_val - 1 < 0:
                            is_blocked_down = True
                        else:
                            if room[y_val-1][x_val] == block:
                                is_blocked_down = True
            if not is_blocked_down:
                y -= 1
            else:
                falling = False
                if shape_num == 0:
                    old_high = high_point
                for idy, row in enumerate(shape):
                    for idx, entry in enumerate(row):
                        if entry == block:
                            y_val = y - idy
                            x_val = x + idx
                            room[y_val][x_val] = block
                            if y_val > high_point:
                                high_point = y_val

                if shape_num == 0:
                    top_rows = get_top_n_rows(room,3)
                    key = str(top_rows)+" "+str(push_num)
                    if not key in top_3_rows:
                        top_3_rows[key] = 0
                    top_3_rows[key] += 1
                    idex = list(top_3_rows.keys()).index(key)
                    if loop_end == None or idex > loop_end:
                        loop_end = idex
                    if len(indexes) > 0 and idex < indexes[-1]:
                        loop_start = idex
                    indexes.append(idex)
                    loop_idx = idex
                    loop_start_height = old_high
                    diff = y-old_high
                if shape_num == 4:
                    loop_end_height = high_point
                    diff_height = loop_end_height - loop_start_height
                    loop_heights[loop_idx] = diff_height
            push_counter += 1
        
        counter += 1
    print()
    print(high_point+1)
    print(top_3_rows)
    print(loop_start, loop_end)
    print(loop_heights)

    num_loops = int(1000000000000/5)
    diff_loops = loop_end-loop_start+1
    print(num_loops % diff_loops)
    all_reps = (num_loops - loop_start)// diff_loops
    extra = (num_loops -loop_start)% diff_loops
    print(all_reps, extra)

    height = 0
    for i in range(loop_start):
        height += loop_heights[i]

    for i in range(loop_start, loop_end+1):
        height += (all_reps * loop_heights[i])
        if i - loop_start < extra:
            height += loop_heights[i]

    print(height)


def is_top_flat(room):
    for row in room[::-1]:
        if '█' in row:
            if not '.' in row:
                return True
        else:
            return False

def get_top_n_rows(room,n):
    count = 0
    ret = []
    for row in room[::-1]:
        if '█' in row:
            ret.append(row)
            count += 1
        if count > n:
            break
    return ret
    

def print_shape(shape):
    for row in shape:
        print(''.join(row))

def print_room(room):
    for row in room[::-1]:
        print(''.join(row))

def print_top_n(room,n):
    for idx, row in enumerate(room[::-1]):
        if idx < n:
            print(''.join(row))
        else:
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

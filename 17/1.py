import sys

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

    counter = 0
    push_counter = 0
    while counter < 2022:
        shape_num = counter % 5
        shape = shapes[shape_num]


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
            push_counter += 1
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
                for idy, row in enumerate(shape):
                    for idx, entry in enumerate(row):
                        if entry == block:
                            y_val = y - idy
                            x_val = x + idx
                            room[y_val][x_val] = block
                            if y_val > high_point:
                                high_point = y_val
        
        counter += 1
    print_room(room)
    print()
    print(high_point)

def print_shape(shape):
    for row in shape:
        print(''.join(row))

def print_room(room):
    for row in room[::-1]:
        print(''.join(row))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

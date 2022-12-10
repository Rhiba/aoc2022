
import sys

def main(in_string):
    ops = in_string.splitlines()

    cycle = 0
    cycles_left_for_op = 0 if ops[0].startswith('noop') else 1
    cycle_values = []
    op_ptr = 0
    xreg = 1
    crt = [' ' for i in range(240)]
    while op_ptr < len(ops):
        cycle += 1
        idx = (cycle-1) % 40
        if idx in [xreg-1, xreg, xreg+1]:
            crt[cycle-1] = '█'

        if cycles_left_for_op == 0:
            # if the previous was a addx
            if ops[op_ptr].startswith('add'):
                value = int(ops[op_ptr].split(' ')[1])
                xreg += value

            op_ptr += 1
            if op_ptr < len(ops) and ops[op_ptr].startswith('add'):
                cycles_left_for_op = 1
        else:
            cycles_left_for_op -= 1

    for i in range(6):
        start = 40*i
        end = (40*i) + 40
        print(''.join(crt[start:end]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

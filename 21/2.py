from z3 import *
import sys

def main(in_string):
    monkeys = {}
    for line in in_string.splitlines():
        split = line.split(' ')
        monkey = split[0][:-1]
        oper = ' '.join(split[1:])
        monkeys[monkey] = oper

    monkeys['root'] = monkeys['root'].split(' ')[0] + " " + "==" + " " + monkeys['root'].split(' ')[2]
    cons = get_res('root', monkeys)
    solve(cons)

def get_res(monkey, monkey_list):
    oper_str = monkey_list[monkey]
    split = oper_str.split(' ')
    left = split[0]
    right = split[2]
    oper = split[1]
    if monkey_list[left].isnumeric():
        if left != 'humn':
            left_val = IntVal(int(monkey_list[left]))
        else:
            left_val = Int('humn')
    else:
        left_val = get_res(left, monkey_list)

    if monkey_list[right].isnumeric():
        if right != 'humn':
            right_val = IntVal(int(monkey_list[right]))
        else:
            right_val = Int('humn')
    else:
        right_val = get_res(right, monkey_list)

    if oper == '==':
        return left_val == right_val
    elif oper == '+':
        return left_val + right_val
    elif oper == '-':
        return left_val - right_val
    elif oper == '*':
        return left_val * right_val
    elif oper == '/':
        return left_val / right_val


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

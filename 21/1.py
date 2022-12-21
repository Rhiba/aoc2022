
import sys

def main(in_string):
    monkeys = {}
    for line in in_string.splitlines():
        split = line.split(' ')
        monkey = split[0][:-1]
        oper = ' '.join(split[1:])
        monkeys[monkey] = oper

    val = get_res('root', monkeys)
    print(val)

def get_res(monkey, monkey_list):
    oper_str = monkey_list[monkey]
    split = oper_str.split(' ')
    left = split[0]
    right = split[2]
    oper = split[1]
    if monkey_list[left].isnumeric():
        left_val = int(monkey_list[left])
    else:
        left_val = get_res(left, monkey_list)

    if monkey_list[right].isnumeric():
        right_val = int(monkey_list[right])
    else:
        right_val = get_res(right, monkey_list)

    return eval(f"{left_val} {oper} {right_val}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

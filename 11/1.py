import sys

def main(in_string):
    monkeys = in_string.split('Monkey ')[1:]
    items = {}
    ops = {}
    test = {}
    dest = {}
    counts = {}
    for monkey in monkeys:
        lines = monkey.splitlines()
        num = int(lines[0][:-1])
        counts[num] = 0
        item_list = [int(x) for x in ''.join(lines[1].strip().split(' ')[2:]).split(',')]
        items[num] = item_list
        op_op = lines[2].split(' ')[-2]
        op_num = lines[2].split(' ')[-1]
        if not op_num == 'old':
            op_num = int(op_num)

        ops[num] = [op_op, op_num]
        div_num = int(lines[3].split(' ')[-1])
        test[num] = div_num

        dest_true = int(lines[4].split(' ')[-1])
        dest_false = int(lines[5].split(' ')[-1])

        dest[num] = {}
        dest[num][True] = dest_true
        dest[num][False] = dest_false

    for i in range(20):
        for monkey in items.keys():
            for j in range(len(items[monkey])):
                worry_level = items[monkey].pop(0)
                counts[monkey] += 1
                op_op, op_num = ops[monkey]
                if op_num == 'old':
                    op_num = worry_level
                if op_op == '*':
                    result = worry_level * op_num
                else:
                    result = worry_level + op_num

                print(result)
                worry_level = result // 3
                print(worry_level)
                print()
                if worry_level % test[monkey] == 0:
                    branch = True
                else:
                    branch = False
                d = dest[monkey][branch]
                items[d].append(worry_level)

    vals = sorted(list(counts.values()), reverse=True)
    print(vals[0]*vals[1])





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

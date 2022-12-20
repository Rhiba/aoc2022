import sys

class Number:
    def __init__(self, idx, number):
        self.idx = idx
        self.number = number
        self.next = None
        self.prev = None
        self.origin_next = None
        self.start = False

    def __repr__(self):
        return f"(Idx: {self.idx}, Num: {self.number}, Link: {True if self.next else False})"

def main(in_string):
    numbers = [int(x) for x in in_string.splitlines()]

    idx_to_num = {}
    for i in range(len(numbers)):
        num = Number(i,numbers[i])
        idx_to_num[i] = num
        if num.number == 0:
            zero_num = num
        if i > 0:
            idx_to_num[i-1].next = num
            idx_to_num[i-1].origin_next = num
            num.prev = idx_to_num[i-1]

    idx_to_num[0].start = True
    idx_to_num[0].prev = idx_to_num[len(idx_to_num.keys())-1]
    idx_to_num[len(idx_to_num.keys())-1].next = idx_to_num[0]
    zero = idx_to_num[0]
    current_node = zero

    while current_node is not None:
        to_move = current_node.number
        if not to_move == 0:
            # yoink out and join prev to next
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            new_current = current_node

            if current_node.start:
                current_node.start = False
                next_node.start = True
                zero = next_node

            for i in range(abs(to_move)):
                if to_move > 0:
                    new_current = new_current.next
                else:
                    new_current = new_current.prev

            # if going negative, skip one more time because we always place in next
            if to_move < 0:
                new_current = new_current.prev

            # replace just after new_current
            new_next = new_current.next
            new_current.next = current_node
            new_next.prev = current_node
            current_node.next = new_next
            current_node.prev = new_current

        current_node = current_node.origin_next

    numbers = [zero.number]
    next_node = zero.next
    while not next_node.start:
        numbers.append(next_node.number)
        next_node = next_node.next

    zero_idx = numbers.index(0)
    numbers = numbers[zero_idx:] + numbers[:zero_idx]

    thousand_idx = 1000%len(numbers)
    twothousand_idx = 2000%len(numbers)
    threethousand_idx = 3000%len(numbers)


    print(numbers[thousand_idx]+ numbers[twothousand_idx]+ numbers[threethousand_idx])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

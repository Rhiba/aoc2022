
import sys

def main(in_string):
    pairs = in_string.split("\n\n")
    correct_indices = []

    for idx,pair in enumerate(pairs):
        pair1 = eval(pair.splitlines()[0])
        pair2 = eval(pair.splitlines()[1])
        correct = comp_list(pair1, pair2)
        if correct == 2:
            correct_indices.append(idx+1)

    print(sum(correct_indices))

def comp_list(list1, list2):
    '''
    Returns 0 = wrong, 1 = check next, 2 = correct
    '''
    if isinstance(list1, int) and isinstance(list2, int):
        if list1 < list2:
            return 2
        elif list2 < list1:
            return 0
        else:
            return 1
    elif isinstance(list1, int) and isinstance(list2, list):
        list1 = [list1]
    elif isinstance(list2, int) and isinstance(list1, list):
        list2 = [list2]

    if len(list1) == 0 and len(list2) == 0:
        return 1
    elif len(list1) == 0 and len(list2) > 0:
        return 2
    elif len(list2) == 0 and len(list1) > 0:
        return 0
    else:
        for i in range(min(len(list1), len(list2))):
            var1 = list1[i]
            var2 = list2[i]
            res = comp_list(var1, var2)
            if res == 0 or res == 2:
                return res

        if len(list1) < len(list2):
            size = len(list1)
            return comp_list([],list2[size:])
        else:
            size = len(list2)
            return comp_list(list1[size:],[])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

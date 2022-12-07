
import sys
import string

def main(in_string):
    contents = in_string.splitlines()
    groups = int(len(contents)/3)

    running_total = 0
    for g in range(groups):
        si = g*3
        e1 = set(contents[si])
        e2 = set(contents[si+1])
        e3 = set(contents[si+2])

        included = list(e1.intersection(e2).intersection(e3))[0]

        tot = string.ascii_lowercase.index(included.lower())
        if included.isupper():
            tot += 26
        tot += 1
        running_total += tot

    print(running_total)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

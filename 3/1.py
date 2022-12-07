
import sys
import string

def main(in_string):
    contents = in_string.splitlines()
    running_total = 0
    for rucksack in contents:
        size = int(len(rucksack)/2)
        comp1 = set(rucksack[:size])
        comp2 = set(rucksack[size:])
        both = list(comp1.intersection(comp2))[0]
        tot = string.ascii_lowercase.index(both.lower())
        if both.isupper():
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

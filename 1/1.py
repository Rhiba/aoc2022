
import sys

def main(in_string):
    per_elf = in_string.split("\n\n")
    high = 0
    for pe in per_elf:
        amounts = pe.split("\n")
        amounts = [int(a) for a in amounts]
        tot = sum(amounts)
        if tot > high:
            high = tot
    print(high)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

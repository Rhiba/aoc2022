
import sys

def main(in_string):
    for i in range(len(in_string)-14):
        chunk = in_string[i:i+14]
        if len(set(chunk)) == len(chunk):
            print(i+14)
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

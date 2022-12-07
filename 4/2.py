
import sys

def main(in_string):
    assigns = in_string.splitlines()
    inside_c = 0
    for ass_str in assigns:
        spl = ass_str.split(",")
        sec0 = (int(spl[0].split('-')[0]), int(spl[0].split('-')[1]))
        sec1 = (int(spl[1].split('-')[0]), int(spl[1].split('-')[1]))
        if overlaps(sec0, sec1):
            inside_c += 1

    print(inside_c)

def overlaps(inner, outer):
    in1 = inner[0]
    in2 = inner[1]
    out1 = outer[0]
    out2 = outer[1]
    if (in1 >= out1 and in1 <= out2) or (in2 >= out1 and in2 <= out2) or (out1 >= in1 and out1 <= in2) or (out2 >= in1 and out2 <= in2):
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

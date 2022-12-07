
import sys

def main(in_string):
    stack_lines = in_string.split("\n\n")[0].split("\n")
    stack_lines = stack_lines[::-1]

    move_lines = in_string.split("\n\n")[1].strip().split("\n")
    stacks = []
    for idx,line in enumerate(stack_lines):
        line += ' '
        num_chunks = len(line) // 4
        chunks = []
        for ch in range(num_chunks):
            chunk = line[ch*4:(ch*4)+4]
            chunk = chunk.strip()
            chunks.append(chunk)

        if idx == 0:
            for ch in chunks:
                stacks.append([])
        else:
            for idy,ch in enumerate(chunks):
                if len(ch) > 0:
                    stacks[idy].append(ch)

    for mv in move_lines:
        split = mv.split(" ")
        count = int(split[1])
        source = int(split[3])
        dest = int(split[5])

        popped = stacks[source-1][-count:]
        stacks[source-1] = stacks[source-1][:-count]
        stacks[dest-1] += popped

    for s in stacks:
        print(s[-1][1],end="")
    print()



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read()
            main(in_string)

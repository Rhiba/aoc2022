
import sys

def main(in_string):
    head = [0,0]
    tail = [0,0]
    covered = [[0,0]]
    for pair in in_string.splitlines():
        spl = pair.split(' ')
        direction = spl[0]
        dist = int(spl[1])
        for i in range(dist):
            if direction == 'R':
                head = [head[0]+1,head[1]] 
            elif direction == 'L':
                head = [head[0]-1,head[1]] 
            elif direction == 'U':
                head = [head[0],head[1]+1] 
            elif direction == 'D':
                head = [head[0],head[1]-1] 

            x_diff = head[0]-tail[0]
            y_diff = head[1]-tail[1]
            
            if abs(x_diff) == 2:
                # if negative move left/down
                sign_lr = 1 if x_diff > 0 else -1
                sign_ud = 1 if y_diff > 0 else -1
                if abs(y_diff) == 0:
                    tail = [tail[0]+sign_lr, tail[1]]
                elif abs(y_diff) == 1:
                    tail = [tail[0]+sign_lr, tail[1]+sign_ud]
                else:
                    print("UH OH")
                if not tail in covered:
                    covered.append(tail)

            elif abs(y_diff) == 2:
                sign_lr = 1 if x_diff > 0 else -1
                sign_ud = 1 if y_diff > 0 else -1
                if abs(x_diff) == 0:
                    tail = [tail[0], tail[1]+sign_ud]
                elif abs(x_diff) == 1:
                    tail = [tail[0]+sign_lr, tail[1]+sign_ud]
                else:
                    print("UH OH")
                if not tail in covered:
                    covered.append(tail)
    print(len(covered))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

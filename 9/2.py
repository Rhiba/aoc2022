
import sys

def main(in_string):
    knots = [[0,0] for i in range(10)]
    covered = [[0,0]]
    for pair in in_string.splitlines():
        spl = pair.split(' ')
        direction = spl[0]
        dist = int(spl[1])
        for i in range(dist):
            if direction == 'R':
                knots[0] = [knots[0][0]+1,knots[0][1]] 
            elif direction == 'L':
                knots[0] = [knots[0][0]-1,knots[0][1]] 
            elif direction == 'U':
                knots[0] = [knots[0][0],knots[0][1]+1] 
            elif direction == 'D':
                knots[0] = [knots[0][0],knots[0][1]-1] 

            for j in range(1,len(knots)):
                x_diff = knots[j-1][0]-knots[j][0]
                y_diff = knots[j-1][1]-knots[j][1]
                
                if abs(x_diff) == 2:
                    # if negative move left/down
                    sign_lr = 1 if x_diff > 0 else -1
                    sign_ud = 1 if y_diff > 0 else -1
                    if abs(y_diff) == 0:
                        knots[j] = [knots[j][0]+sign_lr, knots[j][1]]
                    elif abs(y_diff) == 1 or abs(y_diff) == 2:
                        knots[j] = [knots[j][0]+sign_lr, knots[j][1]+sign_ud]
                    else:
                        print("UH OH")

                elif abs(y_diff) == 2:
                    sign_lr = 1 if x_diff > 0 else -1
                    sign_ud = 1 if y_diff > 0 else -1
                    if abs(x_diff) == 0:
                        knots[j] = [knots[j][0], knots[j][1]+sign_ud]
                    elif abs(x_diff) == 1 or abs(x_diff) == 2:
                        knots[j] = [knots[j][0]+sign_lr, knots[j][1]+sign_ud]
                    else:
                        print("UH OH")
            if not knots[-1] in covered:
                covered.append(knots[-1])

    print(len(covered))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

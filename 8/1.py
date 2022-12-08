
import sys

def main(in_string):
    grid = [[int(x) for x in y] for y in in_string.splitlines()]
    visible = 0
    for idy, row in enumerate(grid):
        for idx, entry in enumerate(row):
            #check up
            seen_up = True
            for i in range(1,idy+1):
                if grid[idy-i][idx] >= entry:
                    seen_up = False
            if seen_up:
                visible += 1
                continue

            seen_down = True
            for i in range(1,len(grid)-idy):
                if grid[idy+i][idx] >= entry:
                    seen_down = False
            if seen_down:
                visible += 1
                continue

            seen_right = True
            for i in range(1,idx+1):
                if grid[idy][idx-i] >= entry:
                    seen_right = False
            if seen_right:
                visible += 1
                continue

            seen_left = True
            for i in range(1,len(grid[0])-idx):
                if grid[idy][idx+i] >= entry:
                    seen_left = False
            if seen_left:
                visible += 1

    print(visible)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

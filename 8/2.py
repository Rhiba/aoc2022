
import sys

def main(in_string):
    grid = [[int(x) for x in y] for y in in_string.splitlines()]
    visible = 0
    max_scenic = 0
    for idy, row in enumerate(grid):
        for idx, entry in enumerate(row):
            score_up = 0
            for i in range(1,idy+1):
                if grid[idy-i][idx] >= entry:
                    score_up += 1
                    break
                else:
                    score_up += 1

            score = score_up

            score_down = 0
            for i in range(1,len(grid)-idy):
                if grid[idy+i][idx] >= entry:
                    score_down += 1
                    break
                else:
                    score_down += 1
            score *= score_down

            score_right = 0
            for i in range(1,idx+1):
                if grid[idy][idx-i] >= entry:
                    score_right += 1
                    break
                else:
                    score_right += 1
            score *= score_right

            score_left = 0
            for i in range(1,len(grid[0])-idx):
                if grid[idy][idx+i] >= entry:
                    score_left += 1
                    break
                else:
                    score_left += 1

            score *= score_left

            if score > max_scenic:
                max_scenic = score

    print(max_scenic)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

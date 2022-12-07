import sys

def main(in_string):
    rounds = in_string.splitlines()
    rounds = [(a.split(" ")[0],a.split(" ")[1]) for a in rounds]
    beats = {'A':'Z', 'B':'X', 'C':'Y'}
    equals = {'A':'X', 'B':'Y', 'C':'Z'}
    scores = {'X':1, 'Y':2, 'Z':3}
    score = 0
    for r in rounds:
        win_score = None
        if beats[r[0]] == r[1]:
            win_score = 0
        elif equals[r[0]] == r[1]:
            win_score = 3
        else:
            win_score = 6
        score += (win_score + scores[r[1]])
    print(score)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

import sys

def main(in_string):
    rounds = in_string.splitlines()
    rounds = [(a.split(" ")[0],a.split(" ")[1]) for a in rounds]
    beats = {'C':'B', 'A':'C', 'B':'A'}
    looses = {'B':'C', 'C':'A', 'A':'B'}
    scores = {'A':1, 'B':2, 'C':3}
    score = 0
    for r in rounds:
        win_score = None
        if r[1] == 'Z':
            win_score = 6
            item_score = scores[looses[r[0]]]
        elif r[1] == 'Y':
            win_score = 3
            item_score = scores[r[0]]
        else:
            win_score = 0
            item_score = scores[beats[r[0]]]
        score += (win_score + item_score)
        print(r[0], r[1])
        print(win_score, item_score)
        print()
    print(score)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

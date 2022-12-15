import sys

def main(in_string):
    sensors = {}
    beacons = set()
    sensors_alone = set()
    min_x = None
    max_x = None
    for line in in_string.splitlines():
        first = line.split(': ')[0]
        second = line.split(': ')[1]
        sensor_x = int(first.split(' ')[2][:-1].split('=')[1])
        sensor_y = int(first.split(' ')[3].split('=')[1])

        beacon_x = int(second.split(' ')[4][:-1].split('=')[1])
        beacon_y = int(second.split(' ')[5].split('=')[1])

        dist = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)

        if sensor_x not in sensors:
            sensors[sensor_x] = {}

        beacons.add((beacon_x, beacon_y))
        sensors_alone.add((sensor_x, sensor_y))

        sensors[sensor_x][sensor_y] = [beacon_x, beacon_y, dist]
        if min_x is None or sensor_x-dist < min_x:
            min_x = sensor_x-dist

        if max_x is None or sensor_x+dist > max_x:
            max_x = sensor_x+dist

    #val = 20
    val = 4000000
    coords = None

    x = 0
    y = 0
    break_all = False
    while y < val:
        x = 0
        # progress
        if y % 10000 == 0:
            print(y)
        while x < val:
            found = False
            for s in sensors_alone:
                if abs(x-s[0]) + abs(y-s[1]) <= sensors[s[0]][s[1]][2]:
                    new_x = s[0] + (sensors[s[0]][s[1]][2]-abs(y-s[1]))
                    x = new_x
                    found = True
                    break
            if found == False:
                coords = (x,y)
                break_all = True
            if break_all:
                break
            x += 1
        if break_all:
            break
        y += 1


    print(coords)
    print((coords[0]*4000000)+coords[1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

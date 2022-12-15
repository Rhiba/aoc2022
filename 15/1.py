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

    val = 2000000
    #val=10
    count = 0

    # Attempt 2
    stuff_on_line = 0
    for b in beacons:
        if b[1] == val:
            stuff_on_line += 1
    for s in sensors_alone:
        if s[1] == val:
            stuff_on_line += 1

    i = min_x

    while i < max_x + 1:

        if (i,val) in beacons or (i,val) in sensors_alone:
            pass
        else:
            for s in sensors_alone:
                if abs(i-s[0]) + abs(val-s[1]) <= sensors[s[0]][s[1]][2]:
                    new_i = s[0] + (sensors[s[0]][s[1]][2]-abs(val-s[1]))
                    diff = new_i - i
                    count += diff + 1
                    i = new_i
                    break

        i += 1
    print(count-stuff_on_line)

    """
    # Attempt 1
    for i in range(min_x, max_x+1):
        if (i,val) in beacons or (i,val) in sensors_alone:
            pass
        else:
            for s in sensors_alone:
                if abs(i-s[0]) + abs(val-s[1]) <= sensors[s[0]][s[1]][2]:
                    count += 1
                    break
    print(count)
    """


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

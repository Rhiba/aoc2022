import sys

def main(in_string):

    surface_area = 0
    cube_list = []

    for cube in in_string.splitlines():
        split = cube.split(',')
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        surface_area += 6
        for other_cube in cube_list:
            if manhat((x,y,z), other_cube) == 1:
                surface_area -= 2
        cube_list.append((x,y,z))

    print(surface_area)
        

def manhat(cube1, cube2):
    ret = 0
    for dim in range(len(cube1)):
        ret += abs(cube1[dim]-cube2[dim])

    return ret



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

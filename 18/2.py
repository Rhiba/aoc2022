import sys

def main(in_string):

    surface_area = 0
    cube_list = []
    low_x = None
    high_x = None
    low_y = None
    high_y = None
    low_z = None
    high_z = None

    for cube in in_string.splitlines():
        split = cube.split(',')
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        if low_x is None or x < low_x:
            low_x = x
        if high_x is None or x > high_x:
            high_x = x
        if low_y is None or y < low_y:
            low_y = y
        if high_y is None or y > high_y:
            high_y = y
        if low_z is None or z < low_z:
            low_z = z
        if high_z is None or z > high_z:
            high_z = z

        surface_area += 6
        for other_cube in cube_list:
            if manhat((x,y,z), other_cube) == 1:
                surface_area -= 2
        cube_list.append((x,y,z))

    print(surface_area)
    air_pockets = []
    for x in range(low_x,high_x+1):
        for y in range(low_y, high_y+1):
            for z in range(low_z, high_z+1):
                if (x,y,z) not in cube_list and (x,y,z) not in air_pockets:
                    # potentially a new air pocket
                    new_surface_area, new_pocket = get_floodfill_and_sa(cube_list, (x,y,z), (low_x, high_x, low_y, high_y, low_z, high_z))
                    if new_surface_area > 0:
                        air_pockets += new_pocket
                        surface_area -= new_surface_area

    print(surface_area)



def get_floodfill_and_sa(cube_list,cube,limits):

    pocket = [cube]
    finished_pocket = []
    finished = False
    print("limits",limits)
    while not finished:
        to_check = pocket.pop(0)
        c_x = to_check[0]
        c_y = to_check[1]
        c_z = to_check[2]
        if (c_x-1, c_y, c_z) not in pocket and (c_x-1, c_y, c_z) not in finished_pocket and (c_x-1, c_y, c_z) not in cube_list and c_x-1 >= limits[0]:
            pocket.append((c_x-1,c_y,c_z))
        elif c_x-1 < limits[0]:
            return 0, []

        if (c_x+1, c_y, c_z) not in pocket and (c_x+1, c_y, c_z) not in finished_pocket and (c_x+1, c_y, c_z) not in cube_list and c_x+1 <= limits[1]:
            pocket.append((c_x+1,c_y,c_z))
        elif c_x+1 > limits[1]:
            return 0, []

        if (c_x, c_y-1, c_z) not in pocket and (c_x, c_y-1, c_z) not in finished_pocket and (c_x, c_y-1, c_z) not in cube_list and c_y-1 >= limits[2]:
            pocket.append((c_x,c_y-1,c_z))
        elif c_y-1 < limits[2]:
            return 0, []

        if (c_x, c_y+1, c_z) not in pocket and (c_x, c_y+1, c_z) not in finished_pocket and (c_x, c_y+1, c_z) not in cube_list and c_y+1 <= limits[3]:
            pocket.append((c_x,c_y+1,c_z))
        elif c_y+1 > limits[3]:
            return 0, []

        if (c_x, c_y, c_z-1) not in pocket and (c_x, c_y, c_z-1) not in finished_pocket and (c_x, c_y, c_z-1) not in cube_list and c_z-1 >= limits[4]:
            pocket.append((c_x,c_y,c_z-1))
        elif c_z-1 < limits[4]:
            return 0, []

        if (c_x, c_y, c_z+1) not in pocket and (c_x, c_y, c_z+1) not in finished_pocket and (c_x, c_y, c_z+1) not in cube_list and c_z+1 <= limits[5]:
            pocket.append((c_x,c_y,c_z+1))
        elif c_z+1 > limits[5]:
            return 0, []

        finished_pocket.append(to_check)
        if len(pocket) == 0:
            finished = True

    sa = get_sa(finished_pocket)
    return sa, finished_pocket

def get_sa(cube_list):
    recorded_list = []
    surface_area = 0
    for cube in cube_list:
        x = cube[0]
        y = cube[1]
        z = cube[2]

        surface_area += 6
        for other_cube in recorded_list:
            if manhat((x,y,z), other_cube) == 1:
                surface_area -= 2
        recorded_list.append((x,y,z))

    return surface_area
        

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

import sys
import string
import networkx as nx

def main(in_string):
    grid = in_string.splitlines()
    new_grid = []
    G = nx.DiGraph()
    for y, row in enumerate(grid):
        entries = []
        for x, entry in enumerate(row):
            node = (y*len(grid[0]))+x
            G.add_node(node)
            if entry == 'S':
                height = 0
            elif entry == 'E':
                height = 27
            else:
                height = string.ascii_lowercase.index(entry) + 1

            entries.append(height)
        new_grid.append(entries)

    grid = new_grid
    '''
    for r in grid:
        print(r)
    print()
    '''

    start = None
    end = None
    for y, row in enumerate(grid):
        for x, entry in enumerate(row):
            node = (y*len(grid[0]))+x
            if entry == 0:
                start = node
            elif entry == 27:
                end = node

            if y-1 >= 0:
                if grid[y-1][x] - entry <= 1:
                    connect_node = ((y-1)*len(grid[0]))+x
                    G.add_edge(node,connect_node)
            if y+1 < len(grid):
                if grid[y+1][x] - entry <= 1:
                    connect_node = ((y+1)*len(grid[0]))+x
                    G.add_edge(node,connect_node)
            if x-1 >= 0:
                if grid[y][x-1] - entry <= 1:
                    connect_node = (y*len(grid[0]))+(x-1)
                    G.add_edge(node,connect_node)
            if x+1 < len(grid[0]):
                if grid[y][x+1] - entry <= 1:
                    connect_node = (y*len(grid[0]))+(x+1)
                    G.add_edge(node,connect_node)

    path = nx.shortest_path(G, start,end)
    print(path)
    print(len(path)-1)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

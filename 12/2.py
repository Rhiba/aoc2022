import sys
import string
import networkx as nx

def main(in_string):
    grid = in_string.splitlines()
    new_grid = []
    G = nx.DiGraph()
    starts = []
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

            if height == 0 or height == 1:
                starts.append(node)

            entries.append(height)
        new_grid.append(entries)

    grid = new_grid

    end = None
    for y, row in enumerate(grid):
        for x, entry in enumerate(row):
            node = (y*len(grid[0]))+x
            if entry == 27:
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


    path_lens = []
    for s in starts:
        try:
            # hacky way of not caring if there is no path between that
            # particular start and the end
            path = nx.shortest_path(G, s,end)
            path_lens.append(len(path)-1)
        except:
            pass
    path_lens = sorted(path_lens)
    print(path_lens[0])




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

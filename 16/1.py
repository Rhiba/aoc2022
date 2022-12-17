import sys
import networkx as nx

def main(in_string):
    
    G = nx.Graph()
    for line in in_string.splitlines():
        spl = line.split('; ')
        valve = spl[0].split(' ')[1]
        flow_rate = int(spl[0].split(' ')[4].split('=')[1])
        G.add_node(valve, flow_rate=flow_rate)

        leading_to = spl[1].split(' ')[4:]
        for lt in leading_to:
            if lt.endswith(','):
                lt = lt[:-1]
            G.add_edge(valve,lt)

    count = 0
    minutes = 30

    path_from_to = {}
    max_dist = 0
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 not in path_from_to:
                path_from_to[n1] = {}
            path_from_to[n1][n2] = nx.shortest_path(G,n1,n2)
            l = len(path_from_to[n1][n2])
            if l > max_dist:
                max_dist = l

    to_explore = [('AA', 0, [], 0)]
    best = None
    best_at = {}
    # build a new graph of highest gain
    while len(to_explore) > 0:
        entry = to_explore.pop(0)
        current_node = entry[0]
        current_step = entry[1]
        activated = entry[2]
        current_pressure = entry[3]

        if best is None or current_pressure > best[1]:
            best = (entry, current_pressure)

        if current_step == minutes:
            continue

        if current_pressure < best[1] and current_step >= best[0][1] + max_dist:
            continue

        pressure_gains = []
        for node in G.nodes():
            path = path_from_to[current_node][node]
            steps = len(path)-1
            # factor in activation cost
            steps += 1
            if node not in activated:
                generation = (minutes - current_step - steps)*G.nodes[node]['flow_rate']
            else:
                generation = 0

            if generation > 0:
                pressure_gains.append((node,steps,generation))

        for pg in pressure_gains:
            pressure = current_pressure + pg[2]
            new_entry = (pg[0], current_step + pg[1], activated + [pg[0]], pressure)
            to_explore.append(new_entry)

        if count % 1000 == 0:
            to_explore = sorted(to_explore, reverse=True, key=lambda x: x[3])

        count += 1

    print(best[0])
    print(best[1])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

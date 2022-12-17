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
    minutes = 26

    path_from_to = {}
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 not in path_from_to:
                path_from_to[n1] = {}
            path_from_to[n1][n2] = nx.shortest_path(G,n1,n2)

    to_explore = [('AA','AA', 0, 0, [], 0)]
    best = None
    best_for_activated = {}
    # build a new graph of highest gain
    while len(to_explore) > 0:
        entry = to_explore.pop(0)
        me_node = entry[0]
        ele_node = entry[1]
        me_step = entry[2]
        ele_step = entry[3]
        activated = sorted(entry[4])
        current_pressure = entry[5]

        if str(activated) in best_for_activated:
            if current_pressure < best_for_activated[str(activated)]:
                continue
            else:
                best_for_activated[str(activated)] = current_pressure
        else:
            best_for_activated[str(activated)] = current_pressure

        if best is None or current_pressure > best[1]:
            best = (entry, current_pressure)
            print("new best")
            print(best)
            print()

        """
        if current_step == minutes:
            continue

        if current_pressure < best[1] and current_step >= best[0][1]:
            continue
        """
        pressure_gains_me = []
        pressure_gains_ele = []
        for node in G.nodes():
            me_path = path_from_to[me_node][node]
            ele_path = path_from_to[ele_node][node]
            me_steps = len(me_path)-1
            ele_steps = len(ele_path)-1
            # factor in activation cost
            me_steps += 1
            ele_steps += 1
            if node not in activated:
                me_generation = (minutes - me_step - me_steps)*G.nodes[node]['flow_rate']
                ele_generation = (minutes - ele_step - ele_steps)*G.nodes[node]['flow_rate']
            else:
                me_generation = 0
                ele_generation = 0

            if me_generation > 0:
                pressure_gains_me.append((node,me_steps,me_generation))

            if ele_generation > 0:
                pressure_gains_ele.append((node,ele_steps,ele_generation))


        for ide, pg_m in enumerate(pressure_gains_me):
            for pg_e in pressure_gains_ele:
                if not pg_m[0] == pg_e[0]:
                    new_me_node = pg_m[0]
                    new_me_step = me_step + pg_m[1]
                    new_ele_node = pg_e[0]
                    new_ele_step = ele_step + pg_e[1]
                    new_activated = activated + [pg_m[0], pg_e[0]]
                    new_pressure = current_pressure + pg_m[2] + pg_e[2]
                    new_entry = (new_me_node, new_ele_node, new_me_step, new_ele_step, new_activated, new_pressure)
                    to_explore.append(new_entry)

        if len(pressure_gains_me) == 0:
            for pg_e in pressure_gains_ele:
                # add ele gain and me stationary
                new_me_node = me_node
                new_me_step = me_step
                new_ele_node = pg_e[0]
                new_ele_step = ele_step + pg_e[1]
                new_activated = activated + [pg_e[0]]
                new_pressure = current_pressure + pg_e[2]
                new_entry = (new_me_node, new_ele_node, new_me_step, new_ele_step, new_activated, new_pressure)
                to_explore.append(new_entry)

        if len(pressure_gains_ele) == 0:
            for pg_m in pressure_gains_me:
                # add me gain and ele stationary
                new_me_node = pg_m[0]
                new_me_step = me_step + pg_m[1]
                new_ele_node = ele_node
                new_ele_step = ele_step
                new_activated = activated + [pg_m[0]]
                new_pressure = current_pressure + pg_m[2]
                new_entry = (new_me_node, new_ele_node, new_me_step, new_ele_step, new_activated, new_pressure)
                to_explore.append(new_entry)

        if count % 1000 == 0:
            to_explore = sorted(to_explore, reverse=True, key=lambda x: (x[5],-(x[2]+x[3])))

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

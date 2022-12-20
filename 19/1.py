import sys

class State:
    def __init__(self, ore_rbs, clay_rbs, obs_rbs, geode_rbs, ore, clay, obs, geode, minute):
        self.ore_rbs = ore_rbs
        self.clay_rbs = clay_rbs
        self.obs_rbs = obs_rbs
        self.geode_rbs = geode_rbs
        self.ore = ore
        self.clay = clay
        self.obs = obs
        self.geode = geode
        self.minute = minute

    def __eq__(self, other):
        if self.ore_rbs == other.ore_rbs and self.clay_rbs == other.clay_rbs and self.obs_rbs == other.obs_rbs and self.geode_rbs == other.geode_rbs and self.ore == other.ore and self.clay == other.clay and self.obs == other.obs and self.geode == other.geode and self.minute == other.minute:
            return True
        return False

    def __repr__(self):
        return f"(Ore rbs: {self.ore_rbs}, Clay rbs: {self.clay_rbs}, Obs rbs: {self.obs_rbs}, Geode rbs: {self.geode_rbs} -- Ore: {self.ore}, Clay: {self.clay}, Obs: {self.obs}, Geodes: {self.geode} -- Minute: {self.minute})"

class Blueprint:
    def __init__(self, ore_cost, clay_cost, obs_cost, geode_cost):
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obs_cost = obs_cost
        self.geode_cost = geode_cost

    def __repr__(self):
        return f"(Ore robot: {self.ore_cost}, Clay robot: {self.clay_cost}, Obs robot: {self.obs_cost}, Geode robot: {self.geode_cost})"

def main(in_string):
    # (ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost)
    # ((4), (2), (3, 14), (2, 7))
    blueprints = []
    for line in in_string.splitlines():
        split = line.split('Each ')
        ore_robot_cost = int(split[1].split(' ')[3])
        clay_robot_cost = int(split[2].split(' ')[3])
        obsidian_robot_cost = (int(split[3].split(' ')[3]), int(split[3].split(' ')[6]))
        geode_robot_cost = (int(split[4].split(' ')[3]), int(split[4].split(' ')[6]))
        bp = Blueprint(ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost)
        blueprints.append(bp)

    overall_max_geodes = []

    for bp in blueprints:
        print(bp)
        top_ore = max(bp.ore_cost, bp.clay_cost, bp.obs_cost[0], bp.geode_cost[0])
        top_clay = bp.obs_cost[1]
        top_obs = bp.geode_cost[1]
        init_state = State(1,0,0,0,0,0,0,0,0)
        to_explore = [init_state]
        max_geodes = 0
        count = 0
        best = None
        best_at = {}
        obs_geode_best_at = {}
        while len(to_explore) > 0:
            state = to_explore.pop(0)

            if state.minute >= 24:
                if state.geode > max_geodes:
                    max_geodes = state.geode
                    print(state)
                    print(max_geodes)
                continue

            if state.geode + ((24-state.minute)*state.geode_rbs) + ((24-state.minute)*(24-state.minute+1))/2 < max_geodes:
                continue

            can_make_ore_rbs = False
            can_make_clay_rbs = False
            can_make_obs_rbs = False
            can_make_geode_rbs = False

            if state.ore_rbs > 0 and state.clay_rbs > 0:
                if state.obs >= ((24-state.minute)*top_obs)-((24-state.minute)*state.obs_rbs):
                    pass
                else:
                    can_make_obs_rbs = True
            if state.ore_rbs > 0:
                if state.ore >= ((24-state.minute)*top_ore)-((24-state.minute)*state.ore_rbs):
                    pass

                else:
                    can_make_ore_rbs = True

                if state.clay >= ((24-state.minute)*top_clay)-((24-state.minute)*state.clay_rbs):
                    pass
                else:
                    can_make_clay_rbs = True

            if state.ore_rbs > 0 and state.obs_rbs > 0:
                can_make_geode_rbs = True

            if can_make_ore_rbs:
                if state.ore >= bp.ore_cost:
                    # already have enough
                    time_inc = 1
                else:
                    sim_val = state.ore
                    time_inc = 1
                    while sim_val < bp.ore_cost:
                        time_inc += 1
                        sim_val += state.ore_rbs
                if state.minute + time_inc < 24:
                    new_state = State(state.ore_rbs+1, state.clay_rbs, state.obs_rbs, state.geode_rbs, state.ore - bp.ore_cost + (time_inc*state.ore_rbs), state.clay + (time_inc*state.clay_rbs), state.obs + (time_inc*state.obs_rbs), state.geode + (time_inc*state.geode_rbs), state.minute + time_inc)
                    to_explore.append(new_state)
                else:
                    potential_geodes = state.geode + ((24-state.minute)*state.geode_rbs)
                    if potential_geodes > max_geodes:
                        max_geodes = potential_geodes
                        print(state)
                        print(max_geodes)

            if can_make_clay_rbs:
                if state.ore >= bp.clay_cost:
                    # already have enough
                    time_inc = 1
                else:
                    sim_val = state.ore
                    time_inc = 1
                    while sim_val < bp.clay_cost:
                        time_inc += 1
                        sim_val += state.ore_rbs
                if state.minute + time_inc < 24:
                    new_state = State(state.ore_rbs, state.clay_rbs+1, state.obs_rbs, state.geode_rbs, state.ore - bp.clay_cost + (time_inc*state.ore_rbs), state.clay + (time_inc*state.clay_rbs), state.obs + (time_inc*state.obs_rbs), state.geode + (time_inc*state.geode_rbs), state.minute + time_inc)
                    to_explore.append(new_state)
                else:
                    potential_geodes = state.geode + ((24-state.minute)*state.geode_rbs)
                    if potential_geodes > max_geodes:
                        max_geodes = potential_geodes
                        print(state)
                        print(max_geodes)

            if can_make_obs_rbs:
                if state.ore >= bp.obs_cost[0] and state.clay >= bp.obs_cost[1]:
                    # already have enough
                    time_inc = 1
                else:
                    sim_val_ore = state.ore
                    sim_val_clay = state.clay
                    time_inc = 1
                    while sim_val_ore < bp.obs_cost[0] or sim_val_clay < bp.obs_cost[1]:
                        time_inc += 1
                        sim_val_ore += state.ore_rbs
                        sim_val_clay += state.clay_rbs
                if state.minute + time_inc < 24:
                    new_state = State(state.ore_rbs, state.clay_rbs, state.obs_rbs+1, state.geode_rbs, state.ore - bp.obs_cost[0] + (time_inc*state.ore_rbs), state.clay - bp.obs_cost[1] + (time_inc*state.clay_rbs), state.obs + (time_inc*state.obs_rbs), state.geode + (time_inc*state.geode_rbs), state.minute + time_inc)
                    to_explore.append(new_state)
                else:
                    potential_geodes = state.geode + ((24-state.minute)*state.geode_rbs)
                    if potential_geodes > max_geodes:
                        max_geodes = potential_geodes
                        print(state)
                        print(max_geodes)

            if can_make_geode_rbs:
                if state.ore >= bp.geode_cost[0] and state.obs >= bp.geode_cost[1]:
                    # already have enough
                    time_inc = 1
                else:
                    sim_val_ore = state.ore
                    sim_val_obs = state.obs
                    time_inc = 1
                    while sim_val_ore < bp.geode_cost[0] or sim_val_obs < bp.geode_cost[1]:
                        time_inc += 1
                        sim_val_ore += state.ore_rbs
                        sim_val_obs += state.obs_rbs
                if state.minute + time_inc < 24:
                    new_state = State(state.ore_rbs, state.clay_rbs, state.obs_rbs, state.geode_rbs+1, state.ore - bp.geode_cost[0] + (time_inc*state.ore_rbs), state.clay + (time_inc*state.clay_rbs), state.obs - bp.geode_cost[1] + (time_inc*state.obs_rbs), state.geode + (time_inc*state.geode_rbs), state.minute + time_inc)
                    to_explore.append(new_state)
                else:
                    potential_geodes = state.geode + ((24-state.minute)*state.geode_rbs)
                    if potential_geodes > max_geodes:
                        max_geodes = potential_geodes
                        print(state)
                        print(max_geodes)

            '''
            if count % 100 == 0:
                to_explore = sorted(to_explore,key=lambda x: (x.geode_rbs, x.obs_rbs, x.clay_rbs, x.ore_rbs), reverse=True)
                print(len(to_explore))
                #to_explore = sorted(to_explore,key=lambda x: (x.minute), reverse=True)
            '''
            count += 1
        overall_max_geodes.append(max_geodes)
        #break

    print(overall_max_geodes)

    end = [c*(idx+1) for idx, c in enumerate(overall_max_geodes)]
    print(sum(end))
            


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)

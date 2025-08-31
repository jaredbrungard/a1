import collections

def valid_states(state):
   
    left, right = state
    if "Farmer" not in left and (("Wolf" in left and "Goat" in left) or ("Goat" in left and "Cabbage" in left)):
        return False
    if "Farmer" not in right and (("Wolf" in right and "Goat" in right) or ("Goat" in right and "Cabbage" in right)):
        return False
    return True

def next_states(state):
    left, right = state
    possible_states = []
    if "Farmer" in left:
        for item in left:
            if item != "Farmer":
                new_left = left - {item, "Farmer"}
                new_right = right | {item, "Farmer"}
                possible_states.append((frozenset(new_left), frozenset(new_right)))
        new_left = left - {"Farmer"}
        new_right = right | {"Farmer"}
        possible_states.append((frozenset(new_left), frozenset(new_right)))
    else:
        for item in right:
            if item != "Farmer":
                new_right = right - {item, "Farmer"}
                new_left = left | {item, "Farmer"}
                possible_states.append((frozenset(new_left), frozenset(new_right)))
        new_right = right - {"Farmer"}
        new_left = left | {"Farmer"}
        possible_states.append((frozenset(new_left), frozenset(new_right)))

    return [s for s in possible_states if valid_states(s)]

def dls(state, goal, path, limit):
    if state == goal:
        return path

    for next in next_states(state):
        if next not in path:
            result = dls(next, goal, path + [next], limit - 1)
            if result is not None:
                return result
    return None # this is where we would return if we get no result before the limit

def ids(start, goal):
    depth = 0
    while True:
        result = dls(start, goal, [start], depth)
        if result is not None:
            return result
        depth += 1

if __name__ == "__main__":
    #start = (frozenset({"Farmer", "Wolf", "Goat", "Cabbage"}), frozenset())
    start= (frozenset({"Farmer", "Wolf", "Goat"}), frozenset({"Cabbage"}))
    goal = (frozenset(), frozenset({"Farmer", "Wolf", "Goat", "Cabbage"}))
    solution = ids(start, goal)
    
    if solution:
        print("\nSolution Found!")
        for i, step in enumerate(solution):
            print(f"Step {i}: ( {set(step[0])}, {set(step[1])} )")
    else:
        print("No solution found.")
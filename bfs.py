import collections

def valid_states(state):
    left,right = state
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
                possible_states.append((new_left, new_right))
        new_left = left - {"Farmer"}
        new_right = right | {"Farmer"}
        possible_states.append((frozenset(new_left), frozenset(new_right)))
    else:
        #this is how the farmer goes with an item on the boat
        for item in right:
            if item != "Farmer":
                new_right = right - {item, "Farmer"}
                new_left = left | {item, "Farmer"}
                possible_states.append((frozenset(new_left), frozenset(new_right)))
        #this is how the farmer goes alone w/o and item on the boat
        new_right = right - {"Farmer"}
        new_left = left | {"Farmer"}
        possible_states.append((frozenset(new_left), frozenset(new_right)))

    return [s for s in possible_states if valid_states(s)]

def bfs(start, goal):
    frontier = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)


    while frontier:
        current_state, path = frontier.popleft()
        if current_state == goal:
            return path
        for state in next_states(current_state):
            if state not in visited:
                visited.add(state)
                frontier.append((state, path + [state]))
    return None

if __name__ == "__main__":
    start = (frozenset({"Farmer", "Wolf", "Goat", "Cabbage"}), frozenset())
    goal = (frozenset(), frozenset({"Farmer", "Wolf", "Goat", "Cabbage"}))
    solution = bfs(start, goal)
    if solution:
        for step in solution:
            print((set(step[0]), set(step[1])))
    else:
        print("No solution found.")

from collections import deque

# State representation: (missionaries_left, cannibals_left, boat_position)
# Initial state: (3, 3, 'left')
# Goal state: (0, 0, 'right')

def is_valid(state):
    m_left, c_left, boat = state
    # Check if missionaries are eaten
    if m_left > 0 and m_left < c_left:
        return False
    # Check if missionaries are negative or greater than 3
    if m_left < 0 or m_left > 3 or c_left < 0 or c_left > 3:
        return False
    return True

def get_next_states(state):
    m_left, c_left, boat = state
    next_states = []
    
    if boat == 'left':
        # Move one missionary and one cannibal
        if m_left >= 1 and c_left >= 1:
            next_states.append((m_left - 1, c_left - 1, 'right'))
        # Move two missionaries
        if m_left >= 2:
            next_states.append((m_left - 2, c_left, 'right'))
        # Move two cannibals
        if c_left >= 2:
            next_states.append((m_left, c_left - 2, 'right'))
        # Move one missionary
        if m_left >= 1:
            next_states.append((m_left - 1, c_left, 'right'))
        # Move one cannibal
        if c_left >= 1:
            next_states.append((m_left, c_left - 1, 'right'))
    else:  # boat is on the right
        # Move one missionary and one cannibal back
        if m_left <= 2 and c_left <= 2:
            next_states.append((m_left + 1, c_left + 1, 'left'))
        # Move two missionaries back
        if m_left <= 1:
            next_states.append((m_left + 2, c_left, 'left'))
        # Move two cannibals back
        if c_left <= 1:
            next_states.append((m_left, c_left + 2, 'left'))
        # Move one missionary back
        if m_left <= 2:
            next_states.append((m_left + 1, c_left, 'left'))
        # Move one cannibal back
        if c_left <= 2:
            next_states.append((m_left, c_left + 1, 'left'))
    
    # Filter out invalid states
    return [state for state in next_states if is_valid(state)]

def bfs():
    start_state = (3, 3, 'left')
    goal_state = (0, 0, 'right')
    
    if start_state == goal_state:
        return [start_state]
    
    queue = deque([(start_state, [start_state])])
    visited = set([start_state])
    
    while queue:
        current_state, path = queue.popleft()
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                if next_state == goal_state:
                    return path + [next_state]
                queue.append((next_state, path + [next_state]))
                visited.add(next_state)
    
    return None

def print_solution(path):
    if path is None:
        print("No solution found.")
    else:
        print("Solution found:")
        for i, state in enumerate(path):
            m_left, c_left, boat = state
            print(f"Step {i + 1}: Missionaries left: {m_left}, Cannibals left: {c_left}, Boat position: {boat}")

# Solve the problem using BFS
solution_path = bfs()

# Print the solution path
print_solution(solution_path)

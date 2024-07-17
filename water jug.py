from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Initialize the queue with the initial state (0, 0)
    queue = deque([(0, 0)])
    visited = set((0, 0))  # To keep track of visited states

    while queue:
        jug1, jug2 = queue.popleft()

        # If we reach the target in either jug, return the solution
        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            return True

        # List of all possible next states
        next_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour jug1 to jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour jug2 to jug1
        ]

        # Process all possible next states
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)

    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

if water_jug_bfs(jug1_capacity, jug2_capacity, target):
    print(f"Solution found to measure exactly {target} liters")
else:
    print(f"No solution exists to measure exactly {target} liters")

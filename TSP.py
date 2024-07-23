from itertools import permutations

def calculate_path_distance(path, distance_matrix):
    distance = 0
    for i in range(len(path) - 1):
        distance += distance_matrix[path[i]][path[i + 1]]
    distance += distance_matrix[path[-1]][path[0]]  # Return to the start
    return distance

def travelling_salesman_bruteforce(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    shortest_path = None
    min_distance = float('inf')

    for path in permutations(cities):
        current_distance = calculate_path_distance(path, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = path

    return shortest_path, min_distance

# Example distance matrix (symmetric)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, min_distance = travelling_salesman_bruteforce(distance_matrix)
print(f"Shortest path: {shortest_path}")
print(f"Minimum distance: {min_distance}")

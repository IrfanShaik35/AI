from collections import deque

# Function to perform BFS
def bfs(graph, start_node):
    visited = set()             # Set to keep track of visited nodes
    queue = deque([start_node]) # Initialize the queue with the start node
    
    visited.add(start_node)     # Mark the start node as visited
    
    while queue:
        current_node = queue.popleft()
        print(current_node)     # Process the current node (e.g., print it)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from node 'A'
print("BFS traversal starting from node 'A':")
bfs(graph, 'A')

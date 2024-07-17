# Function to perform DFS recursively
def dfs(graph, start_node, visited):
    # Mark the current node as visited and print it
    visited.add(start_node)
    print(start_node, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Set to keep track of visited nodes
visited = set()

# Perform DFS traversal starting from node 'A'
print("DFS traversal starting from node 'A':")
dfs(graph, 'A', visited)

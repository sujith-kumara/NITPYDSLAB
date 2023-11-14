import networkx as nx

def edmonds_karp(graph, source, sink):
    # Initialize residual graph with capacities
    residual_graph = nx.DiGraph(graph)  # Create a copy of the original graph

    # Initialize flow to zero
    flow = 0

    # Continue until no augmenting path exists
    while True:
        # Find augmenting path using Breadth-First Search (BFS)
        path, capacity = bfs(residual_graph, source, sink)

        # If no augmenting path is found, break
        if not path:
            break

        # Update residual graph along the augmenting path
        for u, v in zip(path, path[1:]):
            residual_graph[u][v]['capacity'] -= capacity
            if 'capacity' not in residual_graph[v]:
                residual_graph.add_edge(v, u, capacity=0)
            residual_graph[v][u]['capacity'] += capacity

        # Add flow to the total flow
        flow += capacity

    return flow

def bfs(graph, source, sink):
    # Breadth-First Search to find an augmenting path
    queue = [source]
    visited = {source}
    parent = {source: None}
    capacity = float('inf')

    while queue:
        u = queue.pop(0)
        for v, attr in graph[u].items():
            if v not in visited and attr['capacity'] > 0:
                parent[v] = u
                capacity = min(capacity, attr['capacity'])
                if v == sink:
                    # Reconstruct path
                    path = [v]
                    while v != source:
                        v = parent[v]
                        path.append(v)
                    return path[::-1], capacity
                visited.add(v)
                queue.append(v)

    return None, 0

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add edges with capacities to the graph
G.add_edge('s', 'a', capacity=10)
G.add_edge('s', 'b', capacity=5)
G.add_edge('a', 'b', capacity=15)
G.add_edge('a', 't', capacity=10)
G.add_edge('b', 't', capacity=10)

# Find the maximum flow from source 's' to sink 't'
max_flow = edmonds_karp(G, 's', 't')

print("Maximum Flow:", max_flow)

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
    def searching_algo_BFS(self, s, t, parent):
        # Mark all nodes as unvisited
        visited = [False] * (self.ROW)
        # Create a queue for BFS
        queue = []
        # Enqueue the source node and mark it as visited
        queue.append(s)
        visited[s] = True
        # Loop until the queue is empty
        while queue:
            # Dequeue a node from the queue
            u = queue.pop(0)
            # For every adjacent node of u
            for ind, val in enumerate(self.graph[u]):
                # If the node is unvisited and has positive residual capacity
                if visited[ind] == False and val > 0:
                    # Enqueue the node and mark it as visited
                    queue.append(ind)
                    visited[ind] = True
                    # Store the parent of the node
                    parent[ind] = u
        # Return True if the sink is visited, False otherwise
        return True if visited[t] else False
    def ford_fulkerson(self, source, sink):
        # Initialize the parent array
        parent = [-1] * (self.ROW)
        # Initialize the max flow to 0
        max_flow = 0
        # Loop while there is an augmenting path from source to sink
        while self.searching_algo_BFS(source, sink, parent):
            # Find the minimum residual capacity along the path
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            # Add the path flow to the max flow
            max_flow += path_flow
            # Update the residual capacities of the edges
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        # Return the max flow
        return max_flow

# Create a sample network graph as a matrix
graph1 = [
    [0, 8, 0, 0, 3, 0],
    [0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 7, 2],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 7, 4, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
graph2 = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

# Create a Graph object with the matrix
g = Graph(graph1)


# Define the source and sink nodes
source = 0
sink = 5

# Print the max flow
print("Max Flow: %d " % g.ford_fulkerson(source, sink))
g = Graph(graph2)
# Define the source and sink nodes
source = 0
sink = 5

# Print the max flow
print("Max Flow: %d " % g.ford_fulkerson(source, sink))
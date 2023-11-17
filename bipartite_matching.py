class BipartiteGraph:
    def __init__(self, graph):
        self.graph = graph
        self.U = len(graph)
        self.V = max(max(graph.values(), key=lambda x: max(x, default=0)), default=0) + 1
        self.pair_U = [-1] * self.U
        self.pair_V = [-1] * self.V
        self.dist = [float('inf')] * self.U

  

    def bfs(self):
        queue = []
        for u in range(self.U):
            if self.pair_U[u] == -1:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')

        self.dist[-1] = float('inf')

        while queue:
            u = queue.pop(0)

            if self.dist[u] < self.dist[-1]:
                for v in self.graph[u]:
                    if self.dist[self.pair_V[v]] == float('inf'):
                        self.dist[self.pair_V[v]] = self.dist[u] + 1
                        queue.append(self.pair_V[v])

        return self.dist[-1] != float('inf')

    def dfs(self, u):
        if u != -1:
            for v in self.graph[u]:
                if self.dist[self.pair_V[v]] == self.dist[u] + 1 and self.dfs(self.pair_V[v]):
                    self.pair_V[v] = u
                    self.pair_U[u] = v
                    return True
            self.dist[u] = float('inf')
            return False
        return True

    def hopcroft_karp(self):
        matching = 0
        while self.bfs():
            for u in range(self.U):
                if self.pair_U[u] == -1 and self.dfs(u):
                    matching += 1
        return matching


# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

bipartite_graph = BipartiteGraph(graph)
max_matching = bipartite_graph.hopcroft_karp()

print("Maximum Bipartite Matching:", max_matching)

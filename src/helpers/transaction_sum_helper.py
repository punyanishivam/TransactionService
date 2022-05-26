from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, payment_db):
        sum_ = 0
        visited = set()

        queue = [s]
        visited.add(s)

        while queue:
            s = queue.pop(0)
            sum_ += payment_db[s]["amount"]

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

        return sum_

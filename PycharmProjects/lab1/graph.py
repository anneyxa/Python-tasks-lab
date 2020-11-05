class Graph:
    def __init__(self, dict_graph=None):
        if dict_graph is None:
            dict_graph = {}     # empty dictionary
        self.dict_graph = dict_graph

    def add_vertex(self, vertex):
        if vertex not in self.dict_graph:
            self.dict_graph[vertex] = []

    def delete_vertex(self, vertex):
        try:
            for n in self.dict_graph[vertex]:
                self.dict_graph[n].remove(vertex)
            del self.dict_graph[vertex]
        except KeyError as e:
            print(e)

    def get_vertices(self):      # for testing
        return list(self.dict_graph.keys())

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.dict_graph:
            self.dict_graph[vertex1].append(vertex2)
        else:
            self.dict_graph[vertex1] = [vertex2]

    def delete_edge(self, v1, v2):
        try:
            self.dict_graph[v1].remove(v2)
            self.dict_graph[v2].remove(v1)
        except KeyError as e:
            print(e)

    def get_edges(self):       # for testing
        edge = []
        for vertex in self.dict_graph:
            for next_vertex in self.dict_graph[vertex]:
                if {next_vertex, vertex} not in edge:
                    edge.append({vertex, next_vertex})
        return edge

    def get_all_neighbours_of_vertex(self, vertex):
        try:
            return self.dict_graph[vertex]
        except KeyError as e:
            print(e)

    def bfs(self, start):                # breath-first search
        visited, queue = {start}, []
        if start in self.dict_graph.keys():
            queue.append(start)
            while len(queue) > 0:
                v = queue.pop()
                yield v
                for v2 in self.dict_graph[v]:
                    if v2 not in visited:
                        queue.append(v2)
        else:
            print('vertex not exist in this graph')

    def dfs(self, start, visited=None):    # deep-first search
        if not visited:
            visited = set()
        if start in self.dict_graph.keys():
            yield start
            visited.append(start)
            for v in self.dict_graph[start]:
                self.dfs(start, visited)
        else:
            print('vertex not in graph')



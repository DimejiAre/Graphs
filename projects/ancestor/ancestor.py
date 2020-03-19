class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_neighbors(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        g.add_neighbors(i[1], i[0])

    q = Queue()
    q.enqueue([starting_node])

    visited = set()
    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        p = q.dequeue()
        v = p[-1]

        if(len(p) >= max_path_length and v < earliest_ancestor) or (len(p) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(p)

        if v not in visited:
            visited.add(v)
            
            for neighbor in g.vertices[v]:
                p_copy = list(p)
                p_copy.append(neighbor)
                q.enqueue(p_copy)

    return earliest_ancestor

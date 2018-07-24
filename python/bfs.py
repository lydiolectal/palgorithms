# Breadth-first search

import unittest
from collections import deque
from graph import *

def bfs(graph, start, end):
    if start == end:
        return []
    queue = deque()
    queue.appendleft(start)
    while not len(queue) == 0:
        curr = queue.pop()
        if curr == end:
            break
        for neighbor in curr.neighbors:
            if not neighbor.traversed:
                queue.appendleft(neighbor)
                neighbor.traverse()
                neighbor.parents = curr.parents.copy()
                neighbor.parents.append(curr)
    end.parents.append(end)
    return end.parents

class TestBFS(unittest.TestCase):
    def test_one_edge(self):
        v1 = Vertex("me")
        v2 = Vertex("you")
        g = Graph({v1, v2})
        g.add_edge(v1, v2)

        path = bfs(g, v1, v2)
        self.assertEqual(path, [v1, v2])
    
    def test_many(self):
        i = Vertex("Ilana Glazer")
        h = Vertex("Hilary", {i})
        j = Vertex("Abbi", {i})
        o = Vertex("Barack", {h})
        y = Vertex("Yasmin", {j, o})
        b = Vertex("Ben", {o})
        a = Vertex("Aurora", {y, b})

        graph = Graph({i, h, j, o, y, b, a})
        path = bfs(graph, a, i)
        self.assertEqual(path, [a, y, j, i])

if __name__ == "__main__":
    unittest.main()
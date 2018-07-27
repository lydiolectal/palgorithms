from graph import *
import unittest

def topological_sort(g):
    global n
    n = len(g.vertices) - 1
    global labels
    labels = {}
    for v in g.vertices:
        if not v.traversed:
            dfs(g, v)
    order = list(map(lambda i: labels[i], range(len(g.vertices))))
    return order

def dfs(g, s):
    if not s.traversed:
        s.traverse()
        for neighbor in s.neighbors:
            dfs(g, neighbor)
        global n
        labels[n] = s
        n -= 1

class TestTopologicalSort(unittest.TestCase):

    def test_small(self):
        t = Vertex("t")
        v = Vertex("v", {t})
        w = Vertex("w", {t})
        s = Vertex("s", {v, w})
        g = Graph({t, v, w, s})

        sort = topological_sort(g)
        self.assertIn(sort, [[s, v, w, t], [s, w, v, t]])

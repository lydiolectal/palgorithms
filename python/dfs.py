import unittest
from graph import *

def dfs(graph, start):
    stack = [start]
    traversed = []

    while stack:
        curr = stack.pop()
        if not curr.traversed:
            curr.traversed = True
            traversed.append(curr)
            stack.extend([v for v in curr.neighbors])

    return traversed

def dfs_recursive(graph, curr):
    traversed = []
    def dfs_helper(curr):
        if not curr.traversed:
            curr.traversed = True
            traversed.append(curr)
            for neighbor in curr.neighbors:
                dfs_helper(neighbor)
    dfs_helper(curr)
    return traversed

class TestDFS(unittest.TestCase):
    def test_one_edge(self):
        v1 = Vertex("me")
        v2 = Vertex("you")
        g = Graph({v1, v2})
        g.add_edge(v1, v2)
        path = dfs(g, v1)
        self.assertTrue(path in [
            [v1, v2]
        ])

        v1 = Vertex("me")
        v2 = Vertex("you")
        g = Graph({v1, v2})
        g.add_edge(v1, v2)
        path = dfs_recursive(g, v1)
        self.assertTrue(path in [
            [v1, v2]
        ])

    def test_few(self):
        d = Vertex("d")
        c = Vertex("c", {d})
        b = Vertex("b", {c})
        a = Vertex("a", {b, c, d})
        g = Graph({a, b, c, d})

        path = dfs(g, a)
        self.assertTrue(path in [
            [a, b, c, d],
            [a, d, b, c],
            [a, c, d, b],
            [a, d, c, b]
        ])

        d = Vertex("d")
        c = Vertex("c", {d})
        b = Vertex("b", {c})
        a = Vertex("a", {b, c, d})
        g = Graph({a, b, c, d})

        path = dfs_recursive(g, a)
        self.assertTrue(path in [
            [a, b, c, d],
            [a, d, b, c],
            [a, c, d, b],
            [a, d, c, b]
        ])


if __name__ == "__main__":
    unittest.main()

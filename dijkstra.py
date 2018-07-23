import unittest

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices

    def find_shortest_path(self, start, end):
        cost_table = {n: float("inf") for n in self.vertices.keys()}
        cost_table[start] = 0
        parent_table = {}
        cur_cheapest = start
        while cur_cheapest:
            neighbors = self.vertices[cur_cheapest]
            for neighbor in neighbors.keys():
                new_cost = cost_table[cur_cheapest] + neighbors[neighbor]
                if new_cost < cost_table[neighbor]:
                    cost_table[neighbor] = new_cost
                    parent_table[neighbor] = cur_cheapest

            cur_cheapest = self.next(cur_cheapest, cost_table)

        # traverse parent_table backwards to get path
        path = [end]
        curr = end
        while curr != start:
            curr = parent_table[curr]
            path.append(curr)
        return list(reversed(path))

    def next(self, cur_node, cost_table):
        cur_cost = cost_table[cur_node]
        next_cost = float("inf")
        next_node = None
        for node, cost in cost_table.items():
            if cost > cur_cost and cost < next_cost:
                next_cost = cost
                next_node = node
        return next_node

class TestDijkstra(unittest.TestCase):

    def test_whee(self):
        v = {"start": {"a": 6, "b": 2}, "a": {"fin": 1},
            "b": {"a": 3, "fin": 5}, "fin": {}}
        g = Graph(v)
        path = g.find_shortest_path("start", "fin")
        self.assertEqual(path, ["start", "b", "a", "fin"])

    def test_woo(self):
        v = {"start": {"a": 5, "c": 2}, "a": {"b": 4, "d": 2},
            "b": {"d": 6, "fin": 3}, "c": {"a": , "d"}, "d": {"fin"}}
        g = Graph(v)
        path = g.find_shortest_path("start", "fin")
        self.assertEqual(path, ["start", "a", "d", "fin"])

if __name__ == "__main__":
    unittest.main()

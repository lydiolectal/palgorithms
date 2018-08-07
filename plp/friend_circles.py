import unittest

class UnionFind:

    def __init__(self, l):
        self.parent = [i for i in range(l)]
        self.rank = [0 for _ in range(l)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1

def find_circle_num(m):
    n = len(m)
    uf = UnionFind(n)
    # refactor this grossness into something more readable
    for r in range(n):
        for c in range(r, n):
            if m[r][c] and r != c:
                uf.union(r, c)

    return len(set([uf.find(x) for x in uf.parent]))

class TestFriendCircle(unittest.TestCase):
    # def test_two(self):
    #     m = [[1,1,0],
    #         [1,1,0],
    #         [0,0,1]]
    #     self.assertEqual(find_circle_num(m), 2)
    #
    # def test_one(self):
    #     m = [[1,1,0],
    #          [1,1,1],
    #          [0,1,1]]
    #     self.assertEqual(find_circle_num(m), 1)

    def test_another_one(self):
        m = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
        self.assertEqual(find_circle_num(m), 1)

# if __name__ == "__main__":
#     unittest.main()

class Graph:
  # vertices is a set
  def __init__(self, vertices):
    self.vertices = vertices

  def adjacent(self, v1, v2):
    return v2 in v1.neighbors

  def neighbors(self, v):
    return v.neighbors

  def parents(self, target):
    return set([vertex for vertex in self.vertices
                if self.adjacent(vertex, target)])

  def add_vertex(self, v):
    self.vertices.add(v)

  def remove_vertext(self, v):
    self.vertices.remove(v)

  def add_edge(self, v1, v2):
    self.add_vertex(v1)
    self.add_vertex(v2)
    v1.neighbors.add(v2)

  def remove_edge(self, v1, v2):
    if not v1 in self.vertices or not v2 in self.vertices:
      return None

    v1.neighbors.remove(v2)

  def get_vertex_value(self, v):
    return v.content

  def set_vertex_value(self, v, val):
    v.content = val

class Vertex:
  def __init__(self, content, neighbors = set()):
    self.content = content
    self.neighbors = neighbors
    self.traversed = False
    self.parents = []

  def traverse(self):
    self.traversed = True

if __name__ == "__main__":
  i = Vertex("Ilana Glazer")
  h = Vertex("Hilary", {i})
  j = Vertex("Abbi", {i})
  o = Vertex("Barack", {h})
  y = Vertex("Yasmin", {j, o})
  b = Vertex("Ben", {o})
  a = Vertex("Aurora", {y, b})

  graph = Graph({i, h, j, o, y, b, a})

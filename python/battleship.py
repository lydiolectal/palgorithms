enum HitResult:
    Hit
    Sink
    Miss
    Error

# return HitResult.Hit

# "hit" coords in ship and check if sunk
class Ship:

    def __init__(self, health):
        # {(row, col), (row, col)}
        self.health = health

    def is_sunk(self):
        self.health -= 1
        if self.health == 0:
            return HitResult.Sunk
        return HitResult.Hit

# 1. spot has been hit before
# 1. map coord to Ship
class BattleshipBoard:

    def __init__(self, width, height, ship_coords):
        # self.board_state = [[False for _ in range(width)] for _ in range(height)]
        self.board_state = set()
        self.width = width
        self.height = height
        # {(row, col): Ship, ...,}
        self.ship_coords = ship_coords

    def hit_analyzer(self, coord):
        row, col = coord

        if row >= self.width or col >= self.height:
            return HitResult.Error
        # if self.board_state[row][col]:
        if coord in self.board_state:
            return HitResult.Error

        # self.board_state[row][col] = True
        self.board_state.add(coord)
        if coord not in self.ship_coords:
            return HitResult.Miss
        else:
            ship = self.ship_coords[coord]
            return ship.is_sunk()

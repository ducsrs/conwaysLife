GRID_SIZE = 10

class Cell:
    grid = {}

    def __init__(self, x: int, y: int, is_alive=False):
        self.alive = is_alive
        self.neighbors = [(a % GRID_SIZE, b % GRID_SIZE) for a in range(x - 1, x + 2)
                          for b in range(y - 1, y + 2) if (a, b) != (x, y)]
        self.aliveNext = False

    def rules(self):
        count = [Cell.grid[neighbor].alive for neighbor in self.neighbors].count(True)
        if count < 2 or count > 3:
            self.aliveNext = False
        elif count == 3:
            self.aliveNext = True
        elif self.alive:
            self.aliveNext = True

    def update(self): self.alive = self.aliveNext

def report():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if Cell.grid[(i, j)].alive:
                print('O', end=' ')
            else:
                print('-', end=' ')
        print()


for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        Cell.grid[(i, j)] = Cell(i, j)

starting = [(1, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
for point in starting:
    Cell.grid[point].alive = True

while True:
    report()
    for cell in Cell.grid.values():
        cell.rules()
    for cell in Cell.grid.values():
        cell.update()
    step = input()
    print('\n\n\n\n')

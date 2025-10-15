import random


class EnzoGame:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.grid = self.draw_lupin()

    def draw_lupin(self):
        # crea matrice 4x4 con False e un True casuale
        matrix = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        r = random.randint(0, self.rows - 1)
        c = random.randint(0, self.cols - 1)
        matrix[r][c] = True
        return matrix

    def check_enzo(self, r, c):
        if self.grid[r][c]:
            self.grid = self.draw_lupin()  # rigenera Lupin
            return True
        return False

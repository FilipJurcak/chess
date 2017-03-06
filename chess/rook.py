from chess.figure import Figure


class Rook(Figure):
    def check(self, destx, desty, color, dx, dy):
        if self.color == color and self.checkWayRook(destx, desty):
            return True
        return False

    def checkWayRook(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if dx != 0 and dy != 0:
            return False
        for i in range(max(abs(dy), abs(dx)) - 1):
            if dx == 0:
                diffy = int(dy / abs(dy) * (i + 1))
                if self.board[self.x][self.y + diffy] == 1:
                    return False
            if dy == 0:
                diffx = int(dx / abs(dx) * (i + 1))
                if self.board[self.x + diffx][self.y] == 1:
                    return False
        return True

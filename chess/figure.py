from importlib import import_module
from chess.list_images import List_images


class Figure:
    def __init__(self, x, y, color, image, board):
        self.x = x
        self.y = y
        self.color = color
        self.image = image
        self.board = board

    def movement(self, destx, desty, figures, color, dx, dy):
        if self.check(destx, desty, color, dx, dy):
            return self.move(destx, desty, figures, dx, dy)

    def move(self, destx, desty, figures, dx, dy):
        instance = ''
        for figure in figures:
            if figure.x == destx and figure.y == desty and figure.color != self.color:
                instance = figure.__class__.__name__
        if self.__class__.__name__ == 'Pawn' and instance != 'King' and dy == 1 and (
                    (self.y == 1 and self.color == 'white') or (self.y == 6 and self.color == 'black')):
            if (dx == 0 and self.board[destx][desty] == 0) or (dx == 1 and self.board[destx][desty] == 1):
                var = input("Choose which figure do you want: \n")
                self.switch(var, figures, destx, desty)
                self.board[self.x][self.y] = 0
                self.board[destx][desty] = 1
                return 0
        if self.board[destx][desty] == 1:
            for i in range(len(figures)):
                if figures[i].x == destx and figures[i].y == desty and figures[i].color != self.color:
                    if figures[i].__class__.__name__ == "King":
                        if self.color == 'white':
                            return 1
                        if self.color == 'black':
                            return 2
                    del figures[i]
                    break
        self.board[self.x][self.y] = 0
        self.board[destx][desty] = 1
        self.x = destx
        self.y = desty
        return 0

    def switch(self, var, figures, destx, desty):
        self.Images = List_images().Images
        while var != "Rook" and var != "Queen" and var != "Knight" and var != "Bishop":
            var = input("Choose which figure do you want: \n")
        color = self.color
        board = self.board
        # figures = [value for value in figures if not(value.x == destx and value.y == desty)]
        for i in range(len(figures)):
            if figures[i].x == destx and figures[i].y == desty:
                del figures[i]
                break
        # figures = [value for value in figures if not(value.x == self.x and value.y == self.y)]
        for i in range(len(figures)):
            if figures[i].x == self.x and figures[i].y == self.y:
                del figures[i]
                break
        classfigure = var
        var = chr(ord(var[0]) + 32) + var[1:]
        module = import_module('chess.' + str(var))
        class_ = getattr(module, classfigure)
        figures.append(class_(destx, desty, color, self.Images[color + str(classfigure)]['Image'], board))

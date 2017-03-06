from chess.game import Game


class Console:
    def __init__(self, state):
        self.game = Game()
        if state == 'yes':
            self.game.load()
        else:
            self.game.create()

    def chess_setup(self):
        for figure in self.game.figures:
            self.game.board[figure.x][figure.y] += 1

    def start(self):
        self.chess_setup()
        while True:
            if self.game.whomoves % 2 == 0:
                print("White's turn")
            else:
                print("Black's turn")
            start = input('Figure on which positions do you wanna move?' + '\n' +
                          'If you want to save your game, type save, if quit, type quit.\n')
            if start == 'save':
                name = input('Type name of file in which you wanna save the game.\n')
                name += '.txt'
                self.game.save(name)
                start = input('Figure on which positions do you wanna move?\n')
            if start == 'quit':
                quit()
            startx = self.positions(start)
            startx = start.split()
            dest = input('Where do you wanna move it?\n')
            destx = self.positions(dest)
            move = self.game.move(startx[0], startx[1], destx[0], destx[1])
            if move != 0:
                if move == 1:
                    print("Whites are Winners")
                if move == 2:
                    print("Blacks are Winners")
                return

    def positions(self, position):
        return int(position.split()[0]), int(position.split()[1])

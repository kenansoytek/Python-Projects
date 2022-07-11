
class Game():
    def __init__(self):
        self.board = [["( )","( )","( )",],["( )","( )","( )",],["( )","( )","( )",]]
        self.situation = True
        self.move = 0

    def play(self):
        if self.move % 2 == 0:
            self.p1pick()
        else:
            self.p2pick()
        
        self.situation = self.gamecontrol()

        self.move += 1

    def p1pick(self):
        self.show_board()
        print("Birinci Oyuncu,")
        line = int(input("Satırı Giriniz: "))
        while line < 1 or line > 3:
            line = int(input("Girilecek satır değeri 1,2 veya 3 olabilir tekrar giriniz: "))

        column = int(input("Sütunu Giriniz: "))
        while column < 1 or column > 3:
            column = int(input("Girilecek sütun değeri 1,2 veya 3 olabilir tekrar giriniz: "))

        if self.isitfull(line, column):
            self.p1pick()
        else:
            self.board[line-1][column-1] = "X"

    def p2pick(self):
        self.show_board()
        print("İkinci Oyuncu,")
        line = int(input("Satırı Giriniz: "))
        while line < 1 or line > 3:
            line = int(input("Girilecek satır değeri 1,2 veya 3 olabilir tekrar giriniz: "))

        column = int(input("Sütunu Giriniz: "))
        while column < 1 or column > 3:
            column = int(input("Girilecek sütun değeri 1,2 veya 3 olabilir tekrar giriniz: "))

        if self.isitfull(line, column):
            self.p2pick()
        else:
            self.board[line-1][column-1]= "O"

    def isitfull(self,line,column):
        if self.board[line][column] != "(  ) ":
            return True
        else:
            return False

    def show_board(self):
        for i in self.show_board():
            for j in i:
                print(j, end=" ")

            print("\n")

    def gamecontrol(self):
        #Horizontal control
        if [self.board[0][0],self.board[0][1],self.board[0][2] == ["X","X","X"]] or [self.board[0][0],self.board[0][1],self.board[0][2] == ["O","O","O"]]:
            return False
        if [self.board[1][0],self.board[1][1],self.board[1][2] == ["X","X","X"]] or [self.board[1][0],self.board[1][1],self.board[1][2] == ["O","O","O"]]:
            return False
        if [self.board[2][0],self.board[2][1],self.board[2][2] == ["X","X","X"]] or [self.board[2][0],self.board[2][1],self.board[2][2] == ["O","O","O"]]:
            return False

        #Vertical control
        if [self.board[0][0],self.board[1][0],self.board[2][0] == ["X","X","X"]] or [self.board[0][0],self.board[1][0],self.board[2][0] == ["O","O","O"]]:
            return False
        if [self.board[0][1],self.board[1][1],self.board[2][1] == ["X","X","X"]] or [self.board[0][1],self.board[1][1],self.board[2][1] == ["O","O","O"]]:
            return False
        if [self.board[0][2],self.board[1][2],self.board[2][2] == ["X","X","X"]] or [self.board[0][2],self.board[1][2],self.board[2][2] == ["O","O","O"]]:
            return False

        #Croos Control
        if [self.board[0][0],self.board[1][1],self.board[2][2] == ["X","X","X"]] or [self.board[0][0],self.board[1][1],self.board[2][2] == ["O","O","O"]]:
            return False
        if [self.board[0][2],self.board[1][1],self.board[2][0] == ["X","X","X"]] or [self.board[0][2],self.board[1][1],self.board[2][0] == ["O","O","O"]]:
            return False

        return True
        
        
game = Game()
while game.situation:
    game.play()


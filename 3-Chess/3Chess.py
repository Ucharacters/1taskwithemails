from abc import ABC, abstractmethod

class ChessGame(ABC):
    @abstractmethod
    def rules_of_game(epoch):
        """игра имела разные правила в разные времена"""
        pass

class ChessPiece(ABC):
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
        self.location = None
   
    @abstractmethod
    def move(self, default="БпЕ2Е4"):
        """очень много вариантов реализации"""
        pass

    @abstractmethod
    def attack(self, default="Е4"):
        """очень много вариантов реализации"""
        pass    

        
class Match(ChessGame):
    def __init__(self, country, epoch):
        #в каких странах как называется
        countries={
            "Индия":"shah wazir fil asp rukh piyada",
            "Англия":"king queen bishop knight rook pawn",
            "Россия":"король ферзь слон конь ладья пешка"}        
        self.chesspieceranks=countries[country].split(" ")
        self.rules_of_game(epoch)

        class Pawn(ChessPiece):
            def move(self, default="Е2Е4"):
                """на последней клетке пешка становится другой ферзём"""
                pass

            def attack(self, default="Е4"):
                """пешка атакует по диагонали, не может атаковать короля и т.д."""
                pass

        for chesspiece in self.chesspieceranks:
            #создаём фигуры
            if chesspiece=="пешка":
                    for cell in range(self.board_size):
                        new_pawn=Pawn("белые",chesspiece)
                        new_pawn=Pawn("черные",chesspiece)
                        
        assert issubclass(Pawn("белые","пешка"), ChessPiece)
        assert ininstance(new_pawn,ChessPiece)
        
    def rules_of_game(self, epoch):
        if epoch==2022:
            self.board_size=8 #"8 x 8"

            class Pawn(ChessPiece):
                def move(self, default="Е2Е4"):
                    """на последней клетке пешка становится другой ферзём"""
                    pass

##                def attack(self, default="Е4"):
##                     """пешка атакует по диагонали, не может атаковать короля и т.д."""
##                    pass
                
        if epoch==1920:
            self.board_size="10 x 10"






                


     
    def change_turns():
        print(input('--> ')) 
        setactiveplayer = not setactiveplayer

    def start(default="БпЕ2Е4"):
        self.game_over=False
        self.setactiveplayer=False

        while not game_over:
            change_turns()
            move()
        

country="Россия"
epoch=2022
new_game= Match(country, epoch)
new_game.start()


assert issubclass(Match, ChessGame)
assert isinstance(Match(country, epoch),ChessGame)


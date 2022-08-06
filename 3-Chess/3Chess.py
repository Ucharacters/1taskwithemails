from abc import ABC, abstractmethod

#ООП: пример метакласса, когда создание класса происходит в рантайм
class ChessGame(ABC):
    @abstractmethod
    def rules_of_game(epoch):
        """игра имела разные правила в разные времена"""
        pass
    
    #как называются фигуры в разных странах 
    countries={
        "Индия":"shah wazir fil asp rukh piyada",
        "Англия":"king queen bishop knight rook pawn",
        "Россия":"король ферзь слон конь ладья пешка"} 

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

        
class ModernMatch(ChessGame):
    def __init__(self, country, epoch):
       
        self.chesspieceranks=self.countries[country].split(" ")
        print(" фигуры называются ")
        print(self.chesspieceranks)
        self.rules_of_game(epoch)

    def rules_of_game(self, epoch):
        if epoch==2022:
            self.board_size=8 #"8 x 8"

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
                        
        assert issubclass(Pawn, ChessPiece)
        assert isinstance(new_pawn,ChessPiece)
        


    def start(default="БпЕ2Е4"):
        def change_turns():
            print("Введите ход в формате ФE2E4 (end для завершения игры):")
            return str(input('--> '))

        
        game_over=False
        setactiveplayer=False

        while not game_over:
            if not change_turns()=="end":
                setactiveplayer = not setactiveplayer
            else:
                game_over=True
        
class AncientMatch(ChessGame):
    def __init__(self, country, epoch):
       
        self.chesspieceranks=self.countries[country].split(" ")
        print(" фигуры называются ")
        print(self.chesspieceranks)
        self.rules_of_game(epoch)

    def rules_of_game(self, epoch):
        if epoch==1920:
            self.board_size=10 #"10 x 10"

            class Pawn(ChessPiece):
                def move(self, default="Е2Е4"):
                    """на последней клетке пешка НЕ становится другой ферзём"""
                    pass
                
                def attack(self, default="Е4"):
                    """пешка НЕ атакует по диагонали"""
                    pass
                
        for chesspiece in self.chesspieceranks:
            #создаём фигуры
            if chesspiece=="pawn":
                    for cell in range(self.board_size):
                        new_pawn=Pawn("белые",chesspiece)
                        new_pawn=Pawn("черные",chesspiece)
                        
        assert issubclass(Pawn, ChessPiece)
        assert isinstance(new_pawn,ChessPiece)
                


    def start(default="БпЕ2Е4"):
        def change_turns():
            print("Запишите ход на бумаге в формате QE2E4 и передйте рефери (end для завершения игры):")
            return str(input('--> '))

        
        game_over=False
        setactiveplayer=False

        while not game_over:
            if not change_turns()=="end":
                setactiveplayer = not setactiveplayer
            else:
                game_over=True

#==============================================================
country="Россия"
epoch=2022
new_game= ModernMatch(country, epoch) # правила игры создаются в рантайм
assert issubclass(ModernMatch, ChessGame)
assert isinstance(new_game,ChessGame)
new_game.start()

country="Англия"
epoch=1920
new_game= AncientMatch(country, epoch) # правила игры создаются в рантайм
assert issubclass(AncientMatch, ChessGame)
assert isinstance(new_game,ChessGame)
new_game.start()




from .list_de import ListDE
from .user import User

class Board:
    def __init__(self,id:int,rows:int,cols:int, player:User,ship_list:ListDE):
        self.id = id
        self.cols = cols
        self.rows = rows
        self.player = player
        self.ship_list = ship_list
        self.received_shoots = []
        self.board_state = False

    def validate_shoot(self,x:int,y:int):
        pass
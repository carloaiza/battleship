from .ship import Ship

class ShipDistribution:
    def __init__(self,ship:Ship):
        self.ship = ship
        self.places = []
        self.orientation = 0
        self.state = "FREE"

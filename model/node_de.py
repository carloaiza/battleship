from .ship_distribution import ShipDistribution

class NodeDE:
    def __init__(self,data:ShipDistribution):
        self.data= data
        self.next = None
        self.previous = None
        
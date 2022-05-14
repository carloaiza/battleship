from .node_de import NodeDE
from .ship_distribution import ShipDistribution

class ListDE:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self,data:ShipDistribution):
        if self.head == None:
            self.head = NodeDE(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = NodeDE(data)
            temp.next.previous = temp
        self.count += 1

    def add_to_start(self, data:ShipDistribution):
        if self.head == None:
            self.head = NodeDE(data)
        else:
            self.head.previous = NodeDE(data)
            self.head.previous.next = self.head
            self.head = self.head.previous
        self.count +=1

    def list(self):
        list = []
        temp = self.head
        while temp != None:
            list.append(temp.data)
            temp = temp.next
        return list

    def clone_list(self):
        list = ListDE()
        temp = self.head
        while temp != None:
            list.add(temp.data)
            temp = temp.next
        return list
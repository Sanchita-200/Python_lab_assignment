class Transport:
    def __init__(self):
        self.type = "Road"
class Boat(Transport):
    def __init__(self):
        super().__init__(type)
        self.capacity = input("Enter the capacity")
        self.source = input("enter the source")
        self.destination= input("Enter the destination")
    def show(self):
        print(self.capacity)
        print(self.source)
        print(self.destination)

class Bus(Transport):
    def __init__(self):
        super().__init__(type)
        self.seat_no = input("Enter the seat_no")
        self.source = input("enter the source")
        self.destination= input("Enter the destination")
        def show(self):
        print(self.seat_no)
        print(self.source)
        print(self.destination)

boat1=Boat()
b
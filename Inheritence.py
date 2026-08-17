class Transport:
    def __init__(self,type):
        self.type="road"
    def show(self):
        print("Type of transport is: ",self.type)

class Bus(Transport):
    def __init__(self):
        super().__init__(type)
        self.seatno =input("Enter the seat number ")
        self.source=input("Enter the source ")
        self.destination=input("Enter the destination ")
    def display(self):
        print(self.seatno)
        print(self.source)
        print(self.destination)

ob1=Bus()
ob1.display()
ob1.show()
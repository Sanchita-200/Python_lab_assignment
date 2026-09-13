#Create a class Transport with variable type. Create 2 child classes Boat and Bus. Boat having variable capacity, source, destination. Bus has varibale seat no source destination. 
#Initialise all the variables of all the classes with constructor. Define show method in transport class to display the type of transport. 
#Define show method in Boat class to display type and in Bus class to display the attributes of the bus. Create 2 objects of both boat and bus.

class Transport:
    def __init__(self,type):
        self.type = type
    def show(self):
        print("\nType of Transport: ", self.type)

class Boat(Transport):
    def __init__(self,capacity,source,destination):
        super().__init__("Water Transport")
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
            super().show()
            print("Capacity: ",self.capacity)
            print("Source: ", self.source)
            print("Destination: ", self.destination)

class Bus(Transport):
    def __init__(self,seatNumber,source,destination):
        super().__init__("Road Transport")
        self.seatNumber = seatNumber
        self.source = source
        self.destination = destination

    def show(self):
            super().show()
            print("Seat Number: ",self.seatNumber)
            print("Source: ", self.source)
            print("Destination: ", self.destination,"\n")

t1 = Boat(50,"Here", "There")
t2 = Bus("12A","Yaha","Wahan")
t3 = Boat(10,"This Bank", "That Bank")
t4 = Bus("49B", "This City", "That City")
t1.show()
t2.show()
t3.show()
t4.show()

"""

Type of Transport:  Water Transport
Capacity:  50
Source:  Here
Destination:  There

Type of Transport:  Road Transport
Seat Number:  12A
Source:  Yaha
Destination:  Wahan 


Type of Transport:  Water Transport
Capacity:  10
Source:  This Bank
Destination:  That Bank

Type of Transport:  Road Transport
Seat Number:  49B
Source:  This City
Destination:  That City 

"""

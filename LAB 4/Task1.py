class Vehicle:
    def __init__(self,seating_capacity):
        self.fare = seating_capacity*100
class Bus(Vehicle):
    def __init__(self,seating_capacity):
        super().__init__(seating_capacity)
        self.final_amount = self.fare*0.1 + self.fare
    def print_amount(self):
        print(f"The final amount is {self.final_amount}")

number_of_passengers = int(input("Enter the number of passengers:"))
bus1 = Bus(number_of_passengers)
bus1.print_amount()

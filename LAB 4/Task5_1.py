from datetime import date
from typing import List
class Vehicle:
    def __init__(self,make,model,rental_price,availability_status=True):
        self.make = make
        self.model = model
        self.__rental_price = rental_price  
        self._availability_status = availability_status
    def get_rental_price(self):
        return self.__rental_price
    def set_rental_price(self,new_price):
        if new_price < 0:
            raise ValueError("Rental price cannot be negative")
        self.__rental_price = new_price
    @property
    def availability_status(self):
        return self._availability_status
    @availability_status.setter
    def availability_status(self,value):
        self._availability_status = bool(value)
    def check_availability(self):
        raise NotImplementedError("Subclasses should implement check_availability()")
    def calculate_cost(self,days):
        if days <= 0:
            raise ValueError("Rental period must be at least 1 day")
        return self.get_rental_price() * days
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Rental price (private): {self.get_rental_price()}")
        print(f"Available: {self.availability_status}")
class Car(Vehicle):
    def check_availability(self):
        print("The Car is Available") if self.availability_status else print("The Car is not Available")
    def display(self):
        print("--- Car Details ---")
        super().display()
class SUV(Vehicle):
    def check_availability(self):
        print("The SUV is Available") if self.availability_status else print("The SUV is not Available")
    def display(self) -> None:
        print("--- SUV Details ---")
        super().display()
class Truck(Vehicle):
    def check_availability(self):
        print("The Truck is Available") if self.availability_status else print("The Truck is not Available")

    def display(self):
        print("--- Truck Details ---")
        super().display()
class Customer:
    def __init__(self,name,contact_info):
        self.name = name
        self.__contact_info = contact_info  
        self._reservations: List[RentalReservation] = []  
    def get_contact_info(self):
        return self.__contact_info
    def set_contact_info(self,new_contact):
        self.__contact_info = new_contact
    def add_reservation(self,reservation:'RentalReservation'):
        self._reservations.append(reservation)
    def display_rental_history(self):
        print(f"Rental history for {self.name}:")
        if not self._reservations:
            print("  No reservations yet.")
            return
        for res in self._reservations:
            print(f"  - {res}")
    def __str__(self):
        return f"Customer(name={self.name})"
class RentalReservation:
    def __init__(self,customer,vehicle,start_date,end_date):
        if start_date > end_date:
            raise ValueError("Start date must be on or before end date")
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self._is_active = False
        self._make_reservation()
    def _rental_days(self):
        return (self.end_date - self.start_date).days + 1
    def _make_reservation(self):
        if not self.vehicle.availability_status:
            raise RuntimeError("Vehicle is not available for reservation")
        self.vehicle.availability_status = False
        self._is_active = True
        self.customer.add_reservation(self)
    def calculate_total_cost(self):
        days = self._rental_days()
        return self.vehicle.calculate_cost(days)
    def end_reservation(self):
        if not self._is_active:
            print("Reservation already ended or was never active")
            return
        self._is_active = False
        self.vehicle.availability_status = True
    def display(self):
        print("--- Reservation Details ---")
        print(f"Customer: {self.customer.name}")
        print(f"Contact: {self.customer.get_contact_info()}")
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}")
        print(f"From: {self.start_date} To: {self.end_date}")
        print(f"Total cost: {self.calculate_total_cost()}")
        print(f"Active: {self._is_active}")
    def __str__(self):
        return (f"Reservation(customer={self.customer.name}, vehicle={self.vehicle.make} {self.vehicle.model}, "f"from={self.start_date}, to={self.end_date}, active={self._is_active})")
def display_details(obj):
    if hasattr(obj, 'display') and callable(getattr(obj, 'display')):
        obj.display()
    else:
        print(obj)
if __name__ == '__main__':
    car = Car('Toyota', 'Corolla', 40.0, True)
    suv = SUV('Honda', 'CRV', 60.0, True)
    truck = Truck('Isuzu', 'NPR', 100.0, True)
    cust = Customer('Ali Khan', 'ali.khan@gmail.com')
    res = RentalReservation(cust, car, date(2025, 10, 5), date(2025, 10, 7))
    display_details(car)
    display_details(res)
    res.end_reservation()
    cust.display_rental_history()
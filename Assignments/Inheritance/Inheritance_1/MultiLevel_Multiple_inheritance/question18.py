# 18. Vehicle Insurance System
# Vehicle
# InsuredVehicle
# Car

# Calculate insurance amount.

class Vehicle:

    __collection = {}

    def __init__(self, company_name, vehicle_type, availability, vehicle_id):

        self.__company_name = company_name
        self.__vehicle_type = vehicle_type
        self.__availability = availability
        self.__vehicle_id = vehicle_id

        Vehicle.__collection[self.__vehicle_id] = {
            "company name": self.__company_name,
            "vehicle type": self.__vehicle_type,
            "availability": self.__availability
        }

    def display_all_vehicles(self):

        for key, val in Vehicle.__collection.items():
            print(f"ID: {key} : {val}")

    def check_vehicle_id(self, id):

        if id in Vehicle.__collection:
            return id
        else:
            return None

    def check_availability(self, id):

        return Vehicle._Vehicle__collection[id]["availability"]


class InsuredVehicle(Vehicle):

    def __init__(self, vehicle_id, amount, age_of_vehicle):

        self.__id = vehicle_id
        self.__amount = amount
        self.__age_of_vehicle = age_of_vehicle

    def get_amount(self):
        return self.__amount

    def Insurance(self):

        if super().check_vehicle_id(self.__id) is not None:

            if super().check_availability(self.__id):
                print("Insurance is possible")
                return True

            else:
                print("Vehicle is not available")
                return False

        else:
            print("There is no vehicle registered with this ID")
            return False


class Car(InsuredVehicle):

    def __init__(self, name, age, vehicle_id, amount,age_of_vehicle, duration):

        super().__init__(vehicle_id, amount, age_of_vehicle)

        self.__name = name
        self.__age = age
        self.__duration = duration

    def insurance_paper(self):

        if self.Insurance():

            print("\n_____________Insurance Document_____________")

            print(f"""
This is to inform that {self.__name} has purchased
insurance for their vehicle from Shree Ram Finance.

Insurance Amount: Rs. {self.get_amount()}
Duration: {self.__duration} months
Vehicle Age: {self._InsuredVehicle__age_of_vehicle} years
""")

            print("______________________________________________")


# Register vehicles

v1 = Vehicle("Hyundai", "Car", True, 101)
v2 = Vehicle("Honda", "Car", False, 102)
v3 = Vehicle("Tata", "Car", True, 103)


# Create insurance object

c1 = Car("Kashish", 20, 101, 15000, 3, 12)

c1.insurance_paper()

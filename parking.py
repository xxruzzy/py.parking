import datetime
import time


class Parking:
    users = []

    def __init__(self):
        pass


class User:
    name = ""
    phone = 0
    password = ""
    
    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password = password

    def sign_up():
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        password = input("Set your password: ")
        
    
        
        for user in Parking.users:
            if user.phone == phone:
                print("This phone numbeer is already registered")
                return None
         
        new_user = User(name, phone, password)        
        Parking.users.append(new_user)
        print("Sign up successful!")
        return new_user

    def sign_in():
        phone = input("Enter your Phone numbner: ")
        password = input("Enter your password: ")
        for user in Parking.users:
            if isinstance(user, User) and user.phone == phone and user.password == password:
                return user
        else:
            print("invalid Phone number or password")
            return None
            

class Account:
    balance = 0
    cars = []

    def __init__(self, balance, cars):
        self.balance = balance
        self.cars = cars

    def deposit_money(self):
        amount = float(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print("Deposit successful. Current balance: $", self.balance)

    


class Car:
    car_name = ""
    car_plate = ""

    def __init__(self, car_name, car_plate):
        self.car_name = car_name
        self.car_plate = car_plate


    def add_vehicle():
        car_name = input("Enter the name of the car: ")
        car_plate = input("enter the plates of your car (AA-111-AA): ")
        new_car = Car(car_name, car_plate)
        Account.cars.append(new_car)
        print("Car successfully added!")


class Districts:
    def __init__(self, district_name, lots, price, occupied_lots):
        self.district_name = district_name
        self.lots = lots
        self.price = price
        self.occupied_lots = occupied_lots

    def start_parking(self, account, car):
        if not self.lots:
            print(f"No available lots in {self.district_name}.")
            return

        print(f"Available lots in {self.district_name}: {self.lots}")

        lot_choice = input("Choose a lot to park: ")
        try:
            lot_choice = int(lot_choice)
            if lot_choice not in self.lots:
                print("Invalid lot choice.")
                return

            print(f"{car.car_name} with plate {car.car_plate} parked successfully in lot {lot_choice} of {self.district_name}")
            self.occupied_lots.append(lot_choice)
            self.lots.remove(lot_choice)

            start_time = time.time()
            while True:
                input_msg = "Type 'end' to end parking: "
                if time.time() - start_time <= 10:
                    input_msg = "Type 'end' to end parking (First 10 seconds free): "
                end_parking = input(input_msg)
                if end_parking.lower() == 'end':
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    parking_fee = max(0, (elapsed_time - 10) / 60 * self.price)  # Parking fee after the first 10 seconds
                    print("Parking stopped.")
                    if parking_fee > 0:
                        print(f"Parking fee: ${parking_fee:.2f}")
                        account.balance -= parking_fee
                        print(f"Remaining balance: ${account.balance:.2f}")
                    break
                else:
                    print("Invalid input. Please type 'end' to end parking.")
        except ValueError:
            print("Invalid input. Please enter a valid lot number.")

saburtalo = Districts("Saburtalo", [1001, 1002, 1003, 1004], 0.10, [])
vake = Districts("Vake", [2001, 2002, 2003, 3004], 0.10, [])
rustaveli = Districts("Rustaveli", [3001, 3002, 3003, 3004], 0.10, [])
marjanishvili = Districts("Marjanishvili", [4001, 4002, 4003, 4004], 0.10, [])
sanzona = Districts("Sanzona", [5001, 5002, 5003, 5004], 0.10, [])
gldani = Districts("Gldani", [6001, 6002, 6003, 6004], 0.10, [])




def main():
    print("hello")
    while True:
        choice = input("To sign in type (1) To sign up type (2) To exit type (3): ")
        if choice == "1":
            logged_in_user = User.sign_in()
            
            while logged_in_user:
                print("User logged in:", logged_in_user.name)
                lgdin_choice = input(("Do you want to use existing vehicle (1) add vehicle (2) deposit money (3) exit (4): "))
                if lgdin_choice == "1":
                    if not Account.cars:
                        print("You have no cars added.")
                    else:
                        print("Your cars:")
                        for i, car in enumerate(Account.cars, 1):
                            print(f"{i}. {car.car_name} - {car.car_plate}")
                        car_choice = input("Select a car to park: ")
                        try:
                            car_choice = int(car_choice)
                            selected_car = Account.cars[car_choice - 1]
                            district_choice = input("Choose the district you are parking in (1.Saburtalo 2.Vake 3.Rustaveli 4.Marjanishvili 5.Sanzona 6.Gldani): ")
                            districts = {"1": saburtalo, "2": vake, "3": rustaveli, "4": marjanishvili, "5": sanzona, "6": gldani}
                            if district_choice in districts:
                                chosen_district = districts[district_choice]
                                balancee = Account.balance
                                chosen_district.start_parking(logged_in_user, selected_car )
                            else:
                                print("Invalid choice.")
                        except (ValueError, IndexError):
                            print("Invalid car choice")
                    

                elif lgdin_choice == "2":
                    vehicle1 = Car.add_vehicle()

                elif lgdin_choice == "3":
                    account = Account(0,[])
                    account.deposit_money()
                else:
                    break    
            else:
                break
        elif choice == "2":
           
            User1 = User.sign_up()

        else:
            ("see youu soon")
            break

main()


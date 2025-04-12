class Smartphone:
    def __init__(self, brand, model, price, battery_capacity):
        self.brand = brand
        self.model = model
        self.price = price
        self.__battery_capacity = battery_capacity 

    def get_battery_capacity(self):
        return self.__battery_capacity

    def set_battery_capacity(self, capacity):
        if capacity > 0:
            self.__battery_capacity = capacity
        else:
            print("Battery capacity must be positive!")

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
    
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, battery_capacity, gpu):
        super().__init__(brand, model, price, battery_capacity)
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.model} with {self.gpu} GPU.")

    def __str__(self):
        return f"{super().__str__()} (Gaming Edition with {self.gpu} GPU)"


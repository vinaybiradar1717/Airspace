import airline

class Hotel():

    hotels = {
        'A': {
            'price': 1500,
            'availale': 3
        },
        'B': {
            'price': 2500,
            'availale': 3
        },
        'C': {
            'price': 3500,
            'availale': 3
        }
    }

    total_price = 0

    def __init__(self):
        print("Welcome to SKYHIGH HOTELS")

    def book_rooms(self):
        total_rooms = int(input("How many rooms you want to book: "))
        while total_rooms:

            print(self.hotels)
            user_hotel = str(input("Choose a hotel: "))

            if user_hotel.upper() in self.hotels.keys() and self.hotels[user_hotel.upper()]['availale']>0:
                self.total_price += self.hotels[user_hotel.upper()]['price']
                self.hotels[user_hotel.upper()]['availale'] -= 1
            
            total_rooms -= 1    

        # print(self.total_price)


# hotel = Hotel()
# hotel.book_rooms()
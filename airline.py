
class Airline():

    seats = {
        'economy': {
            'price': 2000,
            'available': 20
        },
        'business': {
            'price': 4500,
            'available': 6
        }
    }

    price_paid = 0

    def __init__(self):
        print("Welcome to SKYHIGH airlines")

    def book_seat(self):
        tickets_to_book = int(input("How many tickets you want to book: "))
        while tickets_to_book:
            print(self.seats)
            seat = int(input("which ticket you want to book, press 1 for economy, press 2 for business: "))

            if seat == 1 and self.seats['economy']['available'] > 0:
                self.price_paid += self.seats['economy']['price']
                self.seats['economy']['available'] -= 1
                print("you booked 1 economy class ticket.")

            elif seat == 2 and self.seats['business']['available'] > 0:
                self.price_paid += self.seats['business']['price']
                self.seats['business']['available'] -= 1
                print("you booked 1 business class ticket.")

            else:
                print("Please enter correct option.")
            tickets_to_book -= 1

        # print(f"Total amount paid: {self.price_paid}")
        


# airline = Airline()
# airline.book_seat()
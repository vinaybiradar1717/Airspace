import airline
import hotels

class Booking():

    total_amount_to_be_paid = 0

    def __init__(self):
        print("WELCOME")

    def book(self):
        air_line = airline.Airline()
        air_line.book_seat()

        book_hotel = int(input("Would you like to book hotel ? Press 1 for YES, Press 0 NO: "))
        if book_hotel:
            hotel = hotels.Hotel()
            hotel.book_rooms()
        self.total_amount_to_be_paid = air_line.price_paid + hotel.total_price
        print(f"Total amount to be paid is: Rs {self.total_amount_to_be_paid}")

booking = Booking()
booking.book()
    
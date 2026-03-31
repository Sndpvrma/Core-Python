from Exception_Ticket_booking import TicketBookingException


class Ticket_Booking_Exception(Exception):
    def __init__(self, message):
        super().__init__(message)

class Booking:
    def __init__(self):
        self.ticket = 0

    def set_ticket(self, ticket):
        self.ticket = ticket
    def get_ticket(self):
        return self.ticket

    def book_ticket(self, ticket):
        if ticket > 2:
            raise TicketBookingException("You can not book more than 2 tickets")

        if ticket > self.ticket:
            raise TicketBookingException("Not enough tickets available")

        if self.ticket - ticket < 1:
            raise TicketBookingException("At least one ticket must be remain")

        self.ticket -= ticket
        print(f"Booking Successful {ticket} tickets booked, remaining ticket {self.ticket}")

Bkg = Booking()
Bkg.set_ticket(5)

try:
    Bkg.book_ticket(2)
    Bkg.book_ticket(1)
    Bkg.book_ticket(2)

except TicketBookingException as e:
    print("Error Occurred", e)
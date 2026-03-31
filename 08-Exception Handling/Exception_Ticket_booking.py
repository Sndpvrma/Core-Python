class TicketBookingException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Booking:
    def __init__(self):
        self.ticket = 0

    def set_ticket(self, ticket):
        self.ticket = ticket
    def get_ticket(self):
        return self.ticket

    def book_ticket(self, tickets):
        if tickets > 2:
            raise TicketBookingException("You can't book more than 2 tickets")

        if tickets > self.ticket:
            raise TicketBookingException("Not enough tickets available")

        if self.ticket - tickets < 1:
            raise TicketBookingException("At least 1 ticket must remain")

        self.ticket -= tickets
        print(f"Booking successful: {tickets} tickets booked, Remaining Tickets: {self.ticket}")

Bkg = Booking()
Bkg.set_ticket(5)

try:
    Bkg.book_ticket(2)
    Bkg.book_ticket(1)
    Bkg.book_ticket(2)

except TicketBookingException as e:
    print("Error Occurred:", e)
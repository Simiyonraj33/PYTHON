class Ticket:
    total_sold = 0
    total_seats = 100

    def __init__(self, name, train, seat, price):
        self.name = name
        self.train = train
        self.seat = seat
        self.price = price
        Ticket.total_sold += 1

    def details(self):
        return (f"Name: {self.name}\n"
                f"Train: {self.train}\n"
                f"Seat: {self.seat}\n"
                f"Price: Rs.{self.price:.2f}")

    @classmethod
    def remaining_seats(cls):
        return cls.total_seats - cls.total_sold

    @staticmethod
    def total_tickets():
        return Ticket.total_sold


while True:
    if Ticket.remaining_seats() <= 0:
        print("No more seats available.")
        break

    name = input("Passenger name: ")
    train = input("Train number: ")
    seat = input("Seat number: ")
    price = float(input("Ticket price: "))

    ticket = Ticket(name, train, seat, price)

    print("\nTicket Details:")
    print(ticket.details())
    print("-----")

    another = input("Create another ticket? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print(f"\nTotal tickets sold: {Ticket.total_tickets()}")
print(f"Remaining seats: {Ticket.remaining_seats()}")

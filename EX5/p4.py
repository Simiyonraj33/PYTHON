class InvalidPriceError(Exception):
   def __init__(self,message="Invalid price: The ticket price must be a non negative number"):
      self.message=message
class Ticket:
   total_sold=0
   total_seats=1000
   def __init__(self,name,screen,seat,price):
      self.name=name
      self.screen=screen
      self.seat=seat
      self.price=price
      Ticket.total_sold+=1
   def details(self):
      print(f"Movie name:{self.name}\n"
	    f"screen:{self.screen}\n"
	    f"Seat:{self.seat}\n"
	    f"Price:Rs.{self.price:.2f}")
   @classmethod
   def remaining_seats(cls):
      return cls.total_seats-cls.total_sold
   @staticmethod
   def total_tickets():
      return Ticket.total_sold
while True:
   if Ticket.remaining_seats()<0:
      print("No more seats available")
      break
   name=input("Movie name:")
   screen=input("Screen:")
   seat=input("Seat Number:")
   while True:
      try:
         price=float(input("Ticket price:"))
         if price<0:
            raise InvalidPriceError()
         break
      except ValueError:
         print("Invalid input for price:Please enter a valid number")
      except InvalidPriceError as e:
         print(e.message)
   ticket=Ticket(name,screen,seat,price)
   print("\n Ticket Details:")
   print(ticket.details())
   print("--------------------")
   another=input("Book Another Ticket?(yes/no):").strip().lower()
   if another!='yes':
      break
print(f"\n Total Tickets sold:{Ticket.total_tickets()}")
print(f"Remaining seats:{Ticket.remaining_seats()}")


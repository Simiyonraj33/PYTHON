class Theatre:
   def __init__ (self,theatre_name,location):
      self.theatre_name=theatre_name
      self.location=location
      self.total_seats=100
      self.tickets=[]
   def display_info(self):
      return(f"welcome to {self.theatre_name} theatre!\n"f"location:{self.location}\n"f"total seats:{self.total_seats}\n")
   class Ticket:
      def __init__(self,name,screen,seat,price):
         self.name=name
         self.screen=screen
         self.seat=seat
         self.price=price
      def details(self):
         return(f"movie name:{self.name}\n"f"screen:{self.screen}\n"f"seat:{self.seat}\n"f"price:Rs.{self.price:.2f}")
   def book_ticket(self,name,screen,seat,price):
      if len(self.tickets)<self.total_seats:
         ticket=self.Ticket(name,screen,seat,price)
         self.tickets.append(ticket)
         return ticket
      else:
         return None
   def tickets_sold(self):
      return len(self.tickets)
   def seats_left(self):
      return self.total_seats-len(self.tickets)
   
theatre=Theatre("MAX SCREENS","APK")
print(theatre.display_info())
while True:
   if theatre.seats_left()<=0:
      print("no more seats available.")
      break
   name=input("Enter Movie Name:")
   screen=input("Enter Screen Number:")
   seat=input("Enter Seat Number:")
   price=float(input("Enter Ticket Price:Rs"))
   ticket=theatre.book_ticket(name,screen,seat,price)
   if ticket:
      print("\n TICKET BOOKED SUCESSFULLY")
      print(ticket.details())
      print("--------------------------")
   else:
      print("Booking Failed.no seats left.")
      break
   another=input("book another ticket?(yes/no):").strip().lower()
   if another!="yes":
      break
print(f"\n Total Tickets sold:{theatre.tickets_sold()}")
print(f"Remaining seats:{theatre.seats_left()}")

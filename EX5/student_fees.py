class StudentBill:
    def __init__(self, name, category, city=None, food_type=None):
        self.name = name
        self.category = category.lower()
        self.city = city
        self.food_type = food_type.lower() if food_type else None
        
        # Default college fees
        self.tuition_fee = 80000
        self.placement_fee = 20000
        self.lab_fees = 10000

    def calculate_bill(self):
        total_college_fees = self.tuition_fee + self.placement_fee + self.lab_fees
        
        if self.category == "dayscholar":
            bus_charges = {
                "madurai": 30000,
                "sivakasi": 10000,
                "virudhunagar": 20000
            }
            bill = bus_charges.get(self.city.lower(), 0)
            total_amount = total_college_fees + bill
            print(f"Total bill for {self.name} (Dayscholar from {self.city}): Rs. {total_amount}")
        
        elif self.category == "hosteller":
            veg_mess = 20000
            non_veg_mess = 25000
            
            if self.food_type == "veg":
                food_bill = veg_mess
            elif self.food_type == "non veg":
                food_bill = non_veg_mess
            else:
                food_bill = 0
                print("Invalid food type provided.")
            
            total_amount = total_college_fees + food_bill
            print(f"Total bill for {self.name} (Hosteller - {self.food_type}): Rs. {total_amount}")
        
        else:
            print("Invalid category provided.")

# Get input from the user
name = input("Enter the student's name: ")
category = input("Enter the category (dayscholar/hosteller): ")

city = None
food_type = None

if category.lower() == "dayscholar":
    city = input("Enter the city (Madurai/Sivakasi/Virudhunagar): ")
elif category.lower() == "hosteller":
    food_type = input("Enter the food type (veg/non veg): ")

# Create a StudentBill instance with user input
student = StudentBill(name, category, city, food_type)
student.calculate_bill()

print(" Airline Booking ")

ticket = 30000

class_type = input("Class (economy/business): ").lower()
baggage = float(input("Baggage (kg): "))
meal = input("Meal Required (yes/no): ").lower()

if class_type == "business":
    ticket += 20000

if baggage > 20:
    ticket += (baggage - 20) * 1000

if meal == "yes":
    ticket += 1500

print("Total Ticket Price:", ticket)
import time 
car_fleet = {
    "C101": {"model": "Sedan", "daily_rate": 500.00, "status": "Available"},
    "C202": {"model": "SUV", "daily_rate": 665.00, "status": "Available"},
    "C303": {"model": "Van", "daily_rate": 200.00, "status": "Available"},
    "C404": {"model": "Alto", "daily_rate": 400.00, "status": "Rented"},
}
rental_records = {}
next_rental_id = 1 

def display_available_cars():
    print("\n" + "="*60)
    print("           AVAILABLE CARS FOR RENT ")
    print("="*60)
    print(f"{'ID':<6} | {'Model':<25} | {'Rate (per Day)':<15} | {'Status':<10}")
    print("-" * 60)
    for car_id, details in car_fleet.items():
        if details["status"] == "Available":
            rate = details["daily_rate"]
            print(f"{car_id:<6} | {details['model']:<25} | Rs.{rate:<14.2f} | {details['status']:<10}")
    print("="*60)

def rent_car():
    global next_rental_id
    
    display_available_cars()
    
    car_id = input("Enter the ID of the car you want to rent (e.g., C101): ").strip().upper()
    
    if car_id not in car_fleet:
        print(f" Sorry, we don't have a car with the ID '{car_id}'. Please check the list.")
        return

    car = car_fleet[car_id]
    
    if car["status"] != "Available":
        print(f"Warning: The {car['model']} (ID: {car_id}) is currently {car['status']}. Try another one.")
        return
        
    customer_name = input("Please enter your full name for the record: ").strip()
    
    while True:
        try:
            duration_days = int(input("How many days will you rent the car for? "))
            if duration_days > 0:
                break
            else:
                print("Duration must be at least 1 day.")
        except ValueError:
            print("Invalid input. Please enter a whole number for the days.")

    total_estimate = car["daily_rate"] * duration_days
    car["status"] = "Rented"
    rental_id = next_rental_id
    rental_records[rental_id] = { 
        "car_id": car_id,
        "customer": customer_name,
        "days": duration_days,
        "rented_at": time.time(),
        "estimated_cost": total_estimate
    }
    next_rental_id += 1 
    print("\n" + " "*10)
    print(f"          RENTAL CONFIRMED! (ID: {rental_id})")
    print(f"Customer: {customer_name}")
    print(f"Car Rented: {car['model']} (ID: {car_id})")
    print(f"Rental Duration: {duration_days} days")
    print(f"Daily Rate: Rs.{car['daily_rate']:.2f}")
    print(f"\nESTIMATED TOTAL: Rs.{total_estimate:.2f}")
    print("Please pick up your keys at the counter. Enjoy the drive!")

def return_car():
    rental_id_input = input("Enter the Rental ID to process the return: ").strip()
    
    try:
        rental_id = int(rental_id_input)
    except ValueError:
        print("Invalid input. Rental ID must be a number.")
        return

    record = rental_records.get(rental_id)
    if not record:
        print(f"Error: Rental ID {rental_id} not found in our system.")
        return
    
    car_id = record["car_id"]
    car = car_fleet[car_id]
    
    if car["status"] == "Available":
         print(f"Warning: Car {car_id} is already marked as available. Return likely already processed.")
         return

    final_bill = record["estimated_cost"] 

    car["status"] = "Available"
    print("\n" + "-"*10)
    print(f"          RETURN PROCESSED! ")
    print("-"*10)
    print(f"Customer: {record['customer']}")
    print(f"Car Returned: {car['model']} (ID: {car_id})")
    print(f"Original Rental Days: {record['days']}")
    print(f"FINAL BILL CHARGED: Rs.{final_bill:.2f}")
    print("\nThank you for choosing us! See you next time.")

def run_rental_system():

    print("\n\n Welcome to the Simple Python Car Rental Service!")
    
    while True:
        print("\n" + "="*30)
        print("What would you like to do today?")
        print("1. See available cars")
        print("2. Rent a car")
        print("3. Return a car (and pay the bill)")
        print("4. Exit the system")
        print("="*30)

        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

        if choice == '1':
            display_available_cars() 
        
        elif choice == '2':
            rent_car()
            
        elif choice == '3':
            return_car() 
            
        elif choice == '4':
            print("System shutting down. Goodbye!")
            break

        else:
            print("I don't understand that choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    run_rental_system()

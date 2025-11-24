# Car-Rental-Service
# Car Rental System: 

Welcome to the **"Keys Please!"** system! Think of this as your digital assistant for running a small car rental business. It's a simple program built with Python that runs right in your computer's terminal (or command line).

 no fancy databases—just a straightforward way to track which cars are out, who rented them, and when to expect them back.

(The Features)

This system keeps your rental process quick and honest:

* **Spot the Open Cars:** Instantly see a neat list of every car that's **ready to go**, along with its price per day. No more frantic searching!
* **Easy Checkout:** Process a new rental in seconds. Just tell the system which car, who the customer is, and how many days they're keeping it.
* **Instant Quote:** It automatically calculates the **estimated total cost** so you can tell the customer their bill upfront.
* **Simple Returns:** When a car comes back, you just enter the rental's ID number. The system marks the car as **Available** and confirms the final bill.
* **Super Easy to Use:** Everything is done through a simple numbered menu.

## The Tech Stuff 

| What We Used | Why We Used It |
| :--- | :--- |
| **Python 3** | The friendly programming language that makes everything run. |
| **Dictionaries** | These are like digital filing cabinets that hold all your car data (`car_fleet`) and customer records (`rental_records`). |
| **The `time` library** | Just a tiny piece of code to timestamp when a car goes out. |

##(How to Run It)

It takes about 30 seconds to get this thing rolling:

1.  **Save the File:** Take the code and save it on your computer as a file named `rental_system.py`.
2.  **Open Your Terminal:** Launch your command prompt (Windows) or Terminal (Mac/Linux).
3.  **Go to the Folder:** Navigate to where you saved the file.
4.  **Launch the System:** Type this command and hit Enter:

    ```bash
    python rental_system.py
    ```
5.  You'll see the main menu pop up, and you're good to go!

##  (How to Check It Works)

We need to make sure the gears are turning smoothly. Try this sequence:

1.  **Check Availability (Menu Option 1):** Make sure you see the Sedan, SUV, and Van, but NOT the Alto (because it's already marked as rented in the system).
2.  **Rent a Car (Menu Option 2):**
    * Choose an available car (e.g., C303).
    * Enter a name (e.g., "Jane Doe") and a rental duration (e.g., 2 days).
    * Confirm the total estimated price is correct (Rs.400.00).
3.  **Process the Return (Menu Option 3):**
    * The Rental ID should be **1** (since it's the first one you processed).
    * Enter `1` and confirm the return is successful and the final bill is Rs.400.00.
4.  **Final Check:** Run Option 1 again. The C303 Van should now be back in the **Available** list!

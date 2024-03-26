# This program wil calculate a user's total holiday cost (plane cost, 
# hotel cost and car-rental cost)

# Create a city options dictionary with corresponding plane costs.
city_options = {
        "1": ("Barbados", 550),
        "2": ("Oslo", 200),
        "3": ("New York", 375)
}

# Get user input for city selection.
while True:
        city_flight = input("Please select the city you will be flying "
                            "to (Enter a number option (1 to 3):"
                            "\n1. Barbados\n2. Oslo\n3. New York\n")

        if city_flight.isdigit() and 1 <= int(city_flight) <= 3:
            city_flight = str (city_flight)
            city, plane_cost = city_options[city_flight]
            break
        else:
            print ("Invalid number provided. Please enter a number from "
                   "the options provided")  


# Get user input for number of nights and rental days
while True:
        num_nights = input("Please enter the number of nights you will "
                           "be staying at a hotel: ")

        if num_nights.isdigit():
            num_nights = int (num_nights)
            break
        else:
            print ("Invalid number provided. Please enter a valid number "
                   " of nights")


while True:
        rental_days = input("Please enter the number of days you will be "
                            "hiring a car for: ")

        if rental_days.isdigit():
            rental_days = int (rental_days)
            break
        else:
            print ("Invalid number provided. Please enter a valid number "
                   "of rental days")


# Calculate hotel cost
hotel_nightly_rate = 64
total_hotel_cost = num_nights * hotel_nightly_rate

# Calculate car rental cost
car_rental_daily_rate = 27
total_car_rental = rental_days * car_rental_daily_rate

# Calculate total holiday cost
total_cost_holiday = total_hotel_cost + plane_cost + total_car_rental


# print out the details of the holiday
print (f"The hotel cost in {city} is {total_hotel_cost}.")
print (f"The plane cost to {city} is {plane_cost}.")
print (f"The car rental cost in {city} is {total_car_rental}.")
print (f"The total cost of the holiday in {city} is {total_cost_holiday}.")
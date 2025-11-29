# Create User-defined function for hotel cost
def hotel_cost(nights, rate=139.00):
    return nights * rate


# Create User-defined function for plane cost
def plane_cost(city):
    city = city.lower()
    if city == "chicago":
        return 585.25
    elif city == "new york":
        return 917.64
    elif city == "los angeles":
        return 713.92
    else:
        return "invalid city"


# Create User-defined function for car rental cost
def car_rental(days, rate=90.00):
    return days * rate


# Create User-defined function for total holiday cost
def holiday_cost(city, nights, days):
    flight = plane_cost(city)
    total = (hotel_cost(nights) + car_rental(days) + flight)
    return total


# Input for Vacation details
city_flight = input("Which of these cities will you be flying to?\n"
                    "Chicago, New York, or Los Angeles: ").lower()

num_nights = float(input("How many nights will you be staying for? "))

rental_days = float(input("How many days will you be needing a rental car? "))

# Output for Vacation details
print(
    f"The cost of your flight to {city_flight} will be: \
    ${plane_cost(city_flight)}"
    )

print(
    f"Your hotel cost for {num_nights} nights will be: \
    ${hotel_cost(num_nights)}"
    )

print(
    f"Your car rental for {rental_days} days will be: \
    ${car_rental(rental_days)}"
    )

print(
    f"The total holiday cost for your trip will be: \
    ${holiday_cost(city_flight, num_nights, rental_days)}"
    )

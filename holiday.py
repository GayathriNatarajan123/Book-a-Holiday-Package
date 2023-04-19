#  =================Task 16================
# Author: Gayathri
# Created Date: 17/04/2023
# Reference: example.py, W3schools, https://pypi.org/project/tabulate/
# This is a Python program, the purpose of this program is to calculate holiday package.
# Displaying the list of available cities, flights, hotels and car to hire.
# Adding functions for receving the data to display.
# Added function to Set the validation to receive only int value to get the number of nights to stay in hotel and number of day to hire car.
# Added function to Set the validation to receive values from user only from the given options.
# Added function to calculate the cost.
# Finally displaying the invoice.
# Added defensive programing.
# imported the datastructure module created for this project and importing tabulate to display the data in table format.
#  ======================================

import holiday_datastructures as holiday_ds
import tabulate as display

lst_flight = []
lst_hotel = []
lst_car_rental = []

city_message = "\nPlease enter the serial number of the destination city you would like to travel, from the above list only: "
flight_message = "\nPlease enter the serial number of the flight you would like to travel, from the above list only: "
hotel_message = "\nPlease enter the serial number of the hotel you would like to stay, from the above list only: "
car_message = "\nPlease enter the serial number of the car you would like to rent, from the above list only: "

# -------Function to Validate user inputs------------
def validate(user_input, lst, message):
    ''' Validates if user enters the value available from the list

    Parameters:
    user_input --  input that user enters.
    lst        --  list based on which user make the selection.
    message    --  message to display to the user to input correct value.

    returns the correct value from the available option.
    '''
    while(True):
        try:
            num = validate_number(user_input)
            if(num > len(lst) or num == 0):
                user_input = input(message)
            else:
                for eachrow in lst:
                        if(str(num) in eachrow[0]):
                            return str(num)
        except KeyError:
            user_input = input(message)

# Validates the entered values are numeric
def validate_number(number_to_validate):
    ''' validate to check whether user returns only numeric value from 1 and above.
        Make the user to re-enter if the input is invalid.

        Parameter:
        number_to_validate -- number to validate

        returns the correct numeric value
    '''
    while(True):
        try:
            number_to_validate = int(number_to_validate)
            if(number_to_validate > 0):
                return number_to_validate
            else:
                number_to_validate = input("\nPlease enter only natural number(from 1): ")
        except ValueError:
            number_to_validate = input("\nPlease enter only natural number(from 1): ")

# -------Function to display the city, flight, hotel and cars to rent------------
def destination_details():
    ''' Get the list of city from the data structure
    
        returns the lst of city to display
    '''
    global lst_city
    lst_city = [[key, value]for key, value in holiday_ds.city.items()]        
    return lst_city

def flight_details(get_city):
    '''Get the list of flights based on the city from the data structure.

        Parameter:
        get_city -- user selected city

        returns the list of flights to display    
    '''
    global city_name
    city_name = holiday_ds.city[get_city]
    # Get the flight datastructure name
    flight_dsname = assign_dsvalue("flight")

    global lst_flight
    lst_flight = [[key, value[0], f"£{value[1]}"]for key, value in flight_dsname.items()]   
    return lst_flight

def hotel_details(num_nights):  
    '''Get the list of hotels based on the city from the data structure.

        Parameter:
        num_nights -- number of nights user is going to stay.

        returns the list of hotels to display    
    '''  
    hotel_dsname = assign_dsvalue("hotel")

    global lst_hotel
    lst_hotel = [[key, value[0], f"£{value[1]}", f"£{value[1]} * {num_nights} = £{value[1] * num_nights}"]for key, value in hotel_dsname.items()]   
    return lst_hotel
 
def car_rental_details(rental_days):   
    '''Get the list of cars to hire based on the city from the data structure.

        Parameter:
        rental_days -- number of days user is going to hire the car.

        returns the list of cars to display    
    '''   
    rental_cars_dsname = assign_dsvalue("car")       
    global lst_car_rental
    lst_car_rental = [[key, value[0], value[2], f"£{value[1]}", f"£{value[1]} * {rental_days} = £{value[1] * rental_days}"]for key, value in rental_cars_dsname.items()]   
                   
    return lst_car_rental

def assign_dsvalue(item):
    ''' Assign the datastructure based on the city and type of service.

        Parameter:
        item -- type of service, for which data structure is going to assign
        
        returns the data structure name.
    '''
    assign_ds = ""
    if(city_name == "Chennai"):
        if(item == "flight"):
            assign_ds = holiday_ds.flight_chennai
        elif(item == "hotel"):
            assign_ds = holiday_ds.hotel_chennai
        elif(item == "car"):
            assign_ds = holiday_ds.car_rental_chennai
    elif(city_name == "Paris"):
        if(item == "flight"):
            assign_ds = holiday_ds.flight_paris
        elif(item == "hotel"):
            assign_ds = holiday_ds.hotel_paris
        elif(item == "car"):
            assign_ds = holiday_ds.car_rental_paris
    elif(city_name == "Rome"):
        if(item == "flight"):
            assign_ds = holiday_ds.flight_rome
        elif(item == "hotel"):
            assign_ds = holiday_ds.hotel_rome
        elif(item == "car"):
            assign_ds = holiday_ds.car_rental_rome        
    elif(city_name == "London"):
        if(item == "flight"):
            assign_ds = holiday_ds.flight_london
        elif(item == "hotel"):
            assign_ds = holiday_ds.hotel_london
        elif(item == "car"):
            assign_ds = holiday_ds.car_rental_london
    elif(city_name == "Dublin"):
        if(item == "flight"):
            assign_ds = holiday_ds.flight_dublin
        elif(item == "hotel"):
            assign_ds = holiday_ds.hotel_dublin
        elif(item == "car"):
            assign_ds = holiday_ds.car_rental_dublin
    return assign_ds

# -------Function to calculate cost for flight, hotel and cars to rent.------------

def flight_cost(get_flight_nos):
    ''' Calculate the cost for the flight

        Parameter:
        get_flight_nos -- The serial numner of the flight that was selected by user.

        returns the selected flight's details as list and the round trip cost    
    '''
    roundtrip_flight_cost = ""
    lst_flight_items = []
    for item in lst_flight:
            if get_flight_nos in item[0]:
                cost = item[2].split("£")
                roundtrip_flight_cost = float(cost[1]) * 2
                
                lst_flight_items.append("1")
                lst_flight_items.append(item[1])
                lst_flight_items.append(f"£{roundtrip_flight_cost}")
                
    return lst_flight_items, roundtrip_flight_cost

def hotel_cost(get_hotel_nos):
    ''' Calculate the cost for the hotel stay

        Parameter:
        get_hotel_nos -- The serial numner of the hotel that was selected by user.

        returns the selected hotel's details as list and the total cost for hotel stay.
    '''
    total_hotel_cost = ""
    lst_hotel_items = []
    for item in lst_hotel:
            if get_hotel_nos in item[0]:
                cost = item[2].split("£")
                total_hotel_cost = float(cost[1]) * get_num_nights
                
                lst_hotel_items.append("2")
                lst_hotel_items.append(item[1])
                lst_hotel_items.append(f"£{total_hotel_cost}")
                
    return lst_hotel_items, total_hotel_cost

def car_rental(get_car_nos):
    ''' Calculate the cost for the car to hire

        Parameter:
        get_car_nos -- The serial numner of the car that was selected by user.

        returns the selected car's details as list and the total cost for car to hire.
    '''
    total_car_cost = ""
    lst_car_items = []
    for item in lst_car_rental:
            if get_car_nos in item[0]:
                cost = item[3].split("£")
                total_car_cost = float(cost[1]) * get_rental_days
                
                lst_car_items.append("3")
                lst_car_items.append(item[1])
                lst_car_items.append(f"£{total_car_cost}")
                
    return lst_car_items, total_car_cost

def holiday_cost(get_flight_nos, get_hotel_nos, get_car_nos):
    ''' Calculate the total holiday cost based on the selected flight, hotel and car.

        Parameter:
        get_flight_nos -- the serial number of the flight, selected by user.
        get_hotel_nos -- the serial number of the hotel, selected by user.
        get_car_nos -- the serial number of the car, selected by user.

        returns the total cost of the package.    
    '''    
    lst_all_items = []
    lst=[]
    #Gat the flight cost
    lst, roundtrip_flight_cost = flight_cost(get_flight_nos)
    lst_all_items.append(lst)
    #Gat the hotel cost
    lst, total_hotel_cost = hotel_cost(get_hotel_nos)
    lst_all_items.append(lst)
    #Gat the car cost
    lst, total_car_cost = car_rental(get_car_nos)
    lst_all_items.append(lst)

    lst = []
    lst.append("")
    lst.append("Total Net price")
    lst.append(f"£{roundtrip_flight_cost + total_hotel_cost + total_car_cost}")
    lst_all_items.append(lst)
    return lst_all_items

# Start of the program
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print("{:60}Plan your Holiday today".format(""))
print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

print("{:30}We help you to book the best quality and cheapest flights, hotel and rent a car.".format(""))
print("\nCurrently we are providing services to the below cities alone.\n")

# Display the Cities, for which services are provided.
headers=["S.NO", "Destination City"]
print(display.tabulate(destination_details(), headers, tablefmt="grid"))
get_city = validate(input(city_message), lst_city, city_message)
print("\n")

# Display the Flights, that are available.
headers=["S.NO", "Flight Name", "Price(One Way)"]
print(display.tabulate(flight_details(get_city), headers, tablefmt="grid"))
get_flight_nos = validate(input(flight_message), lst_flight, flight_message)

print("\n")
get_num_nights = validate_number(input("Please enter the number of nights you will stay at the hotel: "))
print("\n")

# Display the hotel that are available
headers=["S.NO", "Hotel Name", "Price per day", "Total Price"]
print(display.tabulate(hotel_details(get_num_nights), headers, tablefmt="grid"))
get_hotel_nos = validate(input(hotel_message), lst_hotel, hotel_message)
print("\n")
get_rental_days = validate_number(input("Please enter the number of days that you will hire a car: "))
print("\n")

# Display the cars available to rent.
headers=["S.NO", "Avaliable Rental Cars", "Seater", "Price per day", "Total Price"]
print(display.tabulate(car_rental_details(get_rental_days), headers, tablefmt="grid"))
get_car_nos = validate(input(car_message), lst_car_rental, car_message)

# Display the total cost for the holiday
total_cost = holiday_cost(get_flight_nos, get_hotel_nos, get_car_nos)
headers=["S.NO", f"Your Destination City - {city_name}", "Price incl VAT"]
print("\n")
print("{:20}Your Invoice:".format(""))
print(display.tabulate(total_cost, headers, tablefmt="rounded_grid"))
print("------------------------------------------------Thank you for using the application------------------------------------------------------------------\n")

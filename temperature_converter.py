"""Day 1 exercise: convert Celsius to Fahrenheit."""

# TODO 1: Ask the user for their name and store it in a variable.
nameInput = input("What is your Name :")
name =  str(nameInput)



# TODO 2: Ask for a Celsius temperature.
# Remember: input() returns a string, so convert it to a float.
celInput = input("what is current temperature in Celsius : ")
cel = float(celInput)

# TODO 3: Calculate the Fahrenheit temperature.
# Formula: (celsius * 9 / 5) + 32
Fahrenheit = round(float(((cel * 9)/5) + 32),1)

def is_freezing( celcius):
    if celcius <= 0:
        return "True"
    else:
        return "False"

# TODO 4: Print a friendly result using an f-string.
print(f'Name : {name}')
print(f'Current Celcius: {cel} ')
print(f'dateType of Celcius : {type(cel)}')
print(f'Temperature in Fahrenheit : {Fahrenheit}')
print(f'Is it freezing? : {is_freezing(cel)}')


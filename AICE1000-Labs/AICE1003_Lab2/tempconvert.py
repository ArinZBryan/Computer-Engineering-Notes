def convert_to_fahrenheit(celsius: int) -> int:
    fahrenheit = (1.8 * celsius) + 32
    return round(fahrenheit)

# Complete the definition of convert_to_celsius
def convert_to_celsius(fahrentheit : int) -> int: 
    celcius = (fahrentheit - 32) * 5/9
    return round(celcius)

celsius : str = input("Enter the Temperature in Celsius :")
print("Temperature in Fahrenheit :", convert_to_fahrenheit(int(celsius)))
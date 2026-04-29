"""Q  85: Convert Fahrenheit to Celsius
Write a function fahrenheit_to_celsius(fahrenheit) that accepts a 
temperature in Fahrenheit and converts it to Celsius.

"""
def fahrenheit_to_celsius(fahrenheit):
    tem=((fahrenheit-32)*5)/9
    return round(tem,2) # ye pont ke bad sirf do dijit dega
print(fahrenheit_to_celsius(99.2))
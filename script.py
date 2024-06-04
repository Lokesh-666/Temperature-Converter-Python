def CelsiusToFahrenheit(amount):
    convertedAmount = amount*9/5 + 32
    return convertedAmount

def FahrenheitToCelsius(amount):
    convertedAmount = (amount-32)*5/9
    return convertedAmount       


def main():
    
    print("Welcome to Temperature Converter")
    amount = float(input("Value of temperature that you wish to convert: "))
    unit = str(input("What is the unit of the temperature(C/F)?"))
    if unit.upper() == 'C':
        convertedAmount = CelsiusToFahrenheit(amount)
        print(amount, "℃  converted to ℉  is ", convertedAmount)

    elif unit.upper() == 'F':
        convertedAmount = FahrenheitToCelsius(amount)        
        print(amount, "℉  converted to ℃  is ", convertedAmount)
    else:
        print("Invalid Input! Please choose c/C/f/F")

if __name__ == "__main__":
    main()
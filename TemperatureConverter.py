#Python temperature converter

temperature = float(input("Enter temperature: "))
unit = input("Is it in Celsius (C) or Fahrenheit (F): ")

if unit.lower() == "c":
    convertedTemp = (temperature * (9/5)) + 32
    unit = "F"
    print("Converted temperature: ",round(convertedTemp,1), unit)
elif unit.lower() == "f":
    convertedTemp = (5/9) * (temperature - 32)
    unit = "C"
    print("Converted temperature: ",round(convertedTemp,1), unit)
else:
    print(f"Unit \"{unit}\" is invalid")
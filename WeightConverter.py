#Python weight converter

weight = float(input("Enter weight: "))
unit = input("Is it in Kilograms (K) or Pounds (L): ")

if unit.lower() == "k":
    convertedWeight = weight * 2.205
    unit = "lbs"
    print("Converted weight: ",round(convertedWeight,1), unit)
elif unit.lower() == "l":
    convertedWeight = weight / 2.205
    unit = "kgs"
    print("Converted weight: ",round(convertedWeight,1), unit)
else:
    print(f"Unit \"{unit}\" is invalid")


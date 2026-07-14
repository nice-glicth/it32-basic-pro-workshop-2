Name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
power = int(input("Enter your power level: "))
Money = float(input("Enter your money in Baht: "))



if age < 18 or height < 150 or power < 5 or Money < 1000:
    print("You are a เด็กร้างรถ.")
else:
    print("You are a มหาราชามหารานี.")
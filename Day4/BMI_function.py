def BMI (height, weight):
    print("Enter your height in cm: ")
    height = int(input())
    print("Enter your weight in kg: ")      
    weight = int(input())
    bmi = weight / ((height/100) ** 2)
    print("Your BMI is: ", bmi)

BMI(0, 0)
# BMI Calculator

weight= float(input('Enter Weight in KG: '))
height= float(input('Enter height in Meters: '))
bmi= weight/(height*height)

print('BMI: ', bmi)
if bmi<18.5:
    print('Underweight')
elif bmi>= 18.5 and bmi<=24.9:
    print('Normal')
elif bmi >= 24.9 and bmi<= 29.9:
    print('OverWeight')
else:
    print('Obese')
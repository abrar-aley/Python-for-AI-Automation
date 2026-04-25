# task 2 Country Quizz game

import random

countries = {
    "Pakistan": "Islamabad",
    "India": "Delhi",
    "China": "Beijing",
    "Iran": "Tehran",
    "Turkey": "Ankara",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "Brazil": "Brasilia"
}

score = 0
questions = 5   

country_list = list(countries.keys())

for i in range(questions):
    country = random.choice(country_list)
    answer = input(f"What is the capital of {country}? ")

    if answer.lower() == countries[country].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", countries[country])

    print()

print("Quiz Finished!")
print("Your score:", score, "/", questions)
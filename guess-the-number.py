#Importing random module
import random 

#Randomly picking a number
num = random.randint(1,100)

#Welcome Messages
print("Welcome to The Guessing Game")
print("I am currently thinking of a number between 1 and 100")
print("You are COLD if you are more than 10 away from the number I am thinking of")
print("You are WARM if you are within 10 from the number I am thinking of")
print("You are COLDER, If you guess farther away from your most recent guess ")
print("You are WARMER, If you guess closer to your most recent guess")
print("Let's Start")

#List to keep track of guesses 
guess = [0]

while True:
    user_input = int(input("I am thinking of a number between 1 and 100, Enter your guess: "))
    
    #When user enters a number greater than 100 or less than 1
    if user_input > 100 or user_input < 1:
        print("Out of Bounds, Try again")
        continue
    
    #When user guesses correctly
    if user_input == num:
        print(f"Congratulations, You have guessed correctly in only {len(guess)} guesses")
        break

    guess.append(user_input)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    #And directly moves down to the else condition
    if guess[-2]:
        if abs(num - user_input) < abs(num - guess[-2]):
            print('Warmer')
        else:
            print("Colder")
    
    #Checks if number is within 10 of num
    else:
        if abs(num - user_input) <=10 :
            print("Warm")
        elif abs(num - user_input) > 10:
            print('Cold')

    

import random
print('                                                                Welcome to the number guessing game ')

upper_bound = input("Please type in any number: ")
if upper_bound.isdigit():
    upper_bound = int(upper_bound)
    if upper_bound <= 0:
        print("Please pick a number GREATER than 0")
        quit()
else:
    print("Please type in a number,preferably an integer i.e 1,2,3,4 etc..")
    quit()

random_number = random.randint(0 , upper_bound)
while True:
            user_guess = input('Pick a number between 0 and ' + str(upper_bound) + ': ')
            if user_guess.isdigit():
                user_guess = int(user_guess)
                if user_guess <= 0:
                    print("Please type a number greater than 0 ")
                    quit()
            else:
                print("Please type a number")
                continue


            if user_guess == random_number:
                print("You got it!!")
                exit()
            elif user_guess < random_number:
                print('Try a bigger number than the one you guessed')
            else:
                print('Try a smaller number than the one you guessed')

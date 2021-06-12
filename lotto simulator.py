import random

chosen_lotto_one = random.randint(1, 50)
chosen_lotto_two = random.randint(1, 50)
chosen_lotto_three = random.randint(1, 50)
chosen_lotto_four = random.randint(1, 50)
chosen_lotto_five = random.randint(1, 50)
chosen_lotto_six = random.randint(1, 50)
bonus_number = random.randint(1, 11)

your_choice_one = int(input("Enter your first number from the lotto (1 through 49): "))
your_choice_two = int(input("Enter your first number from the lotto (1 through 49): "))
your_choice_three = int(input("Enter your first number from the lotto (1 through 49): "))
your_choice_four = int(input("Enter your first number from the lotto (1 through 49): "))
your_choice_five = int(input("Enter your first number from the lotto (1 through 49): "))
your_choice_six = int(input("Enter your first number from the lotto (1 through 49): "))
your_bonus_number = int(input("Enter your bonus number (1 through 10): "))

print("The chosen numbers are: ", chosen_lotto_one, chosen_lotto_two, chosen_lotto_three, chosen_lotto_four, chosen_lotto_five, chosen_lotto_six)
print("The bonus number is: ", bonus_number)

random_thingy = 0

if your_choice_one == chosen_lotto_one:
    random_thingy += 1 
else:
    pass

if your_choice_two == chosen_lotto_two:
    random_thingy += 1
else:
    pass

if your_choice_three == chosen_lotto_three:
    random_thingy += 1
else:
    pass

if your_choice_four == chosen_lotto_four:
    random_thingy += 1
else:
    pass

if your_choice_five == chosen_lotto_five:
    random_thingy += 1
else:
    pass

if your_choice_six == chosen_lotto_six:
    random_thingy += 1
else:
    pass

bonus_number_thingy = 0

if bonus_number == your_bonus_number:
    bonus_number_thingy += 1

if random_thingy == 0:
    print("You got none correct, better luck next time")
elif random_thingy == 1:
    print("Good job, you got one correct")
elif random_thingy == 2:
    print("Good job, you got TWO correct")
elif random_thingy == 3:
    print("Good job, you got THREE correct!")
elif random_thingy == 4:
    print("Nice, you got FOUR correct!")
elif random_thingy == 5:
    print("Nice, you got FIVE correct!")
elif random_thingy == 6:
    print("We have a WINNER!!!!!!")

if bonus_number_thingy == 1:
    print("You got the bonus number correct!")
else:
    print("You didn't get the bonus number right.")

import random
number = random.randint(1,1000)

attempts = 0
max_attempts = 10

while attempts < max_attempts:

    guess = int(input("Enter number: "))

    attempts += 1

    if guess == number:
        print("Win!")
        print("attempts", attempts)
        break

    elif guess < number:
        print("The selected number is larger!")

    else:
        print("The chosen number is smaller!")

else:
    print("You lost.")
    
    print("Number selected by the system:", number)
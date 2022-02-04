import random

number = random.randint(1,10)

count = 0
guess = 0
print("Guess a number between 1 to 10: ")
while guess != number:
    count += 1
    
    guess = input(f'Enter Guess #{count}: ')
    if guess.isnumeric():
        guess = int(guess)
        if guess > number:
            print('Your guess is too high') 
        elif guess < number:
            print('Your guess is too low')
        else:
            continue 
    else:
      print('Numbers only! please :)')
 
else:
    print(f"you've guessed it correctly in {count} times")
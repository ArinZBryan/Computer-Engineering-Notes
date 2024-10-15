# Do NOT include this in the submitted answer
import random
random.seed(42)
number = random.randint(1, 50)

# Submit only the game logic below
guess = int(input('Guess a number: '))
guess_count = 1
while guess != number:
    if guess < number: 
        print('Too Low')
    if guess > number: 
        print('Too High')
    guess = int(input('Guess another number: '))
    guess_count += 1

print('Correct!')
print(f"Number of guesses taken: {guess_count}")
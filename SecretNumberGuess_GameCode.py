# secret number guess

import random

print('Hello ,whats ur name ?')
name = input()
print('Well,'+name+',I amthinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for i in range(1,6):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
         print('Your guess is too low')
    elif guess > secretNumber:
         print('Your guess is too high')
    else:
         break

if guess == secretNumber:
    print('Good job, '+name+',you guessed my number in ,'+str(i)+',guesses !')
else:
    print('Nope. The number i was thinking of was,'+str(secretNumber))

import random

while 1:
    n = random.randint(0, 10)
    while 1:
        i = int(input('Your guess: '))
        if i > n:
            print('Too Big')
        elif i < n:
            print('Too Small')
        else:
            print('Correct!')
            break
from random import randint
x = int(input('from number: '))
y = int(input('to number: '))
try_number = int(input('try number: '))
number = randint(x, y)
i = 1
while i <= try_number:
   guess = int(input('your attempt № {}: enter you choosing number: '.format(i)))
   if guess == number:
       print('you are the winner!')
       break
   else:
       if i == try_number:
           print('you are the loser!')
       else:
           if guess < number:
               print('your choose is less than the number: ')
           elif guess > number:
               print('your choose is more than the number: ')
   i += 1
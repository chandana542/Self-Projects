import random
print('Welcome to the Number Guessing Game!!')
print('Rules:')
print('1. The computer has chosen a number between 1 and 100.')
print('2. Your task is to guess the number.')
print('3. After each guess, the computer will tell you if your guess is too high or too low.')
print('4. You can quit anytime by entering 0.')
print('5. You start with 100 points.')
print('6. For every wrong guess, 10 points will be deducted.')
print('7. The fewer attempts you take, the higher your final score.')
print('8. You have a maximum of 10 attempts. Good Luck!')
a=0
max_a=10
s=100
num=random.randint(1,100)
while True:
    user_num=int(input('Guess the Number: '))
    if user_num==0:
        print('The Number was',num)
        print(f'And You Took {a} Attempts!')
        print('Your Final Score is',s)
        break
    a+=1
    if(a<=max_a):
        if num==user_num:
            print('You Won!')
            print(f'And You Took {a} Attempts!')
            print('Your Final Score is',s)
            break
        elif num>user_num:
            print('Too Low, Try Again!')
            s=s-10
        elif num<user_num:
            print('Too High, Try Again!')
            s=s-10
    else:
        print('Sorry! Your attempts are finished')
        print('The Number was',num)
        print(f'And You Took {a-1} Attempts!')
        break


import random

options = ['rock', 'paper', 'scissors']
computer = options[random.randint(0,2)]

user = False
computer_score = 0
user_score = 0
i=0

print('You have 5 chances to win with the computer and at the end the final result will be announced. Have fun!')
username = input('Enter your name \n')

while i <5:
    user = input('Rock, paper or scissors? \n')
    if computer == user:
        print('Tie!')
    elif user == 'Rock' or user =='rock':
        if computer == 'paper':
            print ('The point goes to computer')
            computer_score +=1
        else:
            print ('The point goes to you')
            user_score +=1
    elif user == 'Paper' or user == 'paper':
        if computer == 'scissors':
            print ('The point goes to computer')
            computer_score +=1
        else:
            print ('The point goes to you')
            user_score +=1
    elif user == 'Scissors' or user == 'scissors':
        if computer == 'rock':
            print ('The point goes to computer')
            computer_score +=1
        else:
            print ('The point goes to you')
            user_score +=1
    else:
        print ('Wrong input, try again')
        i=i-1
    computer = options[random.randint(0,2)]
    user == False
    i+=1
if i == 5:
    if user_score > computer_score:
        print ('The result is ' + str(user_score) + ' : ' + str(computer_score) + '\n' + username + ' You are the winner')
    elif user_score < computer_score:
        print ('The result is ' + str(user_score) + ' : ' + str(computer_score) + '\n' + username + ' You lose')
    else:
        print ('No winner this time')


import random
import time

answers = ['It is certain.',
           'As I see it, yes.',
           'Outlook good.',
           'Yes - definitely.',
           'Better not tell you now.',
           'Reply hazy, try again.',
           'Outlook not so good.',
           'My reply is no.',
           'i dont know',
           '42']
#array of strings.

def answerFunc():
    question = input("Enter your question: ")
    print('Shuffling the ball')
    time.sleep(2)
    print('Here is your answer:')
    print(random.choice(answers))
    #.choice method returns a random item from the answer array
#def is used for defining functions, so what does this function do?
    
answerFunc()
#able to call function when i need to.

time.sleep(2)
#making the code pause for (2) seconds.

print('\n')
#printing a new line

secondQ = input("Would you like to ask another question? Y/N: ")

while secondQ == "Y":
    answerFunc()
    #calling the function to the if statement.
    print ('\n')
    secondQ = input("Would you like to ask another question? Y/N: ")
    #repeat the process if they want to continue to ask questions.
else:
    print ('GoodBye!')
    exit()
 

num = 1
while (num < 300):
    print num
    num = num + 2
    
list1 = [0,1,5,84,684,3,19,11,20,'ball']
step = 0

while (step < len(list1)):
    print list1[step]
    step = step +1
    
import random
rand = random.randint(0,50)

print 'Guess a number between 0 & 50'
userInput = int(raw_input())

while (userInput != rand):
    print 'Guess a number between 0 & 50'
    userInput = int(raw_input())
    if userInput < rand:
        print 'Too Low'
    elif userInput > rand:
        print 'Too High'
    else:
        print "Correct"
    
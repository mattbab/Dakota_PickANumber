maxnum=100
repeat = True
while repeat:
    print ('guess a number beteen 1-'+str(maxnum))
    import random
    count=0
    guess= 0
    computer = random.randint(1,maxnum)

    print (count)
    while guess != computer:
        guessc = input()
        guess = int(guessc)
        if guess < computer :
            print ('too low.guess again.')
        if guess == computer :
            print ('good job. you win.')
        if guess > computer :
            print ('too high.try again.')
        count=count+1
    print ('you solved it in ' + str(count) +' turns.')
    print ('do you want to play again?')
    print('yes or no')
    repeat2=input()
    if repeat2.lower() =='no' or repeat2.lower() =='n':
       repeat = False

    

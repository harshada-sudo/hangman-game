import random

def hangman():
    #create a list of words
    words=['hello','good','beautiful','sweet','home','mother','teacher']
    random.shuffle(words)
    answer=list(words[0])

    #create list where user is going to fill characters
    user=[]
    for i in range(len(answer)):
        user.insert(i,'_'+" ")

    #create an empty list for display
    display=[]
    print("Word is :")
    for d in range(len(answer)):
        display.insert(d,"_"+" ")
    print(display)

    length=0    #if length is not equals to length of word then try 
    a= 10         #total number of attempts  
    while True:
        user_input=input("Enter a character :")
        print(user_input)  
        flag=0                                      #not found
        for i in range(len(answer)):                #loop through for single character
            if user_input == answer[i]:
                print("found at position"+" "+str(i))
                flag=1                              # element found
                user[i]=user_input
                print(user)
                length = length + 1                 #filled positions
                
        if(flag==0):                                               # if character is not found
            if(a!=1):                                              #till remaining attempt is not 1 print remainign attempts and try
                a=a-1                                              #deduct one attepmt
                print("Remaining number of attempts are :"+str(a))
            else:                                                  #if attempt is 1 and its wrong then break
                print("Try Again !!")
                break
        
        if(length == len(answer)):      # if all positions are filled then word found so break
            print("You did it !!")
            break

def Caller():
    while True:
        choice=input("Would you like to play Hangman ??(1.yes / 2.no) :")    
        if choice == '1':
            hangman()
        elif choice == '2':
            print("Good Bye !!")
            return(exit)    
        else:
            print("Invalid Option")
Caller()    
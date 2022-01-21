#
#  Python:  3.10.1
#
#  Author:  Travis Lord
#
#  Purpose: The Tech Academy - Python Course, Creating our first program.
#               Demonstrating how to pass variables from function to function
#               while producing a functional game.
#
#               Remember, function_name(variable) _means that we pass in the variable.
#               return variable _means that we are returning the variable to
#               back to the calling function.


def start(nice=0,mean=0,name=""):           # when user doesn't supply value we want these variables at 0 or empty("") to control the variables 
    # get user's name
    name = describe_game(name)          #pass in name from iuser nput
    nice,mean,name = nice_mean(nice,mean,name)      # passing info into and out of functions from game 


def describe_game(name):
    """
        Check if this is a new game or not.
        If it is a new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print('\nThank you for playing again, {}!'.format(name))   # this one can't format the name unless the user fills out their, so the game doesn't ask the user more than once
    else:
        stop = True         # while stop is true do whats underneath this 
        while stop:
            if name == "":
                name = input('\nWhat is your name?  \>>> ').capitalize()  # capitalize user input raw string
                if name != "":     # if name not empty do this>
                    print("\nWelcome, {}!".format(name))
                    print('\nIn this game you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                    print('but at the end of the game your fate \nwill be sealed by your actions.')
                    stop = False   # this shuts off the while loop, acts as a switch for logic
    return name    # user name aquired and saved after returned to name var


def nice_mean(nice,mean,name):  
    stop = True
    while stop:
        show_score(nice,mean,name) 
        pick = input('\nA stranger approcaches you for a \nconversation.  Will you be nice \nor mean?>>>: type n or m >>>: ').lower()  # converts to lowercase string
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1)
            stop = False            # stop asking user if condition is met
        if pick == 'm':
            print('\nThe stranger glares at you \nmeancilngly and storms off...')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)  #pass the 3 variables to the score()

def show_score(nice,mean,name):
    print('\n {}, your current total: \n ({}, Nice) and ({}, Mean)'.format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2:    # if condition is valid, call lose function passing in the variables so it can use them
        win(nice,mean,name)
    if mean >2:    # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:             # else, call nice_mean function passing in the variables so it can use them- because game is not over (no one over 3 points nice or mean
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you and you've \nmade lots of friends along the way!".format(name))
    import playsound
    playsound.playsound('win.mp3')
    #call again function and pass in our variables  Above is the proper syntax for adding a sound effect to the program
    again(nice,mean,name)

def lose(nice,mean,name):
    # Subsitute the {} wildcards with our variable values
    print('\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!'.format(name))
    # call again function and pass in our variables
    again(nice,mean,name)
    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('nDo you want to play again?  (y/n):\n>>> ').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\nOh, so sad, sorry to see you go but its your fault so bye!')
            stop = False
            quit()
        else:
            print('\nEnter (Y) for "YES, (N) for "NO":\n>>> ')

def reset(nice,mean,name):
    nice =0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)
    







if __name__ =="__main__":
    start()

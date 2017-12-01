in time import sleep

#Functions set at start of code
def helpme1():
    for a in 'Recognised commands are: explore, help, suicide, flee, look, get,open door, run and attack. With the objects you wish to affect next to them..have fun! :)':
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.02)
    game()
def helpme2():
    for a in 'Recognised commands are: explore, help, suicide, flee, look, get, open door, run and attack. With the objects you wish to affect next to them..have fun! :)':
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.02)
    game2()

def youlose():
    print "_Game over_"
    quit()
def game():
    for a in 'You find yourself in a dimly lighted room with no obvious exits, if only you had a torch...however it does have a strange box there. And one door next to the box':
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.02)
    print
    option1=(raw_input('>'))
    if option1=="help":
        helpme1()
    if option1=="look box":
        game2() #This calls the next situation :-)

def game2():
    for a in 'The box is open and you find a remote looking button there. Your going to have to guess the command on how to use it, as it is not in the help file.':
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.02)
    print
    option2=(raw_input('>'))

    if option2=="get button":
        game3()
    if option2=="get remote like button":
        game3()
    if option2=="help":
        helpme2()
    else:
        print "Er... try reading it again. Or use help to find out what is going on."
        game2()

def game3():
      for a in 'You have the button now, but how to use it is another question.':
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.02)
      print
      option3=(raw_input('>'))
      if option3=="press button":
          game4()
      if option3=="attack button":
          for a in 'You attack the button you have aquired like a stupid fool. And now there is no escape':
            sys.stdout.write(a)
            sys.stdout.flush()
            sleep(0.02)
      print
      youlose()







#Functions end, note: Functions may continue in other parts of the game
for a in 'Welcome to space dungeon!': #MENU BEGIN!
   sys.stdout.write(a)
   sys.stdout.flush()
   sleep(0.03)
for a in '  Copyright Navid Momtahen':
   sys.stdout.write(a)
   sys.stdout.flush()
   sleep(0.03)
def menu():
 print 
 print "[1] Play"
 print "[2] Help"
 print "[e] Exit"
 prompt1=(raw_input(''))  #Menu options here
 if prompt1=="1":
     game()
 if prompt1=="2":
     print "You chose help"
 if prompt1=="e":
     print "You wanted to exit! :-O"
 else:
     print "Not defined command."
     menu()

menu() #Main loop for menu


#Copyright code Navid Momtahen

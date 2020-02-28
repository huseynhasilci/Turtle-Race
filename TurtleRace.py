from swampy.TurtleWorld import *
import random

world = TurtleWorld()
name1 = Turtle()
name2 = Turtle()
def questions():
    # Turtle one requirements
    print "*****************First Turtle******************"

    while True:
        input1Name = raw_input("Please enter your first turtle name:")         # to ask the f'rst turtle name
        if input1Name != " ":
            name1.__setattr__("name", input1Name)
            name1.delay = 0.01
            print "Your turtle name is:",input1Name
            break
        elif input1Name == " " or input1Name == "":                         # turtle name cannot be blank
            print "Empty is not a name please enter a real name."
            continue
    while True:
        first_racer_color = raw_input("Please choose your first Turtle color: red-blue-yellow:")     # to make decision first turtle color
        if first_racer_color == "red" or first_racer_color == "blue" or first_racer_color == "yellow":
            name1.set_color(first_racer_color)
            break
        elif first_racer_color != "red" or first_racer_color != "blue" or first_racer_color != "yellow:":
            print "This color is not valid please choose another color."
            continue
                                                            # if firts turtle's color connot be different colors except blue,red,yellow
    print "{} named turtle is ready to go!".format(input1Name)

#second turtle requirements


    print "***************Second Turtle****************"
    while True:
        input2Name = raw_input("Please enter your second Turtle name:")             # second turtle questions
        if input2Name == " "or input2Name =="":
            print "You cannot enter a empty name please enter a real name."
            continue

        if input1Name != input2Name:
            print "Your second turtle name is",input2Name

            name2.__setattr__("name", input2Name) #http://www.greenteapress.com/thinkpython/swampy/TurtleWorld.html
            break
        elif input1Name == input2Name:
            print "This name is already taken. Please enter another name."
            continue

    # second turtle colors
    name2.delay = 0.01
    while True:
        second_turtle_color = raw_input("Please choose your second Turtle color: red-blue-yellow:")
        if second_turtle_color == "red" or second_turtle_color == "blue" or second_turtle_color == "yellow":
            name2.set_color(second_turtle_color)
            break
        elif second_turtle_color !="red" or second_turtle_color != "blue" or second_turtle_color != "yellow":
            print "This color is also not valid please select another color."
            continue

    print "{} named turtle is also ready to go.".format(input2Name)
     # to make sure the racers position
    pu(name1)
    bk(name1,150)
    rt(name1,90)
    fd(name1,150)
    lt(name1,90)
    pd(name1)

    pu(name2)
    bk(name2,150)
    pd(name2)
    print "Let's the race begin!!!"

questions()

def random1(a,name2):
    b = random.randint(1,3)
    if b == 1:
                                                   # moving shapes for first turtle
        for i in range(1):
            fd(name1, a/5)
            lt(name1, 90)
            fd(name1, a/5)
            rt(name1, 90)
            fd(name1, a/5)
            lt(name1, 90)
            fd(name1, a/5)
            rt(name1, 90)
            fd(name1, a/5)
            rt(name1, 90)
            fd(name1, a/5)
            lt(name1, 90)
            fd(name1, a/5)
            rt(name1, 90)
            fd(name1, a/5)
            lt(name1, 90)
            fd(name1, a/5)
    elif b == 2:
        lt(name1, 90)
        for i in range(180):
            fd(name1, 0.5)
            rt(name1, 1)
        lt(name1,90)
    else:
        fd(name1,a)

def random2(a,name2):
    b = random.randint(1,3)
    if b == 1:
                                       # moving shapes for second turtle
        for i in range(1):
            fd(name2, a/5)
            lt(name2, 90)
            fd(name2, a/5)
            rt(name2, 90)
            fd(name2, a/5)
            lt(name2, 90)
            fd(name2, a/5)
            rt(name2, 90)
            fd(name2, a/5)
            rt(name2, 90)
            fd(name2, a/5)
            lt(name2, 90)
            fd(name2, a/5)
            rt(name2, 90)
            fd(name2, a/5)
            lt(name2, 90)
            fd(name2, a/5)
    elif b == 2:
        lt(name2, 90)
        for i in range(180):
            fd(name2, 0.5)
            rt(name2, 1)
        lt(name2,90)
    else:
        fd(name2,a)


# score1 = 0
# score2 = 0


first_racer = name1.__getattribute__("name")
second_racer = name2.__getattribute__("name")
def race(name1,name2):
    score1 = 0
    score2 = 0
    which_racer = 0
    round1 = 1
    while True:
                                                        # race starting point
        print "******Raund ",round1 ,"**********"
        print first_racer,"Score:",score1
        print second_racer,"Score:",score2

        mod2 = which_racer % 2                             # I made this for the changing turtles between rounds
                                                           # which_racer will increase +1
        if mod2 == 0:
            print first_racer, " plays."
            player_enterence = raw_input("Please enter a number between 0 to 100:")
            player_number = 100 - int(player_enterence)
            random_number = random.randint(0, 100)

            if player_number > random_number:
                print "success:)"
                random1(int(player_enterence),name1)              # if the player enter true number I call the moving part
                score1 = score1 + int(player_enterence)
            else:
                print "You failed your turtle will not move until 2 round"
                print second_racer, "Will move"
        if mod2 == 1:
            print second_racer, " plays."
            player_enterence = raw_input("Please enter a number between 0 to 100:")
            player_number = 100 - int(player_enterence)
            random_number = random.randint(0, 100)

            if player_number > random_number:
                print "success:)"
                random2(int(player_enterence),name2)          # if the player enter true number I call the moving part
                score2 = score2 + int(player_enterence)
            else:
                print "You failed your turtle will not move until 2 round"
                print first_racer, "Will move"


        round1 += 1

        which_racer += 1


        if score1 >= 200:
            print first_racer, "is the winner."        # to decide who is the winner
            break

        if score2 >= 200:
            print second_racer, "is the winner."
            break
    # while True:
    #     one_more_game = raw_input("Do you want to play one more game? Yes / No")
    #     if one_more_game == "Yes" or one_more_game == "yes":
    #         world.quit()
    #         world = TurtleWorld()
    #         name1 = Turtle()
    #         name2 = Turtle()
    #         questions()
    #         race(name1,name2)
    #     elif one_more_game == "No" or one_more_game == "no":
    #         print ("Thank's for playing.")
    #         exit()
race(name1,name2)
while True:
    one_more_game = raw_input("Do you want to play one more game? Yes / No")
    if one_more_game == "Yes" or one_more_game == "yes":
        world.quit()                                      # to reset the game
        world = TurtleWorld()
        name1 = Turtle()
        name2 = Turtle()
        questions()
        race(name1,name2)
    elif one_more_game == "No" or one_more_game == "no":
        print ("Thank's for playing.")
        exit()
# race()
wait_for_user()
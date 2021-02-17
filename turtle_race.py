import turtle
import random

print(
'''
Welcome to turtle race!!!
Here you will be competing with many turtles with will be played by computer...
Enjoy the game.
'''
)

start_point = -500

turtle.title("Welcome to turtle race")
main_player = turtle.Turtle()
main_player.getscreen()
main_player.shape("turtle")
computer_player_1 = main_player.clone()
computer_player_2 = main_player.clone()
computer_player_3 = main_player.clone()
computer_player_4 = main_player.clone()
main_player.shapesize(3)
computer_player_1.shapesize(3)
computer_player_2.shapesize(3)
computer_player_3.shapesize(3)
computer_player_4.shapesize(3)
main_player.color("red")
computer_player_1.color("blue")
computer_player_2.color("green")
computer_player_3.color("black")
computer_player_4.color("pink")

# Setting up Player one...

computer_player_1.pen(pencolor="blue")
computer_player_1.penup()
computer_player_1.goto(300,250)
computer_player_1.pendown()
computer_player_1.circle(50)
computer_player_1.penup()
computer_player_1.goto(start_point,300)
computer_player_1.pendown()

#setting up player 2

computer_player_2.pen(pencolor="green")
computer_player_2.penup()
computer_player_2.goto(300,100)
computer_player_2.pendown()
computer_player_2.circle(50)
computer_player_2.penup()
computer_player_2.goto(start_point,150)

#Setting up main player

main_player.pen(pencolor="red")
main_player.penup()
main_player.goto(300,-50)
main_player.pendown()
main_player.circle(50)
main_player.penup()
main_player.goto(start_point,0)

#Setting up player 3

computer_player_3.pen(pencolor="black")
computer_player_3.penup()
computer_player_3.goto(300,-200)
computer_player_3.pendown()
computer_player_3.circle(50)
computer_player_3.penup()
computer_player_3.goto(start_point,-150)

#Setting up player 4

computer_player_4.pen(pencolor="pink")
computer_player_4.penup()
computer_player_4.goto(300,-350)
computer_player_4.pendown()
computer_player_4.circle(50)
computer_player_4.penup()
computer_player_4.goto(start_point,-300)

die = [1,2,3,4,5,6]

player_move = [1,2,3,4,5]

while True:
    if len(player_move) == 0:
        break
    if computer_player_1.pos() >= (300, 300):
        print("Blue Wins!!!")
        computer_player_1.penup()
        computer_player_1.goto(299,300)
        computer_player_1.pendown()
        player_move.remove(1)
    elif computer_player_2.pos() >= (300, 150):
        print("Green Wins!!!")
        computer_player_2.penup()
        computer_player_2.goto(299,150)
        computer_player_2.pendown()
        player_move.remove(2)
    elif main_player.pos() >= (300, 0):
        print("Red Wins!!!")
        main_player.penup()
        main_player.goto(299,0)
        main_player.pendown()
        player_move.remove(3)
    elif computer_player_3.pos() >= (300, -150):
        print("Black Wins!!!")
        computer_player_3.penup()
        computer_player_3.goto(299,-150)
        computer_player_3.pendown()
        player_move.remove(4)
    elif computer_player_4.pos() >= (300, -300):
        print("Pink Wins!!!")
        computer_player_4.penup()
        computer_player_4.goto(299,-300)
        computer_player_4.pendown()
        player_move.remove(5)
    else:
        for i in range(5):
            random_player = random.choice(player_move)
            if random_player == 1:
                computer_player_1.penup()
                computer_player_1.speed(1)
                computer_player_1.fd(20*random.choice(die))
                computer_player_1.pendown()
            elif random_player == 2:
                computer_player_2.penup()
                computer_player_2.speed(1)
                computer_player_2.fd(20*random.choice(die))
                computer_player_2.pendown()
            elif random_player == 3:
                main_player.penup()
                main_player.speed(1)
                main_player.fd(20*random.choice(die))
                main_player.pendown()
            elif random_player == 4:
                computer_player_3.penup()
                computer_player_3.speed(1)
                computer_player_3.fd(20*random.choice(die))
                computer_player_3.pendown()
            elif random_player == 5:
                computer_player_4.penup()
                computer_player_4.speed(1)
                computer_player_4.fd(20*random.choice(die))
                computer_player_4.pendown()


print("Game Completed")

import turtle

# Fenster erstellen

Fenster = turtle.Screen()
Fenster.title("ping pong mit Ghaith")
Fenster.tracer(0) # wegen latency
Fenster.setup(width=800, height=600)
Fenster.bgcolor("lightblue")

#objekte
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
#grösse
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.goto(x=0,y=0) # Ball Anfang postion
ball.penup()
ball_dx , ball_dy = 1, 1
ball_speed = .6
#mitllereline
mittelline=turtle.Turtle()
mittelline.speed(0)
mittelline.color("black")
mittelline.shape("square")
mittelline.goto(x=0,y=0)
mittelline.penup()

#spieler 1
spieler1 = turtle.Turtle()
spieler1.speed(0)
spieler1.shape("square")
spieler1.color("red")
spieler1.penup()
spieler1.shapesize(stretch_wid=5,stretch_len=1)
spieler1.goto(x=-350,y=0)

#spieler 2
spieler2 = turtle.Turtle()
spieler2.speed(0)
spieler2.shape("square")
spieler2.color("blue")
spieler2.penup()
spieler2.shapesize(stretch_wid=5,stretch_len=1)
spieler2.goto(x=350,y=0)

#ergebnis
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(x=0,y=260)
scoreboard.hideturtle()
scoreboard.write("spieler1 : 0 spieler2 : 0 ", align="center", font=("Courier", 20, "bold"))
s1_score , s2_score = 0, 0
# Bewegungen
def S1_move_up():
    spieler1.sety(spieler1.ycor()+20)
def S1_move_down():
    spieler1.sety(spieler1.ycor()-20)


def S2_move_up():
    spieler2.sety(spieler2.ycor() + 20)


def S2_move_down():
    spieler2.sety(spieler2.ycor() - 20)

# Tasten rufen
Fenster.listen()
Fenster.onkeypress(S1_move_up,"w")
Fenster.onkeypress(S1_move_down,"s")
Fenster.onkeypress(S2_move_up,"Up")
Fenster.onkeypress(S2_move_down,"Down")



#breite
mittelline.shapesize(stretch_wid=30,stretch_len=0.1)


# loop (damit der Fenster nicht sofort schliesst)
while True:
    Fenster.update()

    #ball bewegungen
    ball.setx(ball.xcor() + ball_dx * ball_speed)
    ball.sety(ball.ycor() + ball_dy * ball_speed)
    # ecken und kanten
    if(ball.ycor() > 290):
        ball.sety(290)
        ball_dy *= -1
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball_dy *= -1

    #kolideren mit spiler 1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (spieler1.ycor() - 60) and ball.ycor() < (
            spieler1.ycor() + 60):
        ball.setx(-340)
        ball_dx *= -1

     # kollidieren mit spieler 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (spieler2.ycor() - 60) and ball.ycor() < (
            spieler2.ycor() + 60):
        ball.setx(340)
        ball_dx *= -1

    #resultat
    if(ball.xcor()> 390):
        ball.goto(0,0)
        ball_dx *= -1
        scoreboard.clear()
        s1_score += 1

        scoreboard.write(f"Spieler1: {s1_score} Spieler2: {s2_score}", align="center",
                    font=("Courier", 20, "bold"))

    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1
        scoreboard.clear()
        s2_score += 1
        scoreboard.write(f"Spieler1: {s1_score} Spieler2: {s2_score}", align="center",
                         font=("Courier", 20, "bold"))




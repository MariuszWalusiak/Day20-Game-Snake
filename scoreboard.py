from turtle import  Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score:{self.score} ", align="center", font=FONT)

    def change_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score} ", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align=ALIGMENT, font=FONT )


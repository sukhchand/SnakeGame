from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.teleport(0, 280)
        self.write(arg=f"Score: {self.score}", align="center", move=False)
        print(self.highscore)

    def get_high_score(self):
        with open("high_score.txt", "r") as file:
            return int(file.read()) | 0

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align="center", move=False)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align="center", move=False)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
# “Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of
# each color that are in the hat. Give the object the ability to pick a random number of balls from the hat, 
# which will then be used to compute the probability of picking a certain distribution of balls over a large
# number of experiments”
import random

def prob(n, t):
    p = n/t
    return p

def pull(n, p):
    x = n*p
    return x

class lotteryball:

    def __init__(self, pink, blue, green):
        self.pink = pink
        self.blue = blue
        self.green = green

    def roll(self, num):
        total = self.pink + self.blue + self.green
        p_pink = prob(self.pink, total)
        p_blue = prob(self.blue,total)
        p_green = prob(self.green,total)
        n_pink = round(pull(num, p_pink,))
        n_blue = round(pull(num, p_blue,))
        n_green = round(pull(num, p_green,))

        statement = (f"If you pull {num} balls at random, you will likely get {n_pink} pink ball(s), {n_blue} blue ball(s), and {n_green} green ball(s).")
        return statement

pink = int(input("How many pink balls are inserted: "))
blue = int(input("How many blue balls are inserted: "))
green = int(input("How many green balls are inserted: "))

ball = lotteryball(pink, blue, green)

select = int(input("How many balls do you want to pick (type 0 for a random amount): "))

if select == 0:
    total = ball.pink+ball.blue+ball.green
    select = random.randint(1, total)
    print(ball.roll(select))
else:
    print(ball.roll(select))
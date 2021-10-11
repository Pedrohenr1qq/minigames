import random as t

bot = t.randint(0,1000)

t = 10

print(f"Let's play a game. You have {t} attempts")

a = 0

while True:
    y = int(input("Type a number: "))
    a+=1

    if a == t:
        print(f"You lose. The number was {bot}")
        break
    if y == bot:
        print("You win")
        break

    print("big" if y > bot else "small")

print(f"attempts: {a}")

from random import randint

def throwAndWin(thrower, catcher):
    random = randint(0, 3)
    if random != 0:
        print(f"{thrower} throws. {catcher} catches the ball.")
        throwAndWin(catcher, thrower)
    else:
        y = randint(10, 20)
        print(
            f"{thrower} throws. {catcher} drops the ball. {y} points awarded to {thrower}"
        )
        score[thrower] += y


no_sets = int(input("Enter the number of sets in the game : "))
player1 = input("Enter player one's name : ")
player2 = input("Enter player two's name : ")

score = {player1: 0, player2: 0}

for i in range(no_sets):
    print("Start of set : ", i + 1)
    throwAndWin(player1, player2)
print(
    f"The total points for {player1} are {score[player1]}"
)
print(
    f"The total points for {player2} are {score[player2]}"
)
if score[player1] == score[player2]:
    print("Its a Tie")
else:
    winner = player1 if score[player1] > score[player2] else player2
    print(f"Congratulations! {winner} you are the winner of this game" )
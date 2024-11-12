#grade calculator
def main():
    score = int(input("Score: "))
    maxscore = int(input("Amount of Points Possible: "))

    finalscore = (score) / (maxscore) * 100
    print(f"You're final score is {finalscore:.2f}%.")
main()

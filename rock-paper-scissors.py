import random

liste = ["rock","paper","scissors"]
pcHamle = random.choice(liste)

print("welcome the rock-paper-scissors game.")

running = True

while running:
    hamle1 = str(input("enter your first move."))

    if hamle1 == "rock":
        if pcHamle == "rock":
            print("draw.\n",
                  pcHamle)
        elif pcHamle == "paper":
            print("defeat.\n",
                  pcHamle)
        elif pcHamle == "scissors":
            print("congrulations you win.\n",
                  pcHamle)

    if hamle1 == "paper":
        if pcHamle == "paper":
            print("draw.\n",
                  pcHamle)
        elif pcHamle == "rock":
            print("congrulations you win.\n",
                  pcHamle)
        elif pcHamle == "scissors":
            print("defeat.\n",
                  pcHamle)

    if hamle1 == "scissors":
        if pcHamle == "scissors":
            print("draw.\n",
                  pcHamle)
        elif pcHamle == "paper":
            print("congrulations you win.\n",
                  pcHamle)
        elif pcHamle == "rock":
            print("defeat.\n",
                  pcHamle)

    quit = str(input("would you leave game?"))

    if quit == "yes":
        running = False
        print("okay, you are leaving game now.")
    if quit == "no":
        print("Continue.")


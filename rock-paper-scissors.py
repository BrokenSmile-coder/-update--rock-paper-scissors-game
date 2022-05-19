import random

liste = ["rock","paper","scissors"]

print("welcome the rock-paper-scissors game.")

running = True

while running:
    hamle1 = str(input("enter your first move."))
    pcHamle = random.choice(liste)

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
        else:
            print("yanlış işlem.")

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
        else:
            print("yanlış işlem.")

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
        else:
            print("yanlış işlem.")

    quit = str(input("would you leave game?"))

    if quit == "yes":
        running = False
        print("okay, you are leaving game now.")
        break
    if quit == "no":
        print("Continue.")

    continue

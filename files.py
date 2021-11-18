teams = ["Chelsea", "Cherries","Manchester","Newcastle","Clansmen"]

with open("teams.txt", "w") as file:
    for i in teams:
        newline = str(i)
        file.write(newline + "\n")

with open("teams.txt", "r") as file:
    print(file.readline())
    file.readline()
    file.readline()
    print(file.readline())
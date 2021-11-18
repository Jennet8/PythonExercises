#Create a Python file which does the following:

#     Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
#     Reads and displays the names of the 1st and 4th team in the file.


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
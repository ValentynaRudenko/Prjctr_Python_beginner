# #3. Write a program that will simulate user score in a game. C
# reate a list with 5 player's names. 
# After that simulate 100 games for each player. 
# As a result of the game create a list with player's name and his score 
#     (0-1000 range). And save it to a CSV file. File should looks like this:

#     ```
#     Player name, Score
#     Josh, 56
#     Luke, 784
#     Kate, 90
#     Mark, 125
#     Mary, 877
#     Josh, 345
#     ...
#     ```

import random

import csv

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

with open("scores.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Score"])

    for game in range(1, 101):

        for player in players:
            score = random.randint(0, 1000)
            writer.writerow([player, score])


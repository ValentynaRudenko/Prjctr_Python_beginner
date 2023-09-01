 # 4. Write a script that reads the data from previous CSV file 
# and creates a new file called high_scores.csv 
# where each row contains the player name and their highest score. 
# Final score should sorted by descending of highest score

# The output CSV file should look like this:

    
#     Player name, Highest score
#     Kate, 907
#     Mary, 897
#     Luke, 784
#     Mark, 725
#     Josh, 345


import csv
fields = []
player_all_scores = dict()
player_high_score = []

with open("scores.csv", "r") as file:
    players_scores = csv.reader(file)
    fields = next(players_scores)
    for player, score in players_scores:
        if player in player_all_scores:
            if player_all_scores.get(player) < score:
                player_all_scores.update({player: score})
        else:
            player_all_scores.update({player: score})
    
player_all_scores_sorted = sorted(player_all_scores.items(), key=lambda x: x[1], reverse=True)
print(player_all_scores_sorted) 
        
with open("high_scores.csv", "w") as file2:
    writer = csv.writer(file2)
    writer.writerow(("Player name", "Highest score"))
    writer.writerows(player_all_scores_sorted)

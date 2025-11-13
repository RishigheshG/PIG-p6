import random

def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)
  return roll

while True:
  players = input("Enter the number of players (1-4): ")
  if players.isdigit():
    players = int(players)
    if 1 <= players <= 4:
      break
    else:
      print("Must be between 1 and 4 players.")
  else:
    print("Invalid input. Please enter a number between 1 and 4.")

max_score = 50
player_scores = [0 for _ in range(players)] #This creates a list with a score of 0 for each player

while max(player_scores) < max_score:
  for player_idx in range(players):    
    print("\nPlayer", player_idx + 1, "'s turn:")
    print("Your total score is:", player_scores[player_idx], "\n")
    current_score = 0

    while True:
      should_roll = input('Would you like to roll? (y/n): ').lower()
      if should_roll != 'y':
        break
      
      value = roll()
      if value == 1:
        current_score = 0
        print("You rolled a 1! No points this turn.")
        break
      else:
        current_score += value
        print("You rolled a", value)

      print("Your current turn score is:", current_score)
    player_scores[player_idx] += current_score
    print("Player", player_idx + 1, "total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_player = player_scores.index(max_score) + 1
print("\nPlayer", winning_player, "wins with a score of", max_score, "!")
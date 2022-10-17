import random

def chooseCard(player_name, player_score):
    # Choose a random item from our two lists to crea a 'card'
    chosen_suit = random.choice(suits)
    chosen_val = random.choice(values)
    print(f"{player_name} has been dealth the {chosen_val} of {chosen_suit}")
    if chosen_val in ['2','3','4','5','6','7','8','9','10']:
        player_score += int(chosen_val)
    elif chosen_val in ['Jack','Queen','King','Ace']:
        player_score += 10
    else: # In this case, the card was an Ace
        # In this case the card is an ace
        # We add 11 unless it would bust player then we add 1
        if (player_score + 11) > 21:
            player_sckore += 1
        else:
            player_score += 11
    return player_score

# Create a 'deck' of cards
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

print("--------Welcome to 21/BlackJack!--------"
      "\nThe aim of the game is to get as close to 21 as possible without going over."
      "\nEach time you draw a card it will be added to your total,"
      "\nand you will have the option to draw another card or 'stick' with your hand.")

keep_playing = True
while keep_playing == True:
  # Create game variables
    player1_name = ''
    player2_name = ''
    player1_score = 0
    player2_score = 0
    player1_stick = False
    player2_stick = False

    input_correct = False
    while input_correct == False:
        game_mode = input("\n1. Player vs Player\n2. Player vs Computer\nSelect a game mode (Enter 1 or 2):\t")
        # For 2 players, collect both names, otherwise just collect one
        # input_correct used to make sure player inputs correct value
        if game_mode.lower() in ['1','1.','player vs player','pvp']:
            game_mode = 1
            input_correct = True
            player1_name = input("Please enter the name of player 1:\t")
            player2_name = input("Please enter the name of player 2:\t")
            print(f"\nHello {player1_name} and {player2_name}, let's begin!")
        # if x in list allows multiple checks in one if statement
        # string.lower converts string to all lower case
        elif game_mode.lower() in ['2','2.','player vs computer','pvc']:
          game_mode = 2
          input_correct = True
          player1_name = input("Please enter the name of player 1:\t")
          player2_name = 'The computer'
          print(f"\nHello {player1_name}, let's begin!")
        else:
          print("Invalid input, please try again!")

        game_over = False
        while game_over == False:
          # Both players are sticking, see who won
          if player1_stick == True and player2_stick == True:
            if player1_score > player2_score:
              print(f"\n{player1_name} wins! Congratulations!")

            if player2_score > player1_score:
              print(f"\n{player2_name} wins! Congratulations!")

            else:
              print("It's a tie! Play again!")
            game_over = True

          # Get player 1 to play if they're not sticking
          if game_over == False and player1_stick == False:
            print(f"\nDrawing {player1_name}'s card...")
            player1_score = chooseCard(player1_name, player1_score)
            print(f"{player1_name}'s score is now {player1_score}...")

            if player1_score > 21:
                print(f"{player1_name} has gone bust! They lose!")
                game_over = True
            
            else:
                input_correct = False
                while input_correct == False:
                  player_stick_input = input("Would you like to stick or hit (stick/hit):\t")
                  if player_stick_input.lower() in ['s','stick','1']:
                      player1_stick = True
                      input_correct = True
                  elif player_stick.intput.lower() in ['h','hit','2']:
                    input_correct = True
                  else:
                    print("Incorrect input, try again!")

        # Get player 2 to play if they're not sticking
        if game_over == False and player2_stick == False:
            print(f"\nDrawing {player2_name}'s card...")
            player2_score = chooseCard(player2_name, player2_score)

            if player2_score > 21:
                print(f"{player2_name} has gone bust! They lose!")
                game_over = True
            
            else:
                input_correct = False
                while input_incorrect == False:
                  player_stick_input = input("Would you like to stick or hit (stick/hit):\t")
                  if player_stick_input.lower() in ['s','stick','1']:
                      player2_stick = True
                      input_correct = True
                  elif player_stick.intput.lower() in ['h','hit','2']:
                    input_correct = True
                  else:
                    print("Incorrect input, try again!")
                    
input_correct = False
while input_correct == False:
    play_again = input("Would you like to play again(Y/N):\t")
    if play_again.lower() == 'n':
      input_correct = True
      keep_playing = False
    elif play_again.lower() == 'y':
      input_correct = True
    else:
      print("Incorrect input, please try again!")



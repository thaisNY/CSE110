"""
RPG Story: The Quest for the Lost Sword

VERSION FOR TWO PLAYERS
"""


"""
Level 1: The Journey Begins
Narrative: You are an adventurer tasked with retrieving a lost magical sword from the Cave of Shadows.
As you enter the forest that leads to the cave, you encounter a fork in the road.

Level 2: The Encounter
Narrative: After some time on your journey, you hear strange noises. Suddenly, 
a wild goblin jumps out in front of you, blocking your way!

Level 3: The Final Challenge
Narrative: After dealing with the goblin, you finally reach the Cave of Shadows. As you step inside,
you see the magical sword resting on an altar. But before you can take it, a mighty dragon appears, guarding the sword!
"""
# RPG Game: The Quest for the Lost Sword - Two Players Version

play_again = "YES"

while play_again == "YES":

    for player in range(1, 3):  # Loop for two players
        print(f"\nPlayer {player}'s turn!")

        # Level 1: The Journey Begins
        valid_choice = False
        while not valid_choice:
            choice = input(f"Player {player}, you encounter a fork in the road. Do you take the LEFT path, the RIGHT path, or TURN BACK? ").upper()
            if "LEFT" in choice:
                valid_choice = True
                print(f"Player {player} heads towards the village. The villagers warn you of the dangers ahead but offer you supplies.")
            elif "RIGHT" in choice:
                valid_choice = True
                print(f"Player {player} enters the dark forest. Shadows move around you as you hear mysterious whispers.")
            elif "TURN BACK" in choice:
                valid_choice = True
                print(f"Player {player} reconsiders the quest and returns home. The adventure ends before it even begins!")
                break
            else:
                print("Invalid choice. Please choose 'LEFT', 'RIGHT', or 'TURN BACK'.")

        if "TURN BACK" in choice:
            break  # Exit the loop if the player chose to turn back

        # Level 2: The Encounter
        valid_choice = False
        while not valid_choice:
            choice = input(f"Player {player}, a goblin jumps out in front of you! Do you FIGHT, RUN, or TALK? ").upper()
            if "FIGHT" in choice:
                valid_choice = True
                print(f"Player {player} draws a sword and engages in battle with the goblin!")
            elif "RUN" in choice:
                valid_choice = True
                print(f"Player {player} tries to run, but the goblin is faster! It catches up.")
            elif "TALK" in choice:
                valid_choice = True
                print(f"Player {player} tries to reason with the goblin, but it snarls and isn't interested in talking.")
            else:
                print("Invalid choice. Please choose 'FIGHT', 'RUN', or 'TALK'.")

        # Level 3: The Final Challenge
        valid_choice = False
        while not valid_choice:
            choice = input(f"Player {player}, you face a mighty dragon guarding the sword. Do you CHALLENGE it, SNEAK past it, or OFFER treasure? ").upper()
            if "CHALLENGE" in choice:
                valid_choice = True
                print(f"Player {player} draws a weapon and prepares for an epic battle with the dragon!")
            elif "SNEAK" in choice:
                valid_choice = True
                print(f"Player {player} tries to sneak past the dragon, but its keen senses detect them!")
            elif "OFFER" in choice:
                valid_choice = True
                print(f"Player {player} offers the dragon some treasure, and it considers the offer.")
            else:
                print("Invalid choice. Please choose 'CHALLENGE', 'SNEAK', or 'OFFER'.")

    # Asking if the players want to play again with validation for the input
    valid_response = False
    while not valid_response:
        play_again = input("Do you both want to play again? (YES/NO): ").upper()
        if play_again == "YES":
            valid_response = True
        elif play_again == "NO":
            valid_response = True
        else:
            print("Invalid answer. Please type 'YES' or 'NO'.")

print("Thanks for playing! Hope both players enjoyed the adventure!")

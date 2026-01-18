import random

options = ("rock", "paper", "scissors")
playing = True

while  playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Ti's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # play_again = input("Play again? (y/n): ").lower()
    # if not play_again == "y":
    #     playing = False

    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing")

# other code

# import random
#
# def play():
#     user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor: \n")
#     computer = random.choice(['r', 'p', 's'])
#
#     if user == computer:
#         return 'it\'s a Tie'
#     # r > s , s > p , p > r
#
#     if is_win(user, computer):
#         return 'You won!'
#
#     return 'You lost!'
#
# def is_win(player, opponent):
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
#             or (player == 'p' and opponent == 'r'):
#         return True
#
# print(play())
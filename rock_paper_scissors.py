
print(".......rock paper scissors game......")

p1 = input("Enter your turn, player 1: ").strip().lower()
p2 = input("Enter your turn, player 2: ").strip().lower()

valid_choices = ["rock", "paper", "scissors"]

if p1 not in valid_choices or p2 not in valid_choices:
    print("Invalid input! Please choose rock, paper, or scissors.")

elif p1 == p2:
    print("It's a draw!")
    print("Player 1 played =", p1)
    print("Player 2 played =", p2)

elif (
    (p1 == "rock" and p2 == "scissors")
    or (p1 == "paper" and p2 == "rock")
    or (p1 == "scissors" and p2 == "paper")
):
    print("Player 1 wins!")
    print("Player 1 played =", p1)
    print("Player 2 played =", p2)

else:
    print("Player 2 wins!")
    print("Player 1 played =", p1)
    print("Player 2 played =", p2)

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = input("What is your choice? Rock, Paper or scissors?").lower()
print(user)
computer = random.randint(0,2)
print(computer)

if user == "rock":
    choice = 0
    print(rock)
elif user == "paper":
    choice = 1
    print(paper)
elif user == "scissors":
    choice = 2
    print(scissors)
else:
    print("Input a valid choice")

if computer == 0:
    print("computer chose:")
    print(rock)
elif computer == 1:
    print("computer chose:")
    print(paper)
elif computer == 2:
    print("computer chose:")
    print(scissors)
else:
    print("Input a valid choice")

if choice == computer:
    print("It's a tie!")
elif choice == 2 and computer == 1:
    print("You win")
elif choice == 2 and computer == 0:
    print("You lose")
elif choice == 1 and computer == 2:
    print("You lose")
elif choice == 1 and computer == 0:
    print("You win")
elif choice == 0 and computer == 2:
    print("You win")
elif choice == 0 and computer == 1:
    print("You lose")
else:
    print("Try again")


# 2scissors x 2scissors : tie
# 2scissors x 1paper : winner
# 2scissors x 0rock : lose

# 1paper x 2scissor : lose
# 1paper x 1paper : tie
# 1paper x 0rock : win

# 0rock x 2scissor : win
# 0rock x 1paper : lose
# 0rock x 0rock : tie
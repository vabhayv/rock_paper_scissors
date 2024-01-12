import random
input("Wanna play rock paper scissors?\nTap enter to continue")
user = int(input("To select rock enter '1', to select paper enter '2', and for scissors enter '3' \n"))
choice1 = '''
     ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
choice2 = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''
choice3 = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
bot = random.randint(1,3)
if user == 1 and bot == 1:
    print(f"You choose: {choice1}\nBot choose: {choice1}")
    print("It's a draw")
elif user == 1 and bot == 2:
    print(f"You choose: {choice1}\nBot choose: {choice2}")
    print("Bot wins")
elif user == 1 and bot == 3:
    print(f"You choose: {choice1}\nBot choose: {choice3}")
    print("You won")
elif user == 2 and bot == 2:
    print(f"You choose: {choice2}\nBot choose: {choice2}")
    print("It's a draw")
elif user == 2 and bot == 3:
    print(f"You choose: {choice2}\nBot choose: {choice3}")
    print("Bot wins")
elif user == 2 and bot == 1:
    print(f"You choose: {choice2}\nBot choose: {choice1}")
    print("You wins")
elif user == 3 and bot == 3:
    print(f"You choose: {choice3}\nBot choose: {choice3}")
    print("It's a draw")
elif user == 3 and bot == 2:
    print(f"You choose: {choice3}\nBot choose: {choice2}")
    print("You wins")
elif user == 3 and bot == 1:
    print(f"You choose: {choice3}\nBot choose: {choice1}")
    print("Bot wins")

print("play again :)")
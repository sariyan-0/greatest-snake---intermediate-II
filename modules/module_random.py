############################ random ############################
import random


# A random integer between 10 and 20
# a = random.randint(10, 20)
# print(a)
#
# -------------------------------------------------------------
# A random integer between 10 and 20 (exclusive)
# b = random.randrange(10, 20, 2)
# print(b)
# -------------------------------------------------------------
#
# a = random.random()
# print(a * 100) # Gives a chance in %
#
# -------------------------------------------------------------
# a random choice from list, string, dict, and tuple
# lst = [10, 40, 3, 80, 22, 5, 90, 60]
# #
# a = random.choice(lst)
# print(a) # Picks an item from the list
# -------------------------------------------------------------
# Picks 3 random items from the list
# lst = [10, 40, 3, 80, 22, 5, 90, 60]
# a = random.choices(lst, k=3) # repetition is alloweda
# print(a)
#
# lst = [10, 40, 3, 80, 22, 5, 90, 60]
# a = random.sample(lst, k=3)  # repetition is NOT allowed
# print(a)
# -------------------------------------------------------------
#
# lst = [10, 40, 3, 80, 22, 5, 90, 60]
# random.shuffle(lst)
# print(lst)
###############################################################
# Q1: Generate a random mark
# a = random.randrange(0, 20)
# b = random.random()
# avg = round(a + b, 2)
# print(avg)
# -------------------------------------------------------------
# avg = 10 * random.random() + 10
# #
# print(avg)
###############################################################
# Q2: Generate a 8 character captcha code
#
# example:      "84Td5fU3"
# chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# cap = ""
# for item in range(8):
#     cap += random.choice(chars)

# print(cap)
# -------------------------------------------------------------
# Without repetition
# characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
# chars = random.sample(chars, k=8)
# cap = ""
# for char in chars:
#     cap += char
# print(cap)
###############################################################
# Q3: Rock Papar Scissors with the computer (computer has 70% chance of picking the rock)

# player = input("Enter rock, paper, or scissor: ")

# choices = ["rock", "paper", "scissor"]
# if random.random() < 0.7:
#     computer = "rock"
# else:
#     computer = random.choice(["paper", "scissor"])

# print("You chose:", player)
# print("Computer chose:", computer)

# if player not in choices:
#     print("Invalid choice!")
# elif player == computer:
#     print("It's a tie!")
# elif (player == "rock" and computer == "scissor") or (player == "paper" and computer == "rock") or (player == "scissor" and computer == "paper"):
#     print("You win!")
# else:
#     print("Computer wins!")


###############################################################
# Q4: computer wins 70% of the time

# player = input("Enter rock, paper, or scissor: ")

# p = random.random()
# if p <= 0.7:
    # check the players choice
    #       now computer has a better choice
# else:
        # check the players choice
        #       now computer has a worse choice



###############################################################
# what is the seed()function?
# random.seed() 
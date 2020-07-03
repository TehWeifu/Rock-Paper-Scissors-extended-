# Write your code here
import random
read_file = open('rating.txt', 'r')
winners = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
           'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
           'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
           'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
           'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
           'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
           'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
           'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
           'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
           'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
           'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
           'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
           'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
           'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
           'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']
           }
score = 0

name = input("Enter your name: ")
print("Hello,", name)
for line in read_file:
    data = line.split()
    if data[0] == name:
        score = int(data[1])

input_options = input()
if input_options == "":
    input_options = "rock,paper,scissors"
options = input_options.split(',')
print("Okay, let's start")

human_choice = input()
pc_choice = random.choice(options)

while human_choice != "!exit":
    if human_choice in options:
        if pc_choice == human_choice:
            print("There is a draw({})".format(pc_choice))
            score += 50
        else:
            if pc_choice not in winners[human_choice]:
                print("Sorry, but computer chose {}".format(pc_choice))
            else:
                print("Well done. Computer chose {} and failed".format(pc_choice))
                score += 100
        human_choice = input()
        pc_choice = options[random.randint(0, 2)]
    elif human_choice == "!rating":
        print("Your rating:", score)
        human_choice = input()
    else:
        print("Invalid input")
        human_choice = input()

print("Bye!")
read_file.close()

# hello this is a guessing game I made to showcase my beginner skills in python.
# I spent a whole week learning and taking notes on the basics of python.
# the computer has a number stored and the player(you) guess that number.

player_name = input("Input name: ") # player will enter their name here
print("hello " + player_name)     # player's name will be printed with a greeting
computer_num = 7            # the computer will hold the memory of the number 7
print("guess a number from the numbers shown")  # the player will guess a number
for number in range(21):        # Creating a range of numbers excluding 21
    print(number, end=", ")     # learned this trick from online to make my range print hamburger instead of hotdog style.
while True:                     # used a while loop because I wanted a loop that wouldn't end until the correct number was guessed.
    player_num = input("guess a number: ")  # This is where the player(you) get to input a number
    if int(player_num) == computer_num:     # if the players number is the number that the computer has (7) then the game will break or end if you put.
        break # this is a built-in function that immediately ends the while loop.
    print("you're too far, try again.")     # I initially wanted to make an if else function where if the player guesses a number higher that of equal to 8 the console would print you've gone too far up. And another if else function, if it was too low.
print(f"you entered the correct number yay!: {player_num}") # this will print a win text along with showcasing the players number.

# Sorry if I over did it, my brain likes to overthink every aspect of code before actually implementing the code.
# can't just make things simple


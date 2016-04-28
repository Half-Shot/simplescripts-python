# IFs n Booleans

answer = input("Do you speak english?")

answer = answer.lower() # We convert to lowercase like this, because python is case sensitive.

if answer == "yes":
    print("Good, then you should understand Half-Shot")
elif answer == "no":
    print("That's a sh---what?")
else: # Do something else
    print("Doesn't sound like you do. Not much I can do for you man :/")



# Quick note on booleans.

# Booleans can be either True or False

booleanValue = False

# You can write booleanValue == True or just booleanValue, it means the same thing

if booleanValue:
    print("I will never be printed :(")

# Similarly, you can use not booleanValue in place of booleanValue == False

if not booleanValue:
    print("I will always be printed :)")





# Comparing numbers

# You cannot compare a string with a number

if "1" == 1:
    print("This won't EVER be printed")

if 1 < 2:
    print("1 is indeed less than two")

if 3 > 2:
    print("Okay, you get the point")

# >= is more than or equal to.
# <= is less than or equal to.

BooleanA = True

# You can string together multiple conditions like this

if BooleanA and (1 < 5):
    print("One is less than 5 and the boolean is good.")

# You can also have an or

if BooleanA or (1 > 5):
    print("We are at least half right, heh.")

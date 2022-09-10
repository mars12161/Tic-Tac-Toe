welcome = """
Welcome to Tic Tac Toe! This is how it looks like:

    1   |   2   |   3
  ______|_______|______
    4   |   5   |   6
  ______|_______|______
    7   |   8   |   9
        |       |

You are drawing the X. Type in the number of the position where you want
to place your X.
"""

print(welcome)



field = """ 
    1   |   2   |   3
  ______|_______|______
    4   |   5   |   6
  ______|_______|______
    7   |   8   |   9 
        |       |
""" 

idx = 0
while idx < 3:
    number = input("Enter your number: ")
    idx += 1
    print(field)
    print(number)
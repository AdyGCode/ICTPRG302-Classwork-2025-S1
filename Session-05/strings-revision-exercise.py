# Revision Exercise for Strings
#
# Filename: strings-revision-exercise.py
# Location: Session-05
#
# URI:      
# Author: Rafael Avigad
#
# Instructions:
#     Copy the file from


# Define variables
tic_tac = ("- X O\n" +
           "X - X\n" +
           "O - O\n"   )
# helpful reference
#012345678912345678
'- X OnX - XnO - On'

# what is the length of the string?
# insert code here

# make the following print True by substituting
# each `?` with a **different** value
print(tic_tac[0] ==
      tic_tac[?] ==
      tic_tac[?]) # True

# clue: Here is an example that prints True:
# print(tic_tac[0] == tic_tac[0] == tic_tac[0])
# but remember you must use different integer values!
# notice that line breaks don't matter inside brackets

print(tic_tac[2] ==
      tic_tac[?] ==
      tic_tac[?]) # True

print(tic_tac[5] ==
      tic_tac[?] ==
      tic_tac[?]) # True

# combine two slices of the original string
# for X to win the game:
print(tic_tac[?:?] + 'X' + tic_tac[?:?])
# should print:
# - X O
# X X X
# O - O
# combine two slices of the original string
# for O to win the game:
print(tic_tac[?:?] + 'O' + tic_tac[?:?])
# should print:
# - X O
# X - X
# O O O

# Bonus question!
# Complete the following to print 'XXX'
print(tic_tac[?:?:?])

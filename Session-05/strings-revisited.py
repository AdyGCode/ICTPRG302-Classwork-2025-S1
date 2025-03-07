# Filename: strings-revisited.py
# Location: Session-05

tic_tac = "- X O\n" + "X - X\n" + "O - O\n"

# - X O\nX - X\nO - O\n
#            11 111111
# 012345 678901 234567

# Write the code to print the length of the string
print(len(tic_tac))

# Write the code to print ONLY the 13th character
print(tic_tac[12] )

# Write the code to show only the first 5 characters
print(tic_tac[0:5] )

# Write the code to show characters 8 to 10
print(tic_tac[7:10])

# Write the code to print every other character.
print(tic_tac[0:18:2])
print(tic_tac[::2])

# Various other tricks
print(tic_tac.lower())
print(tic_tac.upper())
print(tic_tac.title())
print(tic_tac[0:5].center(50))
print(tic_tac.capitalize()) # oooh, this doesn't capitalise single letters
print(tic_tac.replace('O','P'))

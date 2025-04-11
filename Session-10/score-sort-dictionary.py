# For details / explanation see:
#       https://realpython.com/sort-python-dictionary/

lines = [
    "25, Trump school for Bankers",
    "12, Stephenson's school for engineers",
    "5, Javier's School for Cops and Robbers",
    "45, Isaac Newton School for Geniuses"
]

scores= {}
for line in lines:
    score, school = line.split(",")
    scores[school.strip()]=int(score)
print(scores)

# Sort by the School name
scores = dict(sorted(scores.items()))
print(scores)

# Sort by the score
scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(scores)



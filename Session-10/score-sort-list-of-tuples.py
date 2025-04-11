# For details / explanation see:
#       https://learnpython.com/blog/sort-tuples-in-python/

lines = [
    "Trump school for Bankers, 25",
    "Stephenson's school for engineers, 12",
    "Javier's School for Cops and Robbers, 5",
    "Isaac Newton School for Geniuses, 4"
]

scores = []
for line in lines:
    school , score= line.split(",")
    scores.append( (school.strip(), int(score)) )
print(scores)

# Sort by the School name
scores.sort()
print(scores)

# Sort by the score
scores.sort(key=lambda item: item[1], reverse=True)
print(scores)


for name,score in scores:
    print(name.ljust(20) + " --> " + str(score))


# "Name",Score

file_handle = open("demo_file.txt","w")
for name,score in scores:
    file_handle.write('"' + name + '",'+ str(score)+"\n")
file_handle.close()
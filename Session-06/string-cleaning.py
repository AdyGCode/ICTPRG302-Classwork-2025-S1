the_sentence = "The Quick Brown Fox. It was asleep on the bed."
the_sentence = the_sentence.lower()

clean_sentence = ""

for character in the_sentence:
  if character.isalpha() or character == " ":
    clean_sentence += character

print(the_sentence)
print(clean_sentence)
# Dictionary Exercises

## filename: exercise-01.py

Write a Python script to concatenate the following 
dictionaries to create a new one.

```python
dictionary_1 = {1:10, 2:20}
dictionary_2 = {3:30, 4:40}
dictionary_3 = {5:50, 6:60}
```

Expected Result :

```text
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

## filename: exercise-02.py

Write a Python script that:
- asks the user to input a number
- when the number is entered, it checks to see if
  the number is in the dictionary's keys
- if the key is found it outputs "Fount it!"
  followed by the value for the key

```python
value_dictionary = {
    1: "Hello", 
    2: "Goodbye", 
    3: "Who is this?"
} 
```

## filename: exercise-03.py

Write a Python script that calculates the total of the values from a dictionary.

In this example the dictionary will contain the rainfall for a week.

```python
week_rainfall = {
  "Mon":0,
  "Tue":3,
  "Wed":7,
  "Thu":1,
  "Fri":2,
  "Sat":6,
  "Sun":23
}
```

The program should output the result in the form:

```text
Total Rainfall: 45 mm
```


## filename: exercise-04.py

Write a Python script that asks the user for a sentence, and then counts the 
words in the sentence, and displays the results to the user. 

We are providing you with the pseudocode to help.

```python
# Ask user for sentence
sentence = input('Enter a sentence (without punctuation): ')

# Create an empty dictionary called word_counts

# Split the sentence into words

# For each word in the sentence:
#   If word is in the word_counts dictionary:
#       Increment the count for the word
#   Else:
#       Make the count for the word 1
#
# For each word in the word_count dictionary:
#   Display word, count
```
The output should be similar to this:

```text
Word Count
The 2
quick 1
brown 1
fox 1
```

Sample sentences:

- The quick brown fox jumps over the lazy dog who was watching the tabby cat
- Mary had a little lamb, it's fleece as white as snow, and everywhere that 
  mary went the lamb was sure to go
- She sells seashells by the sea shore. The shells she sells are surely 
  seashells. So if she sells shells on the seashore, I'm sure she sells 
  seashore shells.

### Hint:
You could use some of the following example code to remove any numbers and 
punctuation from the sentence before splitting it into words.

The code uses a predefined sentence and does the following:
- converts the sentence to lower case
- creates an empty clean sentence string
- loops though each character in the sentence:
  - if the characters is in teh alphabet or is a space then
    - join the character to the clean sentence
- print out the original sentence
- print out the clean sentence

```python
the_sentence = "The Quick Brown Fox. It was asleep on the bed."
the_sentence = the_sentence.lower()

clean_sentence = ""

for character in the_sentence:
  if character.isalpha() or character == " ":
    clean_sentence += character

print(the_sentence)
print(clean_sentence)    
```

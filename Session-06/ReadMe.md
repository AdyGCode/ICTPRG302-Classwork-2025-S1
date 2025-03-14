# Session 06: Dictionary & File Reading Exercises

These exercises are for you to use as practice.

Make mistakes, correct them and enjoy the success as you complete each one.

If you are stuck, then ask for assistance from your lecturer, or from the
lecturer who is holding a Workshop Lab.


## Text files and other assets

The text files and other assets (for example, images) are saved in an 
`assets` folder within this session's folder.

Sometimes files will be linked to from previous session folders to reduce 
duplication and errors from said duplication. 


## Filename: exercise-01.py

Write a Python script to concatenate the following
dictionaries to create a new one.

```python
dictionary_1 = {1: 10, 2: 20}
dictionary_2 = {3: 30, 4: 40}
dictionary_3 = {5: 50, 6: 60}
```

Expected Result:

```text
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

## Filename: exercise-02.py

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

## Filename: exercise-03.py

Write a Python script that calculates the total of the values from a dictionary.

In this example the dictionary will contain the rainfall for a week.

```python
week_rainfall = {
    "Mon": 0,
    "Tue": 3,
    "Wed": 7,
    "Thu": 1,
    "Fri": 2,
    "Sat": 6,
    "Sun": 23
}
```

The program should output the result in the form:

```text
Total Rainfall: 45 mm
```

## Filename: exercise-04.py

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
The 1
quick 1
brown 1
fox 1
jumps 1
over 1
the 1
lazy 1
dog. 1
```

> **Words that have punctuation in or around them will be counted separately.**

Sample sentences:

- The quick brown fox jumps over the lazy dog who was watching the tabby cat
- Mary had a little lamb, it's fleece as white as snow, and everywhere that
  mary went the lamb was sure to go
- She sells seashells by the sea shore! The shells she sells are surely
  seashells. So if she sells shells on the seashore, I'm sure she sells
  seashore shells.

## Filename: exercise-05.py

Copy the code from exercise 4.

Make the program convert the words to lower case so `The`, `THE` and `the` are
all counted as the same word.

> **This version will remove all punctuation, so words such as `I'm` and
> `it's` will be seen as `im` and `its` for the purpose of this exercise.


The output should be similar to this:

```text
Word Count
the 2
quick 1
brown 1
fox 1
jumps 1
over 1
lazy 1
dog 1
```

### Hint:

You could use some of the following example code to remove any numbers and
punctuation from the sentence before splitting it into words.

The code uses a predefined sentence and does the following:

- converts the sentence to lower case
- creates an empty clean sentence string
- loops though each character in the sentence:
    - if the characters is in the alphabet or is a space then
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

## Filename: exercise-06.py

Create a new Python script, and add the code below:

```python
file = open("assets/quick.txt", "r")
quicktext = file.read()
print(quicktext)
```

If you have not done so already, create a file called `quick.txt` (In
PyCharm: Point to the folder to add the file, Right Mouse Click, Hover over
New, then click on File. Type in `quick.txt`).

Add the following text:

```text
The
quick
brown
fox
jumped
over
the lazy
dog
```

Save the file using <kbd>CTRL</kbd>+<kbd>S</kbd>.

Now run your `exercise-06.py` script.

You should see the file's content.

## Filename: exercise-07.py

Use the following link to download the [romeojuliet.txt](assets/romeojuliet.txt)
file.

Create a new Python script and call it `exercise-07.py`.

Copy the code from `exercise-06.py` and paste into the new file.

Modify the code to open, read and display the contents of
the [romeojuliet.txt](assets/romeojuliet.txt) file.

The output should look like this:

```text
All that glitters is not gold
Fair is foul, and foul is fair: Hover through the fog and filthy air.
These violent delights have violent ends...
By the pricking of my thumbs, Something wicked this way comes. Open, locks, Whoever knocks!
Hell is empty and all the devils are here.
Brevity is the soul of wit.
If music be the food of love, play on.
Good night, good night! parting is such sweet sorrow, That I shall say good night till it be morrow.
Now is the winter of our discontent.
```

# Acknowledgement

Some of these exercises are based on the resources from
[ncce.io/tcc](ncce.io/tcc). They are licensed under the Open Government
Licence, version 3. For more information on this licence,
see [ncce.io/ogl](ncce.io/ogl).

More exercises will be available in [Session-07](../Session-07).

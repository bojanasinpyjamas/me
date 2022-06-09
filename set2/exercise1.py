"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform # imports a set of data? makes it information

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"] # 16.59 defines the words in the bracket as a list 'some_words'

for word in some_words:
    print(word) # retrieves word? prints the word in the ""

for x in some_words:
    print(x) #prints the list as "0,1,2"

print(some_words) #prints the list

if len(some_words) > 3:
    print("some_words contains more than 3 words") #if length of list is > than 3 items, print the text


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #prints the uname data with the definition where it's retrieved from?


usefulFunction()

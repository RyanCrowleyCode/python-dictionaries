"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

word_definitions["cat"] = "An animal that wakes me up in the morning for food. Can be cudly and irritating simultaneously."

word_definitions["child"] = "A small human creature that loves eggnog, guitars, and Curious George."


"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["Awesome"] = "The feeling of students when they are learning Python"

word_definitions["Ryan"] = "Me, Myself, and I, as well as Me, Bishop, and Cunningham."

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["cat"])
print()
print(word_definitions["child"])
print()


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for word in word_definitions:
    print(f"The definition of {word} is {word_definitions[word]}")
    print()
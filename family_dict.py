# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    "younger sister": {
        "name": "Molly",
        "age": 28
    },
    "older sister": {
        "name": "Brianna",
        "age": 35
    },
    "wife": {
        "name": "Erica",
        "age": 27
    },
    "son": {
        "name": "Peter",
        "age": 2
    },
}

# print(my_family.items())
# for key, value in my_family.items():
#     print(f"key: {key}, value: {value}")
#     print(value["name"])

# Using a dictionary comprehension, produce output that looks like the following example.
# Krista is my sister and is 42 years old

family_strings = [ f'{value["name"]} is my {key} and is {value["age"]} years old' for key, value in my_family.items() ]

for string in family_strings:
    print(string)

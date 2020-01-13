# Create an empty dictionary
animal = dict()
# Add k/v pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

# create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}

# Dictionaries are iterable
for (key, value) in animal.items():
    print(f"{key}: {value}")
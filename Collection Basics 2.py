"""Task 1
Create a variable called person which should hold a dictionary.
The dictionary should have the key name with the value Bart Simpson
and the key address with the value 742 Evergreen Terrace.
Print the name and the address separated by comma to the screen.

Your result should look like this:
Bart Simpson, 742 Evergreen Terrace"""

# Solution 1
# create a dictionary called "person" with key-value pairs for name and address
person = {"name": "Bart Simpson", "address": "742 Evergreen Terrace"}

# concatenate the value of the "name" key and a comma and a space and the value of the "address" key, 
# and print the resulting string to the console
print(person["name"] + ", " + person["address"])

print("__________________________________________________")

# Solution 2
# create a dictionary called "person" with key-value pairs for name and address
person = {"name": "Bart Simpson", "address": "742 Evergreen Terrace"}

# use the .format() method to create a string with placeholders for name and address,
# then insert the corresponding values from the "person" dictionary
output_string = "{}, {}".format(person["name"], person["address"])

# print the resulting string to the console
print(output_string)

print("__________________________________________________")

# Solution 3
# create a dictionary called "person" with key-value pairs for name and address
person = {"name": "Bart Simpson", "address": "742 Evergreen Terrace"}

# use f-strings to embed the values of the "name" and "address" keys directly in the output string
output_string = f"{person['name']}, {person['address']}"

# print the resulting string to the console
print(output_string)

print("__________________________________________________")

"""Task 2
Create two variables one called bart and the other called homer.
Each stores a dictionary, one with the key name and the value Bart Simpson,
the other one with the same key but the value Homer Simpson.
Create a third variable address with a dictionary which only has one key address.

Use update to add the address to both bart and homer.
 Print bart['address'] to the screen.

Your result should look like this:
742 Evergreen Terrace"""

# Solution 1
# create a dictionary called "bart" with key-value pair for name
bart = {"name": "Bart Simpson"}

# create a dictionary called "homer" with key-value pair for name
homer = {"name": "Homer Simpson"}

# create a dictionary called "address" with a single key "address" and its value
address = {"address": "742 Evergreen Terrace"}

# use the update() method to add the "address" dictionary to both "bart" and "homer"
bart.update(address)
homer.update(address)

# print the value associated with the "address" key in the "bart" dictionary
print(bart["address"])

print("__________________________________________________")

# Solution 2
# create a dictionary called "bart" with key-value pair for name
bart = {"name": "Bart Simpson"}

# create a dictionary called "homer" with key-value pair for name
homer = {"name": "Homer Simpson"}

# create a dictionary called "address" with a single key "address" and its value
address = {"address": "742 Evergreen Terrace"}

# add the "address" dictionary to both "bart" and "homer" using the copy() method
bart = bart.copy()
bart.update(address)

homer = homer.copy()
homer.update(address)

# print the value associated with the "address" key in the "bart" dictionary
print(bart["address"])

print("__________________________________________________")


# Solution 3
# create a dictionary called "bart" with key-value pair for name
bart = {"name": "Bart Simpson"}

# create a dictionary called "homer" with key-value pair for name
homer = {"name": "Homer Simpson"}

# create a dictionary called "address" with a single key "address" and its value
address = {"address": "742 Evergreen Terrace"}

# add the "address" dictionary to both "bart" and "homer" using dictionary unpacking
bart = {**bart, **address}
homer = {**homer, **address}

# print the value associated with the "address" key in the "bart" dictionary
print(bart["address"])

print("__________________________________________________")


"""Task 3
Create a variable ages which holds a dictionary with the key Peter
and the value 36, the key Robin and the value 29 and the key Michael
with the value 33. Loop over the dictionary and print the name with the age.

Your result should look like this:
Peter is 36 years old
Robin is 29 years old
Michael is 33 years old"""

# Solution 1
# create a dictionary called "ages" with key-value pairs for name and age
ages = {"Peter": 36, "Robin": 29, "Michael": 33}

# loop over the dictionary and print the name and age for each person
for name, age in ages.items():
    print(f"{name} is {age} years old")

print("__________________________________________________")

# Solution 2
# create a dictionary called "ages" with key-value pairs for name and age
ages = {"Peter": 36, "Robin": 29, "Michael": 33}

# loop over the dictionary and print the name and age for each person
for name in ages:
    age = ages[name]
    print(name + " is " + str(age) + " years old")

print("__________________________________________________")

# Solution 3
# create a dictionary called "ages" with key-value pairs for name and age
ages = {"Peter": 36, "Robin": 29, "Michael": 33}

# create a list comprehension that interpolates the name and age for each person
age_strings = [f"{name} is {age} years old" for name, age in ages.items()]

# join the strings in the list with a newline character and print the result
print('\n'.join(age_strings))

print("__________________________________________________")


"""Task 4
Store the animals Alligator, Tiger, Parrot, Hamster, and Dolphin
as keys in a dict. Use random numbers as values. 
Now remove all keys ending with r from the dictionary and print
the resulting dict to the screen.

Your result should look similar to this:
{'Dolphin': 8, 'Parrot': 2}"""

# Solution 1
import random

# create the initial dictionary with animal names as keys and random values
animals = {"Alligator": random.randint(1, 10),
           "Tiger": random.randint(1, 10),
           "Parrot": random.randint(1, 10),
           "Hamster": random.randint(1, 10),
           "Dolphin": random.randint(1, 10)}

# create a list of keys to remove
keys_to_remove = [key for key in animals.keys() if key.endswith('r')]

# remove the keys from the dictionary
for key in keys_to_remove:
    animals.pop(key)

# print the resulting dictionary
print(animals)

print("__________________________________________________")

# Solution 2
import random
# create the initial dictionary with animal names as keys and random values
animals = {"Alligator": random.randint(1, 10),
           "Tiger": random.randint(1, 10),
           "Parrot": random.randint(1, 10),
           "Hamster": random.randint(1, 10),
           "Dolphin": random.randint(1, 10)}

# use a dictionary comprehension to create a new dictionary with keys that don't end with "r"
animals_no_r = {key: value for key, value in animals.items() if not key.endswith('r')}

# print the resulting dictionary
print(animals_no_r)

print("__________________________________________________")

# Solution 3
import random
# create the initial dictionary with animal names as keys and random values
animals = {"Alligator": random.randint(1, 10),
           "Tiger": random.randint(1, 10),
           "Parrot": random.randint(1, 10),
           "Hamster": random.randint(1, 10),
           "Dolphin": random.randint(1, 10)}

# use the filter() function to remove all keys that end with "r"
animals_no_r = dict(filter(lambda item: not item[0].endswith("r"), animals.items()))

# print the resulting dictionary
print(animals_no_r)


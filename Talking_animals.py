# Define speak below:
import random
animals = ['pig', 'duck', 'cat', 'dog']

animal = random.choice(animals)

print(animal + ' is doing ...')

def speak(animal):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    else:
        return "woof"
print(speak(animal))
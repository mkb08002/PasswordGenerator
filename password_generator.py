import random
import string

# Noun and Adjective Files

with open('password_generator\english-adjectives.txt') as adjectives_file:
    adjectives = adjectives_file.read().splitlines()
adjective_random = random.choice(adjectives)


with open('password_generator\english-nouns.txt') as nouns_file:
    nouns = nouns_file.read().splitlines()
noun_random = random.choice(nouns)

sp_char = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '+', '=']

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Function to create password
def password_generator():
    sp_char_random = random.choice(sp_char)
    num_random = random.choice(num)
    password = adjective_random + sp_char_random + noun_random + num_random + num_random + num_random

    print("Your password is " + password)


# Begin
password_generator()
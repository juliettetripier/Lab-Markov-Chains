"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)

    words = file.read()

    return words.split()

list_of_words = open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
   


    # your code goes here
    # for idx, word in zip(list_of_words[0:-1], list_of_words[1:]):
    #     chains[idx].append(word)
        # put word and the word that follows it into a tuple, and make that a key in the dictionary
        # the word that comes after that could go into the list of values?
        # need to check if the key already exists in the dictionary
            # if it does, append the following word to the list of values
            # if not, add that key to the dictionary and create a list of values w/ the following word in it
        # new_tuple = word[i] and word[i+1] but in a tuple
        # value could be empty list, append word[i+2] into it?
        # chains[new_tuple] = value list

    for idx in range(0, len(list_of_words) - 2):
        # idx = 0
        key = (list_of_words[idx], list_of_words[idx+1])
        new_value = list_of_words[idx+2]
        if key in chains:
            # value = chains[key] # make sure we refer to the right place in the dict
            # value.append(new_value)
            chains[key].append(new_value)
        else:
            # value = []
            # value.append(new_value)
            # chains[key] = value
            chains[key] = []
            chains[key].append(new_value)

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []
# value = dictionaryname[key]
    random_key = random.choice(list(chains.keys()))
    all_values_for_key = chains[random_key]
    random_value = random.choice(all_values_for_key)
    #value = random.choice(list(chains.keys()))

    for word in random_key:
        words.append(word)
    words.append(random_value)

    while True:
        new_key = tuple(words[-2:])
        new_key_values = chains.get(new_key) # .get() returns None if that key isn't in the dictionary
        if new_key_values == None:
            break
        new_value = random.choice(new_key_values)
        #for word in new_key:
        words.append(new_value)
            #return ' '.join(words)

    return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print(chains)
# ('house?', 'Would'): ['you', 'could', 'you', 'with']

# Produce random text
random_text = make_text(chains)

print(random_text)

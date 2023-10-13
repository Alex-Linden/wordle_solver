import random
import string

# Set the seed for reproducibility (optional)
# random.seed(42)

# Define the function to generate random words
def generate_random_words(num_words, word_length):
    words = []
    for _ in range(num_words):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        words.append(word)
    return words

# Generate 50 random 5-letter words
random_words = generate_random_words(50, 5)

# Print the list of random words
print(random_words)


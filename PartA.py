import sys # For accepting terminal arguments.

# tokenize(text_file) takes a file provided from an argument, reads the text, strips punctuation, then returns a list of tokens (words) from the text.
# Runtime complexity should be O(n) as the function's work relies on the number of characters in the text file.
def tokenize(text_file_path):
    with open(text_file_path, 'r', encoding='utf-8', errors='ignore'):
        text = file.read()
        unhyphenated_text = text.replace('-', ' ') # Space instead of hyphen to separate words that are hyphenated. The canvas example shows 'driver-partner' and 'driver' sharing the word 'driver'.
        unpunctuated_text = ''.join(char for char in unhyphenated_text if char.isascii() and (char.isalnum() or char.isspace())) # Creates a list of characters from unhyphenated_text that are alphanumeric or whitespace (ONLY ASCII CHARACTERS), then joins them back together into a string.
        casefolded_text = unpunctuated_text.casefold()  # Convert text to lowercase for case-insensitive comparison.
        tokenized_text = casefolded_text.split() # Split the casefolded text into tokens (words) based on whitespace.
        return tokenized_text

# computeWordFrequencies(tokens) takes a list of tokens and returns a dictionary with the frequency of each token in the list (in descending order).
# Runtime complexity should be O(nlogn) as the function's work relies on the number of tokens in the list (O(n)) and the sorting operation (O(nlogn)).
def computeWordFrequencies(tokens):
    word_frequencies = {}
    for token in tokens:
        if token in word_frequencies: # If the token is already in the dictionary, increment its frequency count by 1.
            word_frequencies[token] += 1
        else: # If the token is not in the dictionary, add it as a key with a frequency count of 1.
            word_frequencies[token] = 1

    # Sort the word frequencies dictionary by frequency in descending order. If there are ties, order them alphabetically.
    word_frequencies = dict(sorted(word_frequencies.items(), key=lambda item: (-item[1], item[0])))
    return word_frequencies

# printFrequencies(frequencies) takes a dictionary of word frequencies and prints each word and its frequency in the format "word: frequency".
# Runtime complexity should be O(n) as the function's work relies on the number of items in the dictionary.
def printFrequencies(frequencies):
    print('Word Frequencies:')
    for word, frequency in frequencies.items(): # Loop through the dictionary of word frequencies and print each word and its frequency in the format "word - frequency".
        print(f'{word} - {frequency}')
    print('')

if __name__ == '__main__':# Prevents executable code from running when this file is imported as a module in another file.
    if len(sys.argv) < 2:
        print('Missing Arguments: python PartA.py <file1>')
        sys.exit(1)

    # Storing the file argument in a variable.
    file_arg1 = sys.argv[1]

    # Storing tokenized list through the tokenize function (using our file variable as an argument).
    tokens1 = tokenize(file_arg1)

    # Storing the word frequencies dictionary through the computeWordFrequencies function (using our tokenized list variable as an argument).
    frequencies1 = computeWordFrequencies(tokens1)

    # Printing the word frequencies dictionary through the printFrequencies function (using our word frequencies dictionary variable as an argument).
    printFrequencies(frequencies1)
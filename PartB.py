import PartA
import sys

# commonTokens(tokens1, tokens2) takes two lists of tokens and returns a list of tokens that are common to both lists (no duplicates).
# Runtime complexity should be O(n*m) as the function's work relies on the number of tokens in both lists.
def commonTokens(tokens1, tokens2):
    common_tokens = []
    for token in tokens1: # Loop through the list 'tokens1'.
        if token in tokens2: # If any token in 'tokens1' is also in 'tokens2', check if we've added that token to the list.
            if token not in common_tokens: # If it's not in the list, add it to the list. Otherwise, skip it to avoid duplicates.
                common_tokens.append(token)
    common_tokens.sort() # Sort the list of common tokens alphabetically.
    return common_tokens

# printCommonTokens(common_tokens) takes a list of common tokens and prints each token in the list. It also prints the number of common tokens in the list.
# Runtime complexity should be O(n) as the function's work relies on the number of common tokens in the list.
def printCommonTokens(common_tokens):
    print('Common Tokens:')
    for token in common_tokens: # Loop through the list of common tokens and print each token in the list.
        print(f'{token}')
    print(f'Number of Common Tokens: {len(common_tokens)}') # Print the number of common tokens in the list after the loop has finished.
    print('')

if __name__ == '__main__':
    if len(sys.argv) != 3: # Error if missing our required 2 arguments.
        print('Missing Arguments: python PartB.py <file1> <file2>')
        sys.exit(1)

    # Storing the file arguments in variables.
    file_arg1 = sys.argv[1]
    file_arg2 = sys.argv[2]

    # Storing tokenized lists through PartA's tokenize function (using our file variables as arguments).
    tokens1 = PartA.tokenize(file_arg1)
    tokens2 = PartA.tokenize(file_arg2)

    # Storing the common tokens list through the commonTokens function (using our tokenized list variables as arguments).
    common_tokens = commonTokens(tokens1, tokens2)

    # Printing the common tokens list through the printCommonTokens function (using our common tokens list variable as an argument).
    printCommonTokens(common_tokens)
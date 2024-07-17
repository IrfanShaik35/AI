from itertools import permutations

# Function to convert the letters to numbers based on a given permutation
def letters_to_number(word, mapping):
    return int(''.join(mapping[letter] for letter in word))

# Function to check if the given permutation solves the puzzle
def is_solution(perm):
    mapping = {letter: str(digit) for letter, digit in zip(unique_letters, perm)}
    
    send = letters_to_number('SEND', mapping)
    more = letters_to_number('MORE', mapping)
    money = letters_to_number('MONEY', mapping)
    
    return send + more == money

# Define the unique letters in the problem
unique_letters = 'SENDMOREY'

# Generate all permutations of the digits 0-9 of length equal to the number of unique letters
for perm in permutations(range(10), len(unique_letters)):
    # Check if the current permutation is a solution
    if is_solution(perm):
        # Create a mapping from letters to digits
        mapping = {letter: str(digit) for letter, digit in zip(unique_letters, perm)}
        
        # Output the solution
        print("Solution found:")
        print(f"SEND  = {letters_to_number('SEND', mapping)}")
        print(f"MORE  = {letters_to_number('MORE', mapping)}")
        print(f"MONEY = {letters_to_number('MONEY', mapping)}")
        break
else:
    print("No solution found.")

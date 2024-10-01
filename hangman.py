import random

def get_random_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print("Welcome to Hangman!")
    
    # Select a random word
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Number of attempts allowed
    
    # Main game loop
    while attempts > 0:
        # Display the word with guessed letters
        print("\n" + display_word(word, guessed_letters))
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single valid letter.")
            continue
        
        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            
            # Check if the player has guessed the entire word
            if set(word).issubset(guessed_letters):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts remaining.")
        
        # If no attempts left, the game is over
        if attempts == 0:
            print(f"\nGame Over! The word was: {word}")
            break

# Run the game
if __name__ == "__main__":
    hangman()

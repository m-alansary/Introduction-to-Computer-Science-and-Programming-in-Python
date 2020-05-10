# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_len = len(secret_word)
    i = 0
    
    for char1 in secret_word :
        for char2 in letters_guessed:
            if char1 == char2 :
                i += 1
    if i == secret_word_len:
        return True
    else :
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_guessed_len = len(letters_guessed)
    word_letters_guessed = ""
    
    for char1 in secret_word :
        i=0
        for char2 in letters_guessed:
            if char1 == char2 :
                word_letters_guessed += char1 + " "
                break
            elif char1 != char2 :
                i += 1
            if i == letters_guessed_len :
                word_letters_guessed += "_ "
                break
    return word_letters_guessed


def letter_repeat(secret_word, letter):
    
    letter_repeat_times = 0
    
    for char1 in secret_word :
        for char2 in letter:
            if char1 == char2 :
                letter_repeat_times += 1
    return letter_repeat_times


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    string.ascii_lowercase
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    available_letters = ""
    
    for char1 in english_letters :
        for char2 in letters_guessed :
            if char1 == char2 :
                break
            else :
                available_letters += char1
                break
    return available_letters
                
            
                        
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    word_list = load_words()
    secret_word = choose_word(word_list)
    guesses_left = 6
    secret_word_len = len(secret_word)
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    letters_guessed = ""
    warning = 3
    num_guessed_right = 0
    vowels = "aeiou"
    score = 0
    print("Welcome to the hangman game")
    print("I am thinking of a word that is", secret_word_len, "letters long")
    print("_ " * secret_word_len)
    print("You have", guesses_left, "guesses left")
    print ("You have", warning, "warnings left" )
    print("Available letters ", english_letters)
    print ("----------------------")
    while True :
        check = False
        check2 = True
        letter = input("please guesse a letter: ")
        for char1 in letters_guessed :
            for char2 in letter :
                if char1 == char2 :
                    warning -= 1
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left :")
                    print ("----------------------")
                    print("You have", guesses_left, "guesses left")
                    available_letters = get_available_letters(letters_guessed)
                    print("Available letters ", available_letters)
                    letter = input("please guesse a letter: ")
                    if warning == 0:
                        guesses_left -= 1
                        warning =3
        if letter == "*":
            my_word = get_guessed_word(secret_word, letters_guessed)
            possible_matches = show_possible_matches(my_word)
            print("Possible word matches are: ")
            print(possible_matches)
            print("You have", guesses_left, "guesses left")
            available_letters = get_available_letters(letters_guessed)
            letter = input("please guesse a letter: ")
        while str.isalpha(letter) == False or len(letter) > 1 :
            warning -= 1
            print("Oops! That is not a valid letter.")
            print("you have", warning, "warning left")
            print("You have", guesses_left, "guesses left")
            letter = input("Enter one alphabetic letter: ")
            if warning == 0:
                guesses_left -= 1
                warning =3
        for char1 in letters_guessed :
            for char2 in letter :
                if char1 == char2 :
                    warning -= 1
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left :")
                    print ("----------------------")
                    print("You have", guesses_left, "guesses left")
                    available_letters = get_available_letters(letters_guessed)
                    print("Available letters ", available_letters)
                    letter = input("please guesse a letter: ")
                    if warning == 0:
                        guesses_left -= 1
                        warning =3
                        
        letters_guessed += letter
        if letter == "*":
            my_word = get_guessed_word(secret_word, letters_guessed)
            possible_matches = show_possible_matches(my_word)
            print("Possible word matches are: ")
            print(possible_matches)
            print("You have", guesses_left, "guesses left")
            available_letters = get_available_letters(letters_guessed)
            letter = input("please guesse a letter: ")
        for char1 in secret_word :
            for char2 in letter :
                if char1 == char2 :
                    check = True
                    break
        if check :
            letter_repeat_times = letter_repeat(secret_word, letter)
            num_guessed_right += letter_repeat_times
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            print ("----------------------")
            available_letters = get_available_letters(letters_guessed)
            print("You have", guesses_left, "guesses left")
            print("Available letters ", english_letters)
        else :
            for char1 in vowels :
                for char2 in letter:
                    if char1 == char2 :
                        print ("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                        print ("----------------------")
                        if guesses_left > 1 :
                            guesses_left = guesses_left - 2
                        else :
                            guesses_left -= 1
                        available_letters = get_available_letters(letters_guessed)
                        print("You have", guesses_left, "guesses left")
                        print("Available letters ", available_letters)
                        check2 = False
                        break
            if check2 :
                print ("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                print ("----------------------")
                guesses_left = guesses_left - 1
                available_letters = get_available_letters(letters_guessed)
                print("You have", guesses_left, "guesses left")
                print("Available letters ", available_letters)
        if is_word_guessed(secret_word, letters_guessed) :
            print ("Congratulations, you won!")
            score += 6
            print ("Your total score for this game is: ", score)
            break
        elif guesses_left == 0 :
            print ("Sorry, you ran out of guesses. The word was", secret_word)
            break

    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    other_word_len = len(other_word)
    my_word = my_word[0:len(my_word):2]
    my_word_len = len(my_word)
    check = 0
    
    if other_word_len == my_word_len:
        for i in range(other_word_len):
            if my_word[i] == other_word[i] or my_word[i] == "_":
                check += 1
        if check == other_word_len:
            return True
        else:
            return False
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for word in wordlist:
        check = match_with_gaps(my_word, word)
        if check:
            possible_matches.append(word)
    if possible_matches == []:
        return "No matches found"
    else:
        return possible_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

guesses = set()

def get_guess():
    while True:
        guess = raw_input("Guess a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("You must guess a single letter")
            continue

        normalised_guess = guess.upper()

        if normalised_guess in guesses:
            print("You already made that guess")
            continue

        guesses.add(normalised_guess)
        return normalised_guess


while True:
    guess = get_guess()
    print "you guessed: ", guess


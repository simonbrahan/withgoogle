answer = "FUZZY"
max_incorrect_guesses = 8
num_incorrect_guesses = 0
guesses = set()

def get_guess():
    while True:
        guess = raw_input("Guess a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("You must guess a single letter")
            continue

        normalised_guess = guess.upper()

        return normalised_guess


def get_hint():
    output = ""

    for char in answer:
        if char in guesses:
            output += char
        else:
            output += "-"

    return output


while True:
    print "Word looks like %s" % (get_hint(), )

    if "-" not in get_hint():
        print "You win"
        break

    guess = get_guess()
    print "you guessed: %s" % (guess, )

    if guess not in answer:
        num_incorrect_guesses += 1
        print "Wrong guess"

        if num_incorrect_guesses >= max_incorrect_guesses:
            print "You have lost"
            break
        else:
            print "You have %d guesses remaining" % (max_incorrect_guesses - num_incorrect_guesses)
            continue

    if guess in guesses:
        print("You already made that guess")
        continue

    guesses.add(guess)

    print "Good guess"



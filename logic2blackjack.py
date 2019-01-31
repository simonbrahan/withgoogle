def blackjack(a, b):
    if a > 21 and b > 21:
        return 0

    if a > 21:
        return b

    if b > 21:
        return a

    if a > b:
        return a
    else:
        return b


print blackjack(19, 21), "Should be", 21
print blackjack(21, 19), "Should be", 21
print blackjack(19, 22), "Should be", 19

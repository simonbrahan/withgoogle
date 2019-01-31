def string_splosion(input):
    if len(input) == 0:
        return ''

    return string_splosion(input[:-1]) + input


print string_splosion('Code')
print string_splosion('abc')
print string_splosion('ab')

def no_repeated_letters(word_1):
    lettersCount = {}
    for n in word_1:
        if n not in lettersCount:
            lettersCount[n] = 1
        else:
            lettersCount[n] += 1

    return max(lettersCount, key=lettersCount.get)

str=raw_input()
print no_repeated_letters(str)

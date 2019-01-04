def no_repeated_letters(word_1):
    lettersCount = {}
    for i in word_1:
        if i not in lettersCount:
            lettersCount[i] = 1
        else:
            lettersCount[i] += 1

    return max(lettersCount, key=lettersCount.get)

str=raw_input()
print no_repeated_letters(str)

"""words will be in dict format
    {letter: (blank, yellow, green)}"""


def filtered_words(words, guess):
    out = []
    for word in words:
        for i, (ltr, score) in enumerate(guess.items()):
            if score == "blank" and ltr in word:
                break
            elif score == "green" and word[i] != ltr:
                break
            elif score == "yellow" and (word[i] == ltr or ltr not in word):
                break
        else:
            out.append(word)
    return out

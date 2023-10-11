"""words will be in dict format
    {letter: (blank, yellow, green)}
"""


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


def score_guess(guess, potential_answer):
    out = {}
    for i, ltr in enumerate(guess):
        if ltr == potential_answer[i]:
            out[ltr] = "green"
        elif ltr in potential_answer:
            out[ltr] = "yellow"
        else:
            out[ltr] = "blank"
    return out

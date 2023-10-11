"""words will be in dict format
    {letter: (blank, yellow, green)}
    can't use dict because words with repeat letters will break
    teeth => {'t':blank, e:green}"""
from enum import Enum


class Score(Enum):
    Blank = 0
    Yellow = 1
    Green = 2


def filtered_words(words, guess, guess_score):
    out = []
    for word in words:
        for i, (ltr, score) in enumerate(zip(guess, guess_score)):
            if score == Score.Blank and ltr in word:
                break
            elif score == Score.Green and word[i] != ltr:
                break
            elif score == Score.Yellow and (word[i] == ltr or ltr not in word):
                break
        else:
            out.append(word)
    return out


def score_guess(guess, potential_answer):
    out = []
    for i, ltr in enumerate(guess):
        if ltr == potential_answer[i]:
            out.append(Score.Green)
        elif ltr in potential_answer:
            out.append(Score.Yellow)
        else:
            out.append(Score.Blank)
    return tuple(out)

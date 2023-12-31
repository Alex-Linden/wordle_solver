"""words will be in dict format
    {letter: (blank, yellow, green)}
    can't use dict because words with repeat letters will break
    teeth => {'t':blank, e:green}"""
from enum import Enum
from collections import defaultdict
import statistics


class Score(Enum):
    Blank = 0
    Yellow = 1
    Green = 2


def filtered_words(words, guess, guess_score):
    """Takes:
    list of words[],
    a guess 'str',
    score for that guess (tuple -> (Score.Blank:0, Score.Green:2, ...))

    iterates over the list of words to find
    only words that match the score pattern

    returns potential answers[]"""
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
    """Takes 2 strs guess and potential answer

    iterates over both to score guess

    returns tuple of the score

    current limitation => words that have repeated letters either guess or answers
    will note score the same way the NY Times game scores"""
    out = []
    for i, ltr in enumerate(guess):
        if ltr == potential_answer[i]:
            out.append(Score.Green)
        elif ltr in potential_answer:
            out.append(Score.Yellow)
        else:
            out.append(Score.Blank)
    return tuple(out)


def rank_guess(guess, words):
    """takes a guess 'str' and list of words[]

    groups words based on how many words fit a certain score
   counts = {
    (green, blank, yellow) : 2,
    (blank, blank, blank) : 5,
    ...
    }

    returns num that represents the mean of the diff counts
    """
    counts = defaultdict(int)
    for potential_guess in words:
        score = score_guess(guess, potential_guess)
        counts[score] += 1

    # print(counts)

    return statistics.mean(counts.values())


def make_guess(potential_answers, all_words):
    """takes a list of potential answers as ['str',] and all words['str]

    uses rank guess to find the word that returns the lowest rank

    returns that word.

    note: current limitation is there is no way to tie break when multiple words
    have the same ranking
    """
    def _score(word):
        return rank_guess(word, potential_answers)

    return min(all_words, key=_score)


def score_to_tuple(score):
    """
    Takes in score ['g', 'b', 'y', ...]

    turns into tuple usable by other functions
    """
    out = []

    for guess in score:
        if guess == 'g':
            out.append(Score.Green)
        elif guess in 'y':
            out.append(Score.Yellow)
        else:
            out.append(Score.Blank)
    return tuple(out)


def suggest_next_guess(guess, score, all_words):
    """used to help a human come up with next guess"""

    tuple_score = score_to_tuple(score)
    potential_answers = filtered_words(all_words, guess, tuple_score)

    return make_guess(potential_answers, all_words)


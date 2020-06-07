## Derived from Pluralsight Course Unit Testing with Python
## by Emily Bache
import random

def roll(number_of_dice=5):
    """
    Roll the indicated number of six sided dice using a random number generator.

    Examples
    --------
    >>> random.seed(42)
    >>> roll(3)
    [1, 1, 6]
    >>> roll()
    [2, 2, 2, 3, 6]
    >>> roll()
    [1, 5, 6, 6, 6]
    >>> roll(10)
    [1, 1, 1, 1, 2, 2, 4, 5, 5, 5]
    
    """
    return sorted(random.choice((1,2,3,4,5,6)) for i in range(number_of_dice))

def small_straight(dice):
    """Score the given roll in the 'small straight' category.

    Examples:

    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0
    >>> small_straight({1,2,3,4,5})
    15
    >>> small_straight([1,2,5,4,3])
    15

    """
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    return 0

def chance(dice):
    """Score the given roll in the 'Chance' category.

    Examples
    --------

    >>> chance([5,5,5,5,5])
    25
    >>> chance([1,2,3,4,5])
    15

    """
    return sum(dice)

def four_of_a_kind(dice):
    """Score the given roll in the 'Four of a kind' category.

    Examples
    --------

    >>> four_of_a_kind([1,6,6,6,6])
    24
    >>> four_of_a_kind([1,1,6,6,6])
    0

    """
    counts = dice_counts(dice)
    for i in [6,5,4,3,2,1]:
        if counts[i] >= 4:
            return 4*i
    return 0

def dice_counts(dice):
    """Count up the number of dice with each value.

    >>> dice_counts([1,2,3,4,5])
    [0, 1, 1, 1, 1, 1, 0]
    >>> dice_counts([6,6,6,6,6])
    [0, 0, 0, 0, 0, 0, 5]
    >>> dice_counts([4,4,3,3,3])
    [0, 0, 0, 3, 2, 0, 0]

    """
    counts = [0, 0, 0, 0, 0, 0, 0]
    for num in dice:
        counts[num] += 1

    return counts

def score(dice, value):
    """Scores the given face value in the roll.

    Examples
    --------
    >>> score([3,3,3,1,2], 3)
    9
    >>> score([3,3,3,1,2], 2)
    2
    >>> score([3,3,3,1,2], 1)
    1

    """
    return dice_counts(dice)[value]*value

def ones(dice):
    """Scores the roll in the 'Ones' category.

    Examples
    --------
    >>> ones([2,3,4,5,6])
    0
    >>> ones([4,3,2,1,1])
    2

    """
    return score(dice, 1)

def twos(dice):
    """Scores the roll in the 'Twos' category.

    Examples
    --------
    >>> twos([2,3,4,5,6])
    2
    >>> twos([4,3,2,1,1])
    2

    """
    return score(dice, 2)

def threes(dice):
    """Scores the roll in the 'Threes' category.

    Examples
    --------
    >>> threes([2,3,4,5,6])
    3
    >>> threes([4,2,2,1,1])
    0

    """
    return score(dice, 3)

def fours(dice):
    """Scores the roll in the 'Fours' category.

    Examples
    --------
    >>> fours([2,3,2,5,6])
    0
    >>> fours([4,4,2,1,1])
    8

    """
    return score(dice, 4)

def fives(dice):
    """Scores the roll in the 'Fives' category.

    Examples
    --------
    >>> fives([5,5,1,2,3])
    10
    >>> fives([4,3,2,1,1])
    0

    """
    return score(dice, 5)

def sixes(dice):
    """Scores the roll in the 'Sixes' category.

    Examples
    --------
    >>> sixes([2,3,4,5,6])
    6
    >>> sixes([4,3,2,1,1])
    0

    """
    return score(dice, 6)

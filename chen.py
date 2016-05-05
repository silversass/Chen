from random import randint, shuffle
from math import ceil


ranks = "23456789TJQKA"
suits = "cdhs"
deck = [(j + i) for i in suits for j in ranks]
shuffle(deck)

# hand = [deck.pop(0) for _ in range(2)]
hand = raw_input('Enter the hand:').split()  # ["Ah", "2h"]
position = input('Enter position:') # randint(1, 6)


def chen():

    # Sort hand:
    if ranks.index(hand[0][0]) < ranks.index(hand[1][0]):
        hand[0], hand[1] = hand[1], hand[0]

    facePoints = {"A": 10, "K": 8, "Q": 7, "J": 6, "T": 5}

    a, b = hand[0], hand[1]

    # Score highest card
    if a[0] in facePoints:
        score = facePoints.get(a[0])
    else:
        score = int(a[0])/2.

    # Multiply pairs by 2 of one card's value
    if a[0] is b[0]:
        score *= 2
        if score < 5:
            score = 5

    # Add 2 if cards are suited
    if a[1] is b[1]:
        score += 2

    # Subtract points if there is a gap
    gap = ranks.index(a[0]) - ranks.index(b[0]) - 1
    gapPoints = {1: 1, 2: 2, 3: 4}
    if gap in gapPoints:
        score -= gapPoints.get(gap)
    elif gap >= 4:
        score -= 5

    # Straight bonus
    if (gap < 2) and (ranks.index(a[0]) < ranks.index("Q")) and (a[0] is not b[0]):
        score += 1

    return int(ceil(score))

# 6-handed table
def move_six(score):

    # Early position - SB BB UTG
    if position <= 3:
        if score >= 9:
            return 'raise'
        else:
            return 'fold'
    # Middle position - UTG+1
    elif position is 4:
        if score >= 8:
            return 'raise'
        else:
            return 'fold'
    # Late position - CO BTN
    else:
        if score >= 7:
            return 'raise'
        else:
            return 'fold'

# 9-handed table
def move_nine(score):

    if score >= 12:
        return 'raise/reraise'
    elif score >= 10:
        return 'raise'
    # Early position - SB BB UTG UTG+1 UTG+2
    elif position <= 4:
        if score >= 10:
            return 'raise'
        else:
            return 'fold'
    # Middle position - MP1 MP 2 MP 3
    elif position <= 7:
        if score >= 9:
            return 'raise'
        else:
            return 'fold'
    # Late position - CO BTN
    else:
        if score >= 7:
            return 'raise'
        else:
            return 'fold'

score = chen()
print "Hand: %s\nScore: %d\nPosition: %d" % (hand, score, position)
print "Move: %s" % move_nine(score)

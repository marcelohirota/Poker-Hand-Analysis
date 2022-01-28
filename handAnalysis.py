def poker(hands):
    # check the score given by the score function
    scores = [(i, score(hand)) for i, hand in enumerate(hands)]
    # Check both analysis, the hand with shorter lenght of dictionary will win
    winner = sorted(scores , key=lambda x:x[1])[-1][0]
    return hands[winner]
    
def score(hand):
    # Given a weigh for each value through the position of the string
    values = '23456789TJQKA'
    # Separating the value from the suit, and appending to a dictionary
    # Keys of the dictionary will be the values of the cards
    # Values of the dictionary will be how many of the same value
    rcounts = {values.find(r): ''.join(hand).count(r) for r, nsuit in hand}.items()
    # Evaluates if the hand has cards of the same value or not, and sorting it
    # by descending order
    score, values = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    # If the dictionary created has 5 keys and values (no card of the same values), it should be checked the suits of the cards
    if len(score) == 5:
        # check if the cards have the same suit
        if values[0:2] == (12, 3): 
            values = (3, 2, 1, 0, 1)
        # check the diference between the bigger number and smaller number, 
        # if there is a diference of only four numbers between them, 
        # the values are a sequence
        straight = values[0] - values[4] == 4 # same suit
        # check if is the top end of the sequence
        flush = len({suit for nsuit, suit in hand}) == 1 # same suit
        # assign a score depending on the hand
        score = ([(1,), (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
        
    return score, values
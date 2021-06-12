# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:06:38 2020

@author: chaby
"""

class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]
        
    def getValue(self):
        return int(self.points)

def drawCard(*cards, return_string=True):
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        if card.rank == '10':
            rank = card.rank
            space = '' 
        else:
            rank = card.rank[0]
            space = ' '
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    if return_string:
        return '\n'.join(result)
    else:
        return result


def drawHiddenCard(*cards):
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    cards_except_first = drawCard(*cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    return '\n'.join(lines)


# TEST CASES
#test_card_1 = Card('Diamonds', '4')
#test_card_2 = Card('Clubs', 'Ace')
#test_card_3 = Card('Spades', 'Jack')
#test_card_4 = Card('Hearts', '10')

#print(drawCard(test_card_1, test_card_2, test_card_3, test_card_4))
#print(drawHiddenCard(test_card_1))
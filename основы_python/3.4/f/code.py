from itertools import product


cards = list(range(2, 11)) + ['валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())

for card, suit in (product(cards, suits)):
    print(card, suit)

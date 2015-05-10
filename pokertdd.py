import random

suit_type = {
    'C' : "Club",
    'D' : "Diamond",
    'H' : "Heart",
    'S' : "Spade",
    }
card_value = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14,
    }

card1 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card2 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card3 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card4 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card5 = [random.choice(suit_type.values()), random.choice(card_value.values())]

card6 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card7 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card8 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card9 = [random.choice(suit_type.values()), random.choice(card_value.values())]
card10 = [random.choice(suit_type.values()), random.choice(card_value.values())]

white_hands = [card1,card2,card3,card4,card5]
black_hands = [card6,card7,card8,card9,card10]

'''
if card1[0]==card2[0]
    white_hands_score = "blank"
'''

# determine each hand values via rules for example flash or stright or fullhouse then give that a hand a score in a thousand range (so it will not be beat by hand with no combo)

# In case both hands have the same combo the 4th digit would be the same (or no combo)

# the individual cards values are then sum together to determine who is higher

# in case both hands also have same cards values  - the hand with higher suit for highest card values win

print "White Hand is" ,white_hands
print "Black Hand is" ,black_hands

from pokertdd import Poker, Cards
from unittest import TestCase

class TestCardsSuite(TestCase):
    def cardsSizeIsFiftyTwo(self):
        poker = Poker()
        self.assertEqual(52,poker.first())
    def cardHasSuite(self):
        cards = Cards()
        self.assertEqual("",cards.suit_type())

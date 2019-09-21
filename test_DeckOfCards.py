#Import the external package from previous commit deck_of_cards,
#this is an example for implementing testing in python,
#asserting, doctests and unittest


from deck_of_cards import Card
from deck_of_cards import Deck
import unittest

class CradsTest(unittest.TestCase) :
    
    def setUp(self):
        self.card = Card("Hearts","A")

    def test_init(self):
        """cards should have a suit and a value """
        self.assertEqual(self.card.suit, "Hearts")
        self.asserEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of form 'value of suit' """
        self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase) :
    
    def setUp(self) :
        self.deck = Deck()

    def test_init(self) :
        """decks should have a cards attribute , which is a list with 52 cards """
        self.assertTrue(instance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self) :
        """repr should return a string of the form 'Deck of 52 cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count should return a count of numbers of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """deal should deal the number of cards specified if possible"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_insufficient_cards(self) :
        """deal sgould deal the number of cards left in the deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards),52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self) :
        """deal should throw a valueError if the deck is empty"""
        self.deck._deal(self.deck.countt())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        card = self.deck.cards[-1]
        dealt_card = self.deck._deal_card()
        self.aseertEqual(card,dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self) :
        """deal hand should deal the number of cards passed into the hand"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count() ,32)

    def test_shuffle_full_deck(self) :
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(crads, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """shuffle should throw a value error if the deck is empty"""
        self.deck._deal(1)
        with self.assertRaoses(ValueError):
            self.deck.shuffle()


if __name__ == '__main__' :
    unittest.main()

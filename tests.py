import unittest
from score_game import generate_game, get_score


class TestGetScore(unittest.TestCase):
    def test_get_score_validation(self):

        stamps = generate_game()
        self.assertRaises(TypeError, get_score, stamps, ['111', 23132])

    def test_get_score_validation_stamps(self):
        stamps = 'i56776i76'
        self.assertRaises(TypeError, get_score, stamps, 111)

    def test_get_score_required_arguments(self):
        stamps = generate_game()
        self.assertRaises(TypeError, get_score, stamps)

    def test_get_score_empty_stamps(self):
        stamps = []
        self.assertRaises(ValueError, get_score, stamps, 111)

    def test_get_score_negative_offset(self):
        stamps = generate_game()
        self.assertRaises(ValueError, get_score, stamps, -111)




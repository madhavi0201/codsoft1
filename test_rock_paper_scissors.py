import unittest
from rock_paper_scissors import (
    determine_winner,
    parse_user_choice,
    get_computer_choice,
    ROCK,
    PAPER,
    SCISSORS
)

class TestRockPaperScissors(unittest.TestCase):
    def test_determine_winner(self):
        """Test all win, loss, and tie combinations for determine_winner."""
        # User wins
        self.assertEqual(determine_winner(ROCK, SCISSORS), 'user')
        self.assertEqual(determine_winner(SCISSORS, PAPER), 'user')
        self.assertEqual(determine_winner(PAPER, ROCK), 'user')
        
        # Computer wins
        self.assertEqual(determine_winner(SCISSORS, ROCK), 'computer')
        self.assertEqual(determine_winner(PAPER, SCISSORS), 'computer')
        self.assertEqual(determine_winner(ROCK, PAPER), 'computer')
        
        # Ties
        self.assertEqual(determine_winner(ROCK, ROCK), 'tie')
        self.assertEqual(determine_winner(PAPER, PAPER), 'tie')
        self.assertEqual(determine_winner(SCISSORS, SCISSORS), 'tie')

    def test_parse_user_choice(self):
        """Test parsing and normalization of user input."""
        # Rock variations
        self.assertEqual(parse_user_choice("r"), ROCK)
        self.assertEqual(parse_user_choice("R"), ROCK)
        self.assertEqual(parse_user_choice("rock"), ROCK)
        self.assertEqual(parse_user_choice("  ROCK  "), ROCK)
        
        # Paper variations
        self.assertEqual(parse_user_choice("p"), PAPER)
        self.assertEqual(parse_user_choice("P"), PAPER)
        self.assertEqual(parse_user_choice("paper"), PAPER)
        self.assertEqual(parse_user_choice("  Paper  "), PAPER)
        
        # Scissors variations
        self.assertEqual(parse_user_choice("s"), SCISSORS)
        self.assertEqual(parse_user_choice("S"), SCISSORS)
        self.assertEqual(parse_user_choice("scissors"), SCISSORS)
        self.assertEqual(parse_user_choice("  SCISSORS  "), SCISSORS)
        
        # Invalid inputs
        self.assertIsNone(parse_user_choice("invalid"))
        self.assertIsNone(parse_user_choice("1"))
        self.assertIsNone(parse_user_choice(""))
        self.assertIsNone(parse_user_choice("   "))

    def test_get_computer_choice(self):
        """Test that computer choice is valid and random."""
        choices = set()
        for _ in range(100):
            choice = get_computer_choice()
            self.assertIn(choice, [ROCK, PAPER, SCISSORS])
            choices.add(choice)
        
        # In 100 runs, we should see all three choices selected at least once
        self.assertEqual(choices, {ROCK, PAPER, SCISSORS})

if __name__ == '__main__':
    unittest.main()

import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        """Test that the generated password has the requested length."""
        for length in [1, 5, 10, 20, 100]:
            password = generate_password(length)
            self.assertEqual(len(password), length)

    def test_single_character_type_upper(self):
        """Test that if only uppercase is selected, all characters are uppercase."""
        password = generate_password(10, use_upper=True, use_lower=False, use_digits=False, use_special=False)
        self.assertEqual(len(password), 10)
        for char in password:
            self.assertIn(char, string.ascii_uppercase)

    def test_single_character_type_lower(self):
        """Test that if only lowercase is selected, all characters are lowercase."""
        password = generate_password(10, use_upper=False, use_lower=True, use_digits=False, use_special=False)
        self.assertEqual(len(password), 10)
        for char in password:
            self.assertIn(char, string.ascii_lowercase)

    def test_single_character_type_digits(self):
        """Test that if only digits are selected, all characters are digits."""
        password = generate_password(10, use_upper=False, use_lower=False, use_digits=True, use_special=False)
        self.assertEqual(len(password), 10)
        for char in password:
            self.assertIn(char, string.digits)

    def test_single_character_type_special(self):
        """Test that if only special characters are selected, all characters are special."""
        password = generate_password(10, use_upper=False, use_lower=False, use_digits=False, use_special=True)
        self.assertEqual(len(password), 10)
        for char in password:
            self.assertIn(char, string.punctuation)

    def test_complexity_guarantee(self):
        """Test that when all character types are enabled, at least one of each is included (for length >= 4)."""
        # Run multiple times to ensure robustness against random variation
        for _ in range(100):
            password = generate_password(12, use_upper=True, use_lower=True, use_digits=True, use_special=True)
            
            has_upper = any(c in string.ascii_uppercase for c in password)
            has_lower = any(c in string.ascii_lowercase for c in password)
            has_digits = any(c in string.digits for c in password)
            has_special = any(c in string.punctuation for c in password)
            
            self.assertTrue(has_upper, f"Password '{password}' missing uppercase character")
            self.assertTrue(has_lower, f"Password '{password}' missing lowercase character")
            self.assertTrue(has_digits, f"Password '{password}' missing digit character")
            self.assertTrue(has_special, f"Password '{password}' missing special character")

    def test_invalid_arguments(self):
        """Test that invalid inputs raise ValueError."""
        # Length less than 1
        with self.assertRaises(ValueError):
            generate_password(0)
        with self.assertRaises(ValueError):
            generate_password(-5)
            
        # No character types selected
        with self.assertRaises(ValueError):
            generate_password(10, use_upper=False, use_lower=False, use_digits=False, use_special=False)

if __name__ == '__main__':
    unittest.main()

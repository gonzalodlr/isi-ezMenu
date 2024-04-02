import os
import unittest
from unittest.mock import patch, MagicMock

from ..routes.pdf_route import generar_pdf, text_wrap

class TestPDFRoute(unittest.TestCase):
    def test_generar_pdf(self):
        # Create a list of Food objects
        food_list = [
            MagicMock(
                name="Food 1",
                thumbnail_url="https://example.com/food1.jpg",
                description="Description 1",
                price={"portion": 9.99}
            ),
            MagicMock(
                name="Food 2",
                thumbnail_url="https://example.com/food2.jpg",
                description="Description 2",
                price={"portion": 14.99}
            )
        ]

        # Call the function with the food list
        generar_pdf(food_list)

        # Assert that the PDF file is generated
        self.assertTrue(os.path.exists('/home/gonzalo/Desktop/isi-ezMenu/backend/assets/menu.pdf'))

    def test_text_wrap(self):
        # Test with a long text that needs to be wrapped
        long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        expected_lines = [
            "Lorem ipsum dolor sit amet,",
            "consectetur adipiscing elit,",
            "sed do eiusmod tempor",
            "incididunt ut labore et",
            "dolore magna aliqua."
        ]

        # Call the function with the long text
        result = text_wrap(long_text)

        # Assert that the function returns the expected lines
        self.assertEqual(result, expected_lines)

        # Test with a short text that doesn't need to be wrapped
        short_text = "Short text"

        # Call the function with the short text
        result = text_wrap(short_text)

        # Assert that the function returns a list with the short text
        self.assertEqual(result, [short_text])

if __name__ == '__main__':
    unittest.main()
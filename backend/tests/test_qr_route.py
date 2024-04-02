import os
import unittest
from unittest.mock import patch, MagicMock

from ..routes.qr_route import image_to_base64, generate_qr

class TestQrRoute(unittest.TestCase):
    def test_image_to_base64(self):
        # Create a sample image file
        image_path = "sample_image.png"
        with open(image_path, "wb") as img_file:
            img_file.write(b"sample image data")

        # Call the function with the sample image file
        result = image_to_base64(image_path)

        # Assert that the function returns the expected base64 string
        self.assertEqual(result, "c2FtcGxlIGltYWdlIGRhdGE=")

        # Clean up the sample image file
        os.remove(image_path)

    @patch('requests.get')
    @patch('builtins.open', MagicMock())
    def test_generate_qr(self, mock_requests_get):
        # Mock the requests.get function to return a successful response
        mock_response = MagicMock(status_code=200, content=b"qr image data")
        mock_requests_get.return_value = mock_response

        # Call the generate_qr function with a sample URL
        with patch('os.remove', MagicMock()):
            result = generate_qr()

        # Assert that the function returns a JSON response with the expected status and link
        self.assertEqual(result, {"status": "success", "link": "backend/assets/qr_image.jpg"})

        # Assert that the requests.get function was called with the correct arguments
        mock_requests_get.assert_called_once_with(
            "https://qr-code-generator20.p.rapidapi.com/generatebasicimage",
            headers={
                "X-RapidAPI-Key": os.getenv("API_KEY"),
                "X-RapidAPI-Host": "qr-code-generator20.p.rapidapi.com"
            },
            params={
                "data": None,
                "size": "500"
            }
        )

if __name__ == '__main__':
    unittest.main()
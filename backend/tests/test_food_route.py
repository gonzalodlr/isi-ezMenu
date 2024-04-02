import os
import unittest
from unittest.mock import patch, MagicMock

from ..routes.food_route import exits_json, search_json_data, serialize_food, search_foods

class TestFoodRoute(unittest.TestCase):
    def test_exits_json_existing_file(self):
        # Create a temporary directory and file
        temp_dir = "temp"
        temp_file = "search.json"
        os.makedirs(temp_dir, exist_ok=True)
        open(os.path.join(temp_dir, temp_file), 'a').close()

        # Call the function with the temporary file name
        result = exits_json(temp_file)

        # Assert that the function returns True
        self.assertTrue(result)

        # Clean up the temporary directory and file
        os.remove(os.path.join(temp_dir, temp_file))
        os.rmdir(temp_dir)

    def test_exits_json_non_existing_file(self):
        # Call the function with a non-existing file name
        result = exits_json("non_existing_file")

        # Assert that the function returns False
        self.assertFalse(result)

    def test_exits_json_non_existing_directory(self):
        # Call the function with a non-existing directory name
        result = exits_json("non_existing_directory/search")

        # Assert that the function returns False
        self.assertFalse(result)

    def test_search_json_data_existing_file(self):
        # Create a temporary directory and file
        temp_dir = "temp"
        temp_file = "search.json"
        os.makedirs(temp_dir, exist_ok=True)
        open(os.path.join(temp_dir, temp_file), 'w').close()

        # Call the function with the temporary file name
        result = search_json_data(temp_file)

        # Assert that the function returns a list of Food objects
        self.assertIsInstance(result, list)

        # Clean up the temporary directory and file
        os.remove(os.path.join(temp_dir, temp_file))
        os.rmdir(temp_dir)

    def test_search_json_data_non_existing_file(self):
        # Call the function with a non-existing file name
        result = search_json_data("non_existing_file")

        # Assert that the function returns False
        self.assertFalse(result)

    def test_search_json_data_non_existing_directory(self):
        # Call the function with a non-existing directory name
        result = search_json_data("non_existing_directory/search")

        # Assert that the function returns False
        self.assertFalse(result)

    def test_serialize_food(self):
        # Create a list of Food objects
        food_list = [
            MagicMock(get_name=lambda: "Food 1", get_id=lambda: 1, get_description=lambda: "Description 1"),
            MagicMock(get_name=lambda: "Food 2", get_id=lambda: 2, get_description=lambda: "Description 2")
        ]

        # Call the function with the food list
        result = serialize_food(food_list)

        # Assert that the function returns a serialized JSON string
        self.assertIsInstance(result, str)
        self.assertEqual(result, '[{"Name": "Food 1", "ID": 1, "Description": "Description 1"}, {"Name": "Food 2", "ID": 2, "Description": "Description 2"}]')

    @patch('requests.get')
    @patch('json.dump')
    def test_search_foods_existing_json(self, mock_json_dump, mock_requests_get):
        # Mock the requests.get function to return a successful response
        mock_response = MagicMock(status_code=200, json=lambda: {"results": []})
        mock_requests_get.return_value = mock_response

        # Call the search_foods function with an existing JSON file
        with patch('os.path.exists', return_value=True):
            with patch('os.path.isdir', return_value=True):
                with patch('builtins.open', MagicMock()):
                    result = search_foods()

        # Assert that the function returns a serialized JSON string
        self.assertIsInstance(result, str)

        # Assert that the requests.get function was called with the correct arguments
        mock_requests_get.assert_not_called()

        # Assert that the json.dump function was called with the correct arguments
        mock_json_dump.assert_not_called()

    @patch('requests.get')
    @patch('json.dump')
    def test_search_foods_non_existing_json(self, mock_json_dump, mock_requests_get):
        # Mock the requests.get function to return a successful response
        mock_response = MagicMock(status_code=200, json=lambda: {"results": []})
        mock_requests_get.return_value = mock_response

        # Call the search_foods function with a non-existing JSON file
        with patch('os.path.exists', return_value=False):
            with patch('os.path.isdir', return_value=True):
                with patch('builtins.open', MagicMock()):
                    result = search_foods()

        # Assert that the function returns a serialized JSON string
        self.assertIsInstance(result, str)

        # Assert that the requests.get function was called with the correct arguments
        mock_requests_get.assert_called_once_with(
            "https://tasty.p.rapidapi.com/recipes/list",
            headers={
                "X-RapidAPI-Key": os.getenv("API_KEY"),
                "X-RapidAPI-Host": "tasty.p.rapidapi.com"
            },
            params={
                "from": "0",
                "size": "9",
                "q": "searchTerm"
            }
        )

        # Assert that the json.dump function was called with the correct arguments
        mock_json_dump.assert_called_once()

if __name__ == '__main__':
    unittest.main()
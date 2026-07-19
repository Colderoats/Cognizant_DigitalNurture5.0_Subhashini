import unittest
from unittest.mock import patch, MagicMock
from app import fetch_user, fetch_post


class TestApp(unittest.TestCase):

    @patch("app.get_user")
    def test_database_call(self, mock_get_user):

        mock_get_user.return_value = {
            "id": 1,
            "name": "Alice"
        }

        result = fetch_user(1)

        self.assertEqual(result["name"], "Alice")
        mock_get_user.assert_called_once_with(1)

    @patch("app.requests.get")
    def test_http_request(self, mock_get):

        mock_response = MagicMock()

        mock_response.json.return_value = {
            "id": 1,
            "title": "Mock Post"
        }

        mock_get.return_value = mock_response

        result = fetch_post(1)

        self.assertEqual(result["title"], "Mock Post")
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
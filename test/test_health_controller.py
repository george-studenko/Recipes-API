from test.base_test_case import BaseTestCase
import unittest


class HealthTestCase(BaseTestCase):

    def test_get_health_OK_response(self):
        # Arrange
        expected_status_code = 200

        # Act
        result = self.client.get('/health/')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    unittest.main()

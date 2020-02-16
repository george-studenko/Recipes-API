from backend.test.base_test_case import BaseTestCase


class HealthTestCase(BaseTestCase):

    def test_get_health_OK_response(self):
        # Arrange
        expected_status_code = 200

        # Act
        result = self.client.get('/health/')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)


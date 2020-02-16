import json
from backend.test.base_test_case import BaseTestCase
from backend.main.services.category_service import post_category


class CategoryTestCase(BaseTestCase):

    def test_get_categories_OK_response(self):
        # Arrange
        expected_status_code = 200

        # Act
        result = self.client.get('/category/')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_get_categories_name_is_category_1(self):
        # Arrange
        expected_value = 'Category 1'
        post_category('Category 1', 'Category One', 'category-1')

        # Act
        result = self.client.get('/category/')
        content = json.loads(result.data)
        actual_value = content['categories'][0]['name']

        # Assert
        self.assertEqual(actual_value, expected_value)
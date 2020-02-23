import json
from backend.test.base_test_case import BaseTestCase
from backend.main.services.category_service import post_category
from backend.main.models.category import Category


class CategoryTestCase(BaseTestCase):

    def post_test_category(self):
        test_category = dict(category=dict(name='Category 1',
                                  description='category description',
                                  slug='category-slug'))

        result = self.client.post('/category/',
                                  data= json.dumps(test_category),
                                  content_type = 'application/json')

        return result

    def post_bad_test_category(self):
        test_category = dict(category=dict(description='category description',
                                  slug='category-slug'))

        result = self.client.post('/category/',
                                  data= json.dumps(test_category),
                                  content_type = 'application/json')

        return result

    def test_get_categories_status_code_is_200(self):
        # Arrange
        expected_status_code = 200

        # Act
        result = self.client.get('/category/')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_get_correct_category_name(self):
        # Arrange
        expected_value = 'Category 1'
        self.post_test_category()

        # Act
        result = self.client.get('/category/')
        content = json.loads(result.data)
        actual_value = content[0]['name']

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_post_category_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_category()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    # def test_post_bad_category_status_code_is_422(self):
    #     # Arrange
    #     expected_status_code = 422
    #
    #     # Act
    #     result = self.post_bad_test_category()
    #
    #     actual_status_code = result.status_code
    #
    #     # Assert
    #     self.assertEqual(actual_status_code, expected_status_code)


    def test_post_category_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_category()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)
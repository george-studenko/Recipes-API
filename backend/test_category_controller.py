import json
from backend.base_test_case import BaseTestCase


class CategoryTestCase(BaseTestCase):

    def post_test_category(self, name = 'Category 1'):
        test_category = dict(category=dict(name=name,
                                  description='category description',
                                  slug='category-slug'))

        result = self.client.post('/category',
                                  data= json.dumps(test_category),
                                  content_type = 'application/json')

        return result

    def post_bad_test_category(self):
        test_category = dict(category=dict(description='category description',
                                  slug='category-slug'))

        result = self.client.post('/category',
                                  data= json.dumps(test_category),
                                  content_type = 'application/json')

        return result

    def test_get_categories_status_code_is_200(self):
        # Arrange
        expected_status_code = 200

        # Act
        result = self.client.get('/category')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_get_correct_category_name(self):
        # Arrange
        expected_value = 'Category 1'
        self.post_test_category()

        # Act
        result = self.client.get('/category')
        content = json.loads(result.data)
        actual_value = content[0]['name']

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_get_category_by_id_returns_correct_category(self):
        # Arrange
        expected_value = 'Category 1'
        self.post_test_category()
        self.post_test_category(name = 'Another Category')

        # Act
        result = self.client.get('/category/1')
        content = json.loads(result.data)
        actual_value = content['name']

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_get_categories_status_code_is_404_when_not_found(self):
        # Arrange
        expected_status_code = 404

        # Act
        result = self.client.get('/category/2')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_get_category_by_id_returns_only_one_category(self):
        # Arrange
        # When we have only one item json.loads will return a dictionary
        # while if we have multiple items it will return a list of dictionaries
        # so we assume that if the type is a dict then it is a single category
        expected_type = type({})
        for i in range(3):
            self.post_test_category()

        # Act
        result = self.client.get('/category/1')
        actual_type = type(json.loads(result.data))
        self.assertEqual(expected_type, actual_type)

    def test_get_category_list_gets_more_than_one_category(self):
        # Arrange
        expected_category_count = 3
        for i in range(expected_category_count):
            self.post_test_category()

        # Act
        result = self.client.get('/category')
        actual_category_count = len(json.loads(result.data))

        self.assertEqual(expected_category_count,actual_category_count)

    def test_post_category_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_category()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_post_bad_category_status_code_is_422(self):
        # Arrange
        expected_status_code = 422

        # Act
        result = self.post_bad_test_category()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_post_category_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_category()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_delete_category(self):
        # Arrange
        expected_status_code = 404
        self.post_test_category()

        # Act
        self.client.delete('/category/1')

        result = self.client.get('/category/1')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_delete_category_status_code_is_200_when_deleted(self):
        # Arrange
        expected_status_code = 200
        self.post_test_category()

        # Act
        result = self.client.delete('/category/1')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_delete_category_status_code_is_404_when_not_found(self):
        # Arrange
        expected_status_code = 404
        self.post_test_category()

        # Act
        result = self.client.delete('/category/182')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_patch_category_name(self):
        # Arrange
        expected_category_name = 'Category Name Patched'
        self.post_test_category()

        # Act
        category = dict(category=dict(name=expected_category_name))

        self.client.patch('/category/1',
                          data= json.dumps(category),
                          content_type = 'application/json')

        result = self.client.get('/category/1')

        content = json.loads(result.data)
        actual_category_name = content['name']

        # Assert
        self.assertEqual(actual_category_name, expected_category_name)

    def test_patch_category_name_keeps_description_without_changes(self):
        # Arrange
        new_category_name = 'Category Name Patched'
        expected_description = 'category description'
        self.post_test_category()

        # Act
        category = dict(category=dict(name=new_category_name))

        self.client.patch('/category/1',
                          data= json.dumps(category),
                          content_type = 'application/json')

        result = self.client.get('/category/1')

        content = json.loads(result.data)
        actual_category_description = content['description']

        # Assert
        self.assertEqual(actual_category_description, expected_description)
import json
from base_test_case import BaseTestCase
import unittest


class RecipeTestCase(BaseTestCase):

    def post_test_recipe(self, title = 'Recipe 1'):
        test_category = dict(category=dict(name='Category 1',
                                           description='category description',
                                           slug='category-slug'))
        self.client.post('/category',
                                  data=json.dumps(test_category),
                                  content_type='application/json')

        test_user = dict(user=dict(username='username1'))
        self.client.post('/user',
                         data=json.dumps(test_user),
                         content_type='application/json')

        test_recipe = dict(recipe=dict(title=title,
                                  description='recipe description',
                                  user_id='1',
                                  url='url',
                                  category_id='1'
                                       ))

        result = self.client.post('/recipe',
                                  data= json.dumps(test_recipe),
                                  content_type = 'application/json')

        return result

    def post_bad_test_recipe(self):
        test_recipe = dict(recipe=dict(description='recipe description',
                                  url='url'))

        result = self.client.post('/recipe',
                                  data= json.dumps(test_recipe),
                                  content_type = 'application/json')

        return result

    def test_get_recipe_status_code_is_200_when_recipes_exist(self):
        # Arrange
        expected_status_code = 200
        self.post_test_recipe()

        # Act
        result = self.client.get('/recipe')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_get_recipe_status_code_is_404_when_no_recipes_exist(self):
        # Arrange
        expected_status_code = 404

        # Act
        result = self.client.get('/recipe')
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_post_recipe_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_recipe()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_post_bad_recipe_status_code_is_422(self):
        # Arrange
        expected_status_code = 422

        # Act
        result = self.post_bad_test_recipe()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    unittest.main()
import json
from base_test_case import BaseTestCase
import unittest


class RecipeTestCase(BaseTestCase):

    def post_test_recipe(self, token, title='Recipe 1'):

        test_category = dict(category=dict(name='Category 1',
                                           description='category description',
                                           slug='category-slug'))
        self.client.post('/category',
                         data=json.dumps(test_category),
                         content_type='application/json',
                         headers=token)

        test_user = dict(user=dict(username='username1'))
        self.client.post('/user',
                         data=json.dumps(test_user),
                         content_type='application/json',
                         headers=token)

        test_recipe = dict(recipe=dict(title=title,
                                       description='recipe description',
                                       user_id='1',
                                       url='url',
                                       category_id='1'
                                       ))

        result = self.client.post('/recipe',
                                  data=json.dumps(test_recipe),
                                  content_type='application/json',
                                  headers=token)

        return result

    def post_bad_test_recipe(self):
        test_recipe = dict(recipe=dict(description='recipe description',
                                       url='url'))

        result = self.client.post('/recipe',
                                  data=json.dumps(test_recipe),
                                  content_type='application/json',
                                  headers=self.chef_bearer_token)

        return result

    def test_get_recipe_status_code_is_200_when_recipes_exist(self):
        # Arrange
        expected_status_code = 200
        self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        result = self.client.get('/recipe', headers=self.cook_bearer_token)
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_get_recipe_status_code_is_404_when_no_recipes_exist(self):
        # Arrange
        expected_status_code = 404

        # Act
        result = self.client.get('/recipe', headers=self.cook_bearer_token)
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_post_recipe_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_recipe(token=self.chef_bearer_token)

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

    def test_get_recipe_by_id_returns_correct_recipe(self):
        # Arrange
        expected_value = 'Recipe 1'
        self.post_test_recipe(token=self.chef_bearer_token)
        self.post_test_recipe(
            token=self.chef_bearer_token,
            title='Another Recipe 2')

        # Act
        result = self.client.get('/recipe/1', headers=self.cook_bearer_token)
        content = json.loads(result.data)
        actual_value = content['recipe']['title']

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_get_categories_status_code_is_404_when_not_found(self):
        # Arrange
        expected_status_code = 404

        # Act
        result = self.client.get('/recipe/2', headers=self.cook_bearer_token)
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
            self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        result = self.client.get('/recipe/1', headers=self.cook_bearer_token)
        actual_type = type(json.loads(result.data))
        self.assertEqual(expected_type, actual_type)

    def test_delete_category(self):
        # Arrange
        expected_status_code = 404
        self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        self.client.delete('/recipe/1', headers=self.chef_bearer_token)

        result = self.client.get('/recipe/1', headers=self.cook_bearer_token)
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_delete_category_status_code_is_200_when_deleted(self):
        # Arrange
        expected_status_code = 200
        self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        result = self.client.delete(
            '/recipe/1', headers=self.chef_bearer_token)
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_delete_recipe_status_code_is_404_when_not_found(self):
        # Arrange
        expected_status_code = 404
        self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        result = self.client.delete(
            '/recipe/182', headers=self.chef_bearer_token)
        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_patch_recipe_name(self):
        # Arrange
        expected_category_name = 'Category Name Patched'
        self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        category = dict(category=dict(name=expected_category_name))

        result = self.client.patch('/category/1',
                                   data=json.dumps(category),
                                   content_type='application/json',
                                   headers=self.chef_bearer_token)

        content = json.loads(result.data)
        actual_category_name = content['category']['name']

        # Assert
        self.assertEqual(actual_category_name, expected_category_name)

    def test_patch_recipe_name_keeps_description_without_changes(self):
        # Arrange
        new_recipe_name = 'Recipe title Patched'
        expected_description = 'recipe description'
        self.post_test_recipe(token=self.chef_bearer_token)

        # Act
        category = dict(recipe=dict(title=new_recipe_name))

        result = self.client.patch('/recipe/1',
                                   data=json.dumps(category),
                                   content_type='application/json',
                                   headers=self.chef_bearer_token)

        content = json.loads(result.data)
        actual_recipe_description = content['recipe']['description']

        # Assert
        self.assertEqual(actual_recipe_description, expected_description)

    def test_post_recipe_as_cook_status_code_is_401(self):
        # Arrange
        expected_status_code = 401

        # Act
        result = self.post_test_recipe(token=self.cook_bearer_token)

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    unittest.main()

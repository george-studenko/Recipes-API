import json
from base_test_case import BaseTestCase
import unittest


class UserTestCase(BaseTestCase):

    def post_test_user(self):
        test_user = dict(user=dict(username='username1'))
        result =self.client.post('/user',
                         data=json.dumps(test_user),
                         content_type='application/json',
                         headers = self.chef_bearer_token)
        return result

    def post_bad_user(self):
        test_user = dict(user=dict(some_key='missing username'))
        result =self.client.post('/user',
                         data=json.dumps(test_user),
                         content_type='application/json',
                         headers = self.chef_bearer_token)
        return result


    def test_post_user_as_cook_status_code_is_401(self):
        # Arrange
        expected_status_code = 401
        test_user = dict(user=dict(username='username1'))

        # Act
        result = self.client.post('/user',
                                  data=json.dumps(test_user),
                                  content_type='application/json',
                                  headers=self.cook_bearer_token)

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)


    def test_post_user_status_code_is_201(self):
        # Arrange
        expected_status_code = 201

        # Act
        result = self.post_test_user()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

    def test_post_bad_user_status_code_is_422(self):
        # Arrange
        expected_status_code = 422

        # Act
        result = self.post_bad_user()

        actual_status_code = result.status_code

        # Assert
        self.assertEqual(actual_status_code, expected_status_code)

import unittest
from credentials import Credentials
from user import Users

#first test

class TestUsers(unittest.TestCase):
    """
    Test class that defines test cases for the users class behaviour.
    
    unittest.TestCase class helps in creating test cases.
    """
def setUp(self):
    '''
    method to run before test case
    '''
    self.new_users = Users("Jay_Ian","Ian","Wanarua","Pass254")
    self.new_credentials = Credentials("Twitter","Jay_Ian","Pass254")

def test_init(self):
    '''
    test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.user_name, "Jay_Ian")
    self.assertEqual(self.new_user.f_name, "Ian")
    self.assertEqual(self.new_user.l_name, "Wanarua")
    self.assertEqual(self.new_user.password, "Pass254")

def test_credentials_init(self):
    '''
    test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_credentials.account_name, "Twitter")
    self.assertEqual(self.new_credentials.username, "Jay_Ian")
    self.assertEqual(self.new_credentials.password, "Pass254")
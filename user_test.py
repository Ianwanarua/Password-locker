import unittest
from Credentials import Credentials
from User import Users

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
    self.assertEqual(self.new_users.user_name, "Jay_Ian")
    self.assertEqual(self.new_users.f_name, "Ian")
    self.assertEqual(self.new_users.l_name, "Wanarua")
    self.assertEqual(self.new_users.password, "Pass254")
    
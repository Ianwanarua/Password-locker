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
    
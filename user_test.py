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
    self.new_user = Users("Jay_Ian","Ian","Wanarua","Pass254")
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
    
    #second test

def test_save_user(self):
    '''
    tests if user are saved into the users_list
    '''
    self.new_user.save_users()
    self.assertEqual(len(Users.users_list), 1)
    
def test_save_credentials(self):
    '''
    tests if credentials are saved into the credentials_list
    '''
    self.new_credentials.save_account()
    self.assertEqual(len(Credentials.credentials_list), 1)
    
    #3rd Test
    
def tearDown(self):
    '''
    does clean up after each test case has run
    '''
    Users.users_list = []
    Credentials.credentials_list = []
    
def test_save_multiple_user(self):
    '''
    test case to check if we  can save multiple users
    '''
    self.new_user.save_users()
    test_user = Users("GK","Gedion","Kavivya","mason007")
    test_user.save_users()
    self.assertEqual(len(Users.users_list),2)
    
def test_save_multiple_credentials(self):
    '''
    test case to check if we  can save multiple credentials to the credentials lists
    '''
    self.new_credentials.save_account()
    test_credentials = Credentials("FB","GK","mason007")
    test_credentials.save_account()
    self.assertEqual(len(Users.users_list),2)
    
    

        
    

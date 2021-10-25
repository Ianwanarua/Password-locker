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
        self.assertEqual(self.new_user.username, "Jay_Ian")
        self.assertEqual(self.new_user.first_name, "Ian")
        self.assertEqual(self.new_user.last_name, "Wanarua")
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
        self.assertEqual(len(Users.user_list), 1)

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
        Users.user_list = []
        Credentials.credentials_list = []

    def test_save_multiple_user(self):
        '''
        test case to check if we  can save multiple users
        '''
        self.new_user.save_users()
        test_user = Users("GK","Gedion","Kavivya","mason007")
        test_user.save_users()
        self.assertEqual(len(Users.user_list),2)

    def test_save_multiple_credentials(self):
        '''
        test case to check if we  can save multiple credentials to the credentials lists
        '''
        self.new_credentials.save_account()
        test_credentials = Credentials("FB","GK","mason007")
        test_credentials.save_account()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    #4th Test
    def test_delete_credentials(self):
        '''
        Test delete to see if we can remove user credentials from list
        '''
        self.new_credentials.save_account()
        test_credentials = Credentials("Twitter","Jay_Ian","pass254")
        test_credentials.save_account()
        self.assertEqual(len(Credentials.credentials_list),2)
    #5th test
    
    def test_find_user_byusername(self):
        '''
        Test to find if user exist by searching in their username
        '''
        self.new_user.save_users()
        test_user = Users("GK","Gedion","Kavivya","mason007")
        test_user.save_users()

        User_exists = Users.findby_username("GK")
        self.assertEqual(User_exists.username,test_user.username)

    
    def test_find_by_account_name(self): #credentials
        '''
        Test to check if an account exists by searching the accounts name
        '''

        self.new_credentials.save_account()
        test_credentials = Credentials("Twitter","Jay_Ian","pass254")
        test_credentials.save_account()

        credentials_found = Credentials.find_by_account_name("Twitter")
        self.assertEqual(credentials_found.account_name,test_credentials.account_name)
        
    def test_user_exist(self):
        '''
        To check if a user is already registered
        '''
        self.new_user.save_users()
        test_user = Users("GK","Gedion","Kavivya","mason007")
        test_user.save_users()

        user_exist = Users.user_exist("GK","mason007")
        
        self.assertTrue(user_exist)
        
    def test_account_exist(self):
        '''
        test if account exists by searching username
        '''
        self.new_credentials.save_account()
        test_credentials = Credentials("Twitter","Jay_Ian","pass254")
        test_credentials.save_account()

        account_exist = Credentials.account_exist("Jay_Ian")
        self.assertTrue(account_exist)
        
    def test_display_credentials(self):
        '''
        Test to return list of user credentials saved
        '''
        self.assertEqual(Credentials.display_account(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()


        
    

class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = []
    
    def __init__(self,account_name, username, password):
        """
        __init__method to help us create new instances of the class credentials
        """
        self.account_name = account_name
        self.username = username
        self.password = password
    
    def save_account(self):
        """Method to save new account to the credentials_list"""
        Credentials.credentials_list.append(self)

    @classmethod
    def account_exist(cls, username):
        '''
         Method that checks if an account exists from the credentials list.
         
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for Credentials in cls.credentials_list:
            if Credentials.username == username:
                return True

        return False
    

    @classmethod
    def find_by_account_name(cls, account_name):
        """
        method to search account by account name
        """
        for account in cls.credentials_list:
            if account.account_name == account_name:
                return account

    def delete_account(self):
        '''
        method to delete a saved account credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_account(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

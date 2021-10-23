class Users:
    """
    class that generates new instances of users
    """
    
    users_list = []
    
def __init__ (self,user_name,f_name,l_name,password):
        '''
        This is a blueprint that every user instance must conform to
        '''
        self.user_name = user_name
        self.first_name = f_name
        self.last_name = l_name
        self.password = password
        
def save_users(self):
        """Method to save new account to the users_list"""
        Users.users_list.append(self)
        
@classmethod
def user_exist(cls, username, password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            string: username to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True

        return False

@classmethod
def findbyname(cls,  username, password):
    """ Method to find user by searching their name"""
    for user in cls.user_list:
            if user.username == username and user.password == password:
                return user

        
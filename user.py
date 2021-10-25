class Users:
    """
    class that generates new instances of users
    """
    
    user_list = []
    
    def __init__ (self,username,first_name,last_name,password):
            '''
            This is a blueprint that every user instance must conform to
            '''
            self.username = username
            self.first_name = first_name
            self.last_name = last_name
            self.password = password

    def save_users(self):
            """Method to save new account to the user_list
            """
            Users.user_list.append(self)
            
    @classmethod
    def user_exist(cls, username, password):
            '''
            Method that checks if a user exists from the user list.
            Returns :
                Boolean: True or false if the user exists
            '''
            for user in cls.user_list:
                if user.username == username and user.password == password:
                    return True

            return False
        

    @classmethod
    def findby_username(cls,  username):
        """ Method to find user by searching their username
        """
        for user in cls.user_list:
                if user.username == username:
                    return user

        
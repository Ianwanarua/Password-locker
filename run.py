#!/usr/bin/env python3.9
from credentials import Credentials
from user import Users
import string
import random


def create_user(username,first_name,lastname,password):
    '''
    function to create a new account
    '''
    new_user = Users(username,first_name,lastname,password)
    return new_user

def save_users(Users):
    '''
    Function to save a new user
    '''
    Users.save_users()
    
def create_credentials(account_name, username, password):
    '''
    Function to create new passwords for the application
    '''
    new_credentials = Credentials(account_name, username, password)
    return new_credentials
def save_account(Credentials):
    '''
    This function will save all instances of the credentials
    '''
    Credentials.save_account()
    
def findby_username(username, password):
    '''
    Function that finds a account by number and returns the account
    '''
    return Users.findby_username(username, password)
def user_exist(password):
    '''
    This function will check if a given password exists in the user list
    '''
    return Users.user_exist(password)

def account_exist(username):
    '''
    This function will check if account exist
    '''
    return Credentials.account_exist(username)

def find_by_account_name(account_name):
    '''
    This function finds account credentials by searching account name
    '''
    return Credentials.find_by_account_name(account_name)

def verify_user(username,password):
    '''
    This function will verify user exist
    '''
    return Users.user_exist(username,password)

def delete_account(account_name):
    '''
    function will delete credentials from the list
    '''
    Credentials.credentials_list.remove(account_name)

def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_account()

def choose(question):
    '''
    Here the user will respond to if to generate password
    '''
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        return response
    



def main():
    print("Hello welcome to password-locker. What is your name?")
    name = input()
    print(f"Hi {name}, proceed to create an account")
    print('\n')
    print("****************")
    print('\n')
    print("Create your account")
    print('\n')
    print("Enter a username")
    username = input()

    print("First Name")
    firstname = input()

    print("Last Name")
    lastname = input()

    print("New password")
    password = input()
    
    save_users(create_user(username,firstname,lastname,password))
    print('\n')
    
    if username=='' or firstname=='' or lastname=='' or password=='':
        print("Fill in the  fields")
    else:
        save_users(create_user(username,firstname,lastname,password))
        print(f"Username:{username} Password: {password} You have created your account successfully.")

        print("Login with your details to proceed")
        print('\n')

        print("Enter your username")
        userlogin = input()
        print('\n')

        print("Enter your password")
        passwordlogin = input()
        

        if verify_user(userlogin,passwordlogin):
            print(f"{userlogin} welcome to password-locker")
            
            while True:
                print('\n')
                print("****************")
                print('\n')
                print("Use these short codes : na - create a new account credential, da - display account, fa -find an account,dl - delete account, ex -exit the account list ")
                print('\n')
                print("****************")
                print('\n')
                
                shortcode = input().lower()
                if shortcode == 'na':
                    print("New Credential Account")
                    print("-"*10)

                    print("New Account Name")
                    account_name = input()

                    print("Username")
                    username = input()
                    
                    
                    generate = choose("Generate password? (y/n):")
                    if generate == "y":
                            length = int(input('Enter the length of the password: '))
                            lower = string.ascii_lowercase
                            upper = string.ascii_uppercase
                            num = string.digits
                            symbols = string.punctuation
                            all = lower + upper + num + symbols
                            temp = random.sample(all,length)
                            password = "".join(temp)
                            
                    else:
                        
                        print("Enter your password")
                        password = input()
                            
                        save_account(create_credentials(account_name, username, password))
                        print('\n')
                        print(f"New account: {account_name}  with user name : {username} and password :{password} created successfully")
                        print('\n')
        
                elif shortcode == 'da':
                        if display_account():
                            print("Here is a list of all your accounts")
                            print('\n')

                            for credential in display_account():
                                print(
                                    f"{credential.username} |   {credential.account_name} |   {credential.password}")

                        else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                        print('\n')
                        
                elif shortcode == 'fa':
                    print("Enter the account name you want to search for")

                    search_account = input()
                    if find_by_account_name(search_account):
                        check_account = find_by_account_name(search_account)
                        print(f"{check_account.account_name}")
                        print('-' * 20)

                        print(f"Account Name.......{check_account.account_name}")
                        print(f"Username.......{check_account.username}")
                    else:
                        print("That account does not exist")
                    print('\n')
                    
                elif shortcode == 'dl':
                    print("Enter name of account to delete")
                    search_account = input()
                    if find_by_account_name(search_account):
                        check_account = find_by_account_name(search_account)
                        delete_account(check_account)
                        print(
                            f"Account {check_account.account_name}deleted successfully")
                    else:
                        print('\n')
                        print("You dont seem to have any accounts saved yet")

                elif shortcode == "ex":
                    print("Bye .......")
                    break
                else:
                    print("Please use the short codes")
            
        
if __name__ == '__main__':
    main()




    

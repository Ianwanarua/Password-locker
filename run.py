#!/usr/bin/env python3.9
from credentials import Credentials
from user import Users
import random

def create_user(username,firstname,lastname,password):
    '''
    function to create a new account
    '''
    new_user = Users(username,firstname,lastname,password)
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
    return Credentials.account_exist(username)

def find_by_account_name(account_name):
    return Credentials.find_by_account_name(account_name)

def delete_account(account_name):
    Credentials.credentials_list.remove(account_name)

def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_account()

def main():
    print("Hello welcome password-locker. What is your name?")
    name = input()
    print(f"Hi {name}, what would you like to do?")
    print('/n')
    print("****************")
    
    
        
        
if __name__ == '__main__':
    main()




    

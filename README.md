# Password Locker

## Author

[**Ian Wanarua**]()

## Description

A python program which runs on the terminal. The app, stores user's account credentials and also generates passwords for a user's new or existing accounts using the inbuilt random and string libraries. Users can also delete and display user account and credentials.


## Technologies Used

* Git
* Python 3.9
* The following external python libraries were used in this project:
    - string (inbuilt)
    - random (inbuilt)
    - unittest

## Requirements

* This program requires python3.+ installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)

## Setup/Installation

To user the appliction, first make sure you have installed the required modules from above as well as have python 3.+ installed in your computer.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/Ianwanarua/Password-locker.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Open the terminal, go to the project directory and run the following commands: **`chmod +x run.py`** and **`./run.py`** respectively to launch the program.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open on terminal | Run the command ```$ ./run.py```|Welcomes to Password locker... <br>* na ---  Create New Account |
|Select  na| input new username and password| New  account with ```username```, and ```password``` has been created|
|Display stored credentials | Enter ```da```|A list of all credentials that has been inputed|
|Find an account|Enter ```fa```| Enter the account name you want to search for and returns the account credentials|
|Delete an existing credential from the list|Enter ```dl```|Enter name of account to delete and returns true if the account has been deleted and false if the account doesn't exist|
|Exit| Enter ```ex```| Bye.....|


## Known Bugs

* There were no bugs.

## Support and Further contact details

* For queries you can contact me through

ian.wanarua@student.moringaschool.com

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright © 2021  [Ian wanarua](https://github.com/ianwanarua)


# Password_Locker  
#### 24/10/2021
#### By **Annalis Kirwa**  
## Description   
This is a python application that allows a user to create an account with their details( username and password). It allows the user to store existing credentials in the 
app as well as create new account credentials. A user can also type their own passwords or have their passwords generated in the application. One can also delete the account
details they no longer need.  
## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./userinterface.py```|Hello Welcome to your Password locker... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|   

## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pyperclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone using this  <a href = "https://github.com/Annaliskirwa/Password_Locker.git">```link```</a>

* cd Password_Locker

* code . to open it on Visual studio code or atom . to open in atom editor.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x interface.py
        $ ./userinterface.py
* To run test for the application
        $ python3 passwordlock_test.py

## To contribute to the web application:
* Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/Password_Locker" >link </a>
* Clone the repository
* Open the link from where the repository is saved  
* Make contributions   
## Features
The user would be able to:
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard  

##Known bugs  
There are no known bugs so far.   
## Technologies Used
* Python3.6  
## Support and contact details
In case of any problem while interacting with the application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**

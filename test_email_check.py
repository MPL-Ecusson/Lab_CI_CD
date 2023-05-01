'''
First, we want to create a function that checks if an email address is valid

def email_function(input):
    if correct:
	return 1
    else:
	return 0

The function was recognize the presence of '@' and presence of "." after "@"

Second, we want to create a function that check if a username is valid
 -cannot be empty
 -no space
 -all characters are alphanumeric

'''
import re

def check_email (input):
    if (len(input.split("@")) == 2) & (len(re.split('@',input)[1].split(".")) == 2):
        return 1
    else:
        return 0

#do we have a function?
def test_fun():
    assert check_email('h@gmail.com') 


#is there a single @?
def test_at():
    assert check_email("h@gmail.com") == 1

#function 
user = "badass12"
def check_username(name):

#check that name is  alpha numeric
    if name.isalnum() == False:
        return 0

#check that username is not empty
    if name == "":
        return 0

#check that username contains no spaces
    if len(name.split(' ')) != 1:
        return 0
    else:
        return 1

#testing
def test_good_username():
    assert check_username(user) == 1

def test_username_spaces():
    assert check_username("a a b") == 0
    assert check_username(" ") == 0


def test_empty_username():
    assert check_username("") == 1

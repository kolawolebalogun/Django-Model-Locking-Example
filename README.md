# Django-Model-Locking-Example
Making Django Model Instance available by 1 user at a time, Prevents users from overwriting each others changes in Django.

## Requirement

Django Admin Locking Example has been tested in the following environments

* Python (3.6)
* Django (1.11.7)

## Installation

First you create a virtual environment with `virtualenv venv` and enter it with `source venv/bin/activate` in order to keep everything contained. 

Then you run `pip install -r requirements.txt` to install all dependencies

Start Django Server by running `python manage.py runserver` then visit ![http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your browser.


![screen shot](https://raw.githubusercontent.com/kolawolebalogun/Django-Model-Locking-Example/7438fc213361af6335f283f9adef90907b86b5c2/screenshots/Screen%20Shot%202017-11-04%20at%208.07.44%20PM.png)
![screen shot](https://raw.githubusercontent.com/kolawolebalogun/Django-Model-Locking-Example/7438fc213361af6335f283f9adef90907b86b5c2/screenshots/Screen%20Shot%202017-11-05%20at%206.52.59%20AM.png)
![screen shot](https://raw.githubusercontent.com/kolawolebalogun/Django-Model-Locking-Example/7438fc213361af6335f283f9adef90907b86b5c2/screenshots/Screen%20Shot%202017-11-05%20at%206.53.29%20AM.png)


## Test Case
Name | Value  
:--- | :--- 
Test Suite ID | TS001 
Test Case ID | TC001
Test Case Summary | This test is to confirm that Django Model Instance available by 1 user at a time. <br>User_1 logs in to Django Admin and accesses this model instance. Now User_1 can see all the fields and edit them. Meanwhile, User_2 opens the same model in Django admin. User_2 can't edit this model and all actions are disabled. As soon as User_1 closes this form (navigating away from form) User_2 can edit it.
Prerequisites | 1. User_1 & User_2 are authorized.
Test Procedure | 1.	User_1 logins. Tries to edit a row from Insydo guides.<br> 2. User_2 logins and try to edit the same row from Insydo guides.
Expected Result | 1. User_2 is suppose to get a message that says the form is locked by User_1 also the form field and save button are to be disabled.
Actual Result | 
Status | 
Remarks | This is a test case for Django-Model-Locking
Created By | Kolawole Balogun
Date of Creation | 05/11/2017
Executed By | 
Date of Execution | 
Test Environment | 
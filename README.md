# LitReview

1.Introduction

An introductory work to MVT using the basics of DJANGO.

This is a web application that allows :
- Registration of new user and authentication of registered users
- Users can follow others
- Users can ask for a book or article review via a ticket
- Users can post their own reviews of books
- Other users can answer these reviews via an answer to the ticket

2-Install the app 

- Download the ZIP files and unzip them in the repository you wish
- Install venv by typing in your terminal :
'''
$ pip install venv
'''
- Create de the virtual environement and lauch it by typing :
'''
$ python -m venv env
'''
and
'''
$ env\Scripts\activate
'''
- install the packages by typing :
'''
$pip install -r requirements.txt
'''

3. Launch the DJANGO server

Go to the "LitReview" repository then type in :
$ python manage.py runserver

You can then access the site via your web browser at the following URL:
http://127.0.0.1:8000/



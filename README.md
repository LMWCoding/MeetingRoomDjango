# Meeting Room Signage

Developed: by Lee Man Wei

Language
    Python 3.6
    Javascript  / May add in react if needed in future

Framework
    Django

DB
    sqlite (stored as a single file on the server)

## Usage

    Primary purpose is to room usage (name of customer, or name of meeeting) on a signage outside meeting room.

    The meeting inforrmation is stored in a DB on the server.  The client device (signage) will receive a webpage showing the name, automatically updated according to the time of the meeting.

    Access the index page for instruction

## Deployment

This are NOT production deployment instructions.

### Manual

Pre-requisites : python3

    copy the files into a directory / git clone it

Install the required python packages.  Note, if you have other software, you may want to do venv etc.  Instruction not covered here.

    $ pip install -f requirements.txt

After that, django is installed

Review & Edit the meetingroomdjango/settings.py file

    In particular, replace the SECRET_KEY
    
    SECRET_KEY = '80ay2**********************************y31=$r'
    
    with the key generated in next step
    
    $ python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

This creates the initial user credential for the admin portal

    $ python3 manage.py createsuperuser

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

    $ python3 manage.py runserver 0.0.0.0:8000

## Notes to understand the code

For those unfamiliar with Django, here are the order to understand the code

1. meeetingroomdjango.  Look under urls.py
2. That will link to the paths for /entry  and /signage.  Look into the urls.py in those directory
3. The database model is at entry/models.py.  Enter data using the /admin route provide by Django
4. /entry app is meant for entering the data entry for the meeting.  Now just provide as a index for the whole site
5. /signage app is for the devices to access

## History

Initial release 2020-09-18   Enter the meeting information through the admin console
  
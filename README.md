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

    Special note on Time Zone :

    USE_TZ = True is set now
    The admin user (enter data), and the signage must be at same time zone.
    
    If at different time zone, for example, if the admin is done at GMT+8, and entered a meeting at 10am.  But the signage is at GMT+9, that meeting is actually at 11am.

    This design choice is because admin and signage is usually at same time zone.  So admin/signage pair at different time zone can use same server.  Limitation is one admin cannot enter information for two differnt time zones.

## Deployment

These are NOT production deployment instructions.  It is not secured, not the best practice.

### Manual Deployment

Pre-requisites : python3

    copy the files into a directory / git clone it

Install the required python packages.  Note, if you have other software, you may want to do venv etc.  Instruction not covered here.

    $ pip install -r requirements.txt

Django is installed as part of the requirements

Review & Edit the meetingroomdjango/settings.py file

    In particular, replace the SECRET_KEY
    
    SECRET_KEY = '80ay2**********************************y31=$r'
    
    with the key generated in next step
    
    $ python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

This creates the initial user credential for the admin portal

    $ python3 manage.py createsuperuser

Update model strucutre

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

Start the server

    $ python3 manage.py runserver 0.0.0.0:8000

## Notes to understand the code

For those unfamiliar with Django, here are the order to understand the code

1. meeetingroomdjango is the top level.  Look under urls.py
2. That will link to the paths for /entry  and /signage.  Look into the urls.py in those directory
3. The database model is at entry/models.py.  Enter data using the /admin route provide by Django
4. /entry app is meant for entering the data entry for the meeting.  Now just provide as a index for the whole site
5. /signage app is for the devices to access

## History

Initial release 2020-09-18   Enter the meeting information through the admin console
  
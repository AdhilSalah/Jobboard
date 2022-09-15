
# Jobboard

Jobboard is a platform where users can hired and get hired,post blogs,rect to blogs,message to users.

Link = http://65.2.3.224/





## How to Setup

 - Clone this repositary
 - Create Python virtual environment
 - Do pip install -r requirements.txt
 - Install postgres
 - Open postgres and create a databse and user
 - Grant all previlages to the user
 - Add the db details in jobboard/settings.py 
 - Set the port number as 5432
 - Do pip install djangorestframework-simplejwt==5.2.0
 - Do pip install  social-auth-app-django==5.0.0(cannot do on requirements.txt because some errors)
 - Do python manag.py migrate(for model mirations to reflect on your db)
 - Do python manage.py createsuperuser(for creating an admin)
 - Then Python manage.py runserver to run the server 



## Features

User:

* User can signup
- User siginin
- Email verification
- Reset password option
- Continue with google option
- User can add job
- User can post a blog
- User can react to blog
- User can create a full profile
- Users can message each other



## Libraries Used

- Django rest framework
- simpleJWT 
- Channels
- Django-fiters
- Pillow
- Django-social-auth





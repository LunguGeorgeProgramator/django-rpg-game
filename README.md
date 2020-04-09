# django-rpg-game

A simple battle arena rpg

Istall gide for Djnago on windows:

   https://docs.djangoproject.com/en/3.0/howto/windows/

1. install python, in my case python version 3.77 from this link:
  
  https://www.python.org/downloads/release/python-377/
  
 2. test the version n a cmd terminal:
 
     PS C:\Users\XXX> py --version
              
 Also I am using pip version 20.0.2
        
Set up virtual env:
  
      py -m pip install virtualenvwrapper-win
    
      py -m virtualenv venv
    
To start the virtual env:

      venv\Scripts\activate

To stop use comand:

      venv\Scripts\deactivate
      
 Install django comand:
 
      py -m pip install Django
      
Enter with projrcts paths:

    cd env
    
create a folder called 'myProjects' in the venv folder then enter it: cd myProjects

pull the code with git to the folder or copy paste the content and enter the folder: cd django-rpg-game

To run the server comand:

      py manage.py runserver
  
Then check the link in browser to see the site:

      http://127.0.0.1:8000/
   
   
      venv\Scripts\activate
      cd venv\myProjects\django-rpg-game
      py manage.py runserver

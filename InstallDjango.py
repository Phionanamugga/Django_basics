""" Install Django
Now, that we have created a virtual environment, we are ready to install Django.
Note: Remember to install Django while you are in the virtual environment!
Django is installed using pip, with this command:
Windows:
(myworld) C:\Users\Your Name>py -m pip install Django
Unix/MacOS:
(myworld) ... $ python -m pip install Django
Which will give a result that looks like this (at least on my Windows machine):
Collecting Django
  Downloading Django-4.0.3-py3-none-any.whl (8.0 MB)
      |████████████████████████████████| 8.0 MB 2.2 MB/s
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting tzdata; sys_platform == "win32"
  Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
      |████████████████████████████████| 339 kB 6.4 MB/s
Installing collected packages: sqlparse, asgiref, tzdata, Django
Successfully installed Django-4.0.3 asgiref-3.5.0 sqlparse-0.4.2 tzdata-2021.5
WARNING: You are using pip version 20.2.3; however, version 22.3 is available.
You should consider upgrading via the 'C:\Users\Your Name\myworld\Scripts\python.exe -m pip install --upgrade pip' command.
That's it! Now you have installed Django in your new project, running in a virtual environment!

Windows, Mac, or Unix?
You can run this project on either one. There are some small differences, like when writing commands in the command prompt, Windows uses py as the first word in the command line, while Unix and MacOS use python:

Windows:

py --version
Unix/MacOS:

python --version
In the rest of this tutorial, we will be using the Windows command.

Check Django Version
You can check if Django is installed by asking for its version number like this:

(myworld) C:\Users\Your Name>django-admin --version
If Django is installed, you will get a result with the version number:

4.1.2
What's Next?
Now you are ready to create a Django project in a virtual environment on your computer.

In the next chapters of this tutorial we will create a Django project and look at the various features of Django and hopefully make you a Django developer.
"""
# Django Tutorial
# Django is a back-end server side web framework.
# Django is free, open source and written in Python.
# Django makes it easier to build web pages using Python.
# Learning by Doing
# In this tutorial you get a step by step guide on how to install and create a Django project. 
# You will learn how to create a project where you can add, read, update or delete data.
# You will learn how to make HTML Templates and use Django Template Tags to insert data within a HTML document.
# You will learn how to work with QuerySets to extract, filter, and sort data from the database.
# You will also learn how to set up a PostgreSQL database and how to deploy your Django project to the world.
# Django Display Admin Syntax QuerySets Static Files PostgreSQL Deploy

# Django Exercises
# Exercise:
# Insert the missing parts to write a Django variable in a template:

#<h1>Hello firstname ,how are you?</h1>

# Example 2
"""<ul>
    {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>"""

"""Django Introduction
What is Django?
Django is a Python framework that makes it easier to create web sites using Python.
Django takes care of the difficult stuff so that you can concentrate on building your web applications.
Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).
Django is especially helpful for database driven websites.
How does Django Work?
Django follows the MVT design pattern (Model View Template).
Model - The data you want to present, usually data from a database.
View - A request handler that returns the relevant template and content - based on the request from the user.
Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.
Model
The model provides data from the database.
In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.
The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.
Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.
The models are usually located in a file called models.py.
View
A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.
The views are usually located in a file called views.py.
Template
A template is a file where you describe how the result should be represented.
Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.
Django uses standard HTML to describe the layout, but uses Django tags to add logic:
<h1>My Homepage</h1>
<p>My name is {{ firstname }}.</p>
The templates of an application is located in a folder named templates.

URLs
Django also provides a way to navigate around the different pages in a website.

When a user requests a URL, Django decides which view it will send it to.

This is done in a file called urls.py.

So, What is Going On?
When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:

Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
The view, located in views.py, checks for relevant models.
The models are imported from the models.py file.
The view then sends the data to a specified template in the template folder.
The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.
Django can do a lot more than this, but this is basically what you will learn in this tutorial, and are the basic steps in a simple web application made with Django.

Django History
Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines in the newspaper and at the same time meeting the demands of experienced web developers.
Initial release to the public was in July 2005.
Latest version of Django is 4.0.3 (March 2022).
To install Django, you must have Python installed, and a package manager like PIP.
PIP is included in Python from version 3.4.
Django Requires Python
To check if your system has Python installed, run this command in the command prompt:
python --version
If Python is installed, you will get a result with the version number, like this
Python 3.9.2
If you find that you do not have Python installed on your computer, then you can download it for free from the following website: https://www.python.org/
PIP
To install Django, you must use a package manager like PIP, which is included in Python from version 3.4.
To check if your system has PIP installed, run this command in the command prompt:
pip --version
If PIP is installed, you will get a result with the version number.
For me, on a windows machine, the result looks like this:
pip 20.2.3 from c:\python39\lib\site-packages\pip (python 3.9)
If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/
Virtual Environment
It is suggested to have a dedicated virtual environment for each Django project, and in the next chapter you will learn how to create a virtual environment, and then install Django in it.
"""
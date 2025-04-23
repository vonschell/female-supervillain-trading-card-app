# Install Python

Check to see if you already have Python installed on your system by running:

On a Mac:
`python3 --version`

On Windows:
`python --version`

If you already have Python installed, check to be sure it’s Python 3.8 or up. (For example, 3.11 is great!) We suggest waiting on 3.12 to give any dependencies time to be updated.

If you are using a Windows machine, it is possible that you don’t have Python installed. You’ll need to pause here for a moment and proceed to install it. See this document for more [information](https://docs.google.com/document/d/14diNu_g6uhouBscRt8zIezolANTRQA6HobKRP4Lgu5Q/copy).

# Setting up to run scripts to work with Python.

The script will be run in a virtual environment. Start by creating a virtual environment. Navigate to to the project folder in the command line and run:

On a Mac:
`python3 -m venv venv`

On Windows:
`python -m venv venv`

<br>
After creating the virtual environment, you need to activate it:

On a Mac:
`source venv/bin/activate`

On Windows:
`source venv/Scripts/activate`

<br>
Once the virtual environment is activated, the beginning of your terminal prompt should display (venv).

<br>
Install the modules by running (in both a Mac and Windows):

`pip install flask flask-sqlalchemy`

You'll see a venv folder has been added to the directory with all of the installed dependencies.

<br>

To run your code, in the command line run:

Without a debugger:
`flask run`

With a debugger:
`flask run --debug`

<br>

The app will run at: http://127.0.0.1:5000/

<br>

To stop the run, click control + C. When making changes to your Python, HTML, or JavaScript code (and not using debugger) you'll need to stop the run after each change. After restarting the server, hard refresh the page.

<br>
When finished, quit the run by clicking control + C and close the virtual environment by running:

`deactivate`

<br>

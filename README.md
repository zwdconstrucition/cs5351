# Scrum 

This is the course project of the Group "Course Project 24" for the CityU CS5351 24Fall

Online Python Web Editor using Python Flask and HTML

Utilize CodeMirror for code highlighting

Implemented code auto-completion

Able to generate flowcharts based on Python code

效果图：

![editor](doc/FinalFrontend.png)

## Assignment Requirement Analysis

The planned functions to implement are:

1. **User Login System**：Each user can log in and have their own workspace.

Store user information and passwords using a database, and provide a login interface on the web page.

2. **Code Highlighting**：When editing Python code, different colors are displayed for functions, variables, strings, etc.

Use the third-party package CodeMirror to parse the input code and automatically add HTML tags to achieve different colors.

3. **Code Auto-Completion**：Through the input characters, recognize and complete common Python functions and keywords, as well as custom variable names and function names.

Use a modified version of CodeMirror, adding python-hint.jsto suggest Python completions, and include relevant code to fetch all defined variables and functions for further suggestions.

4. **Code Auto-Correction**：Predict whether there are spelling errors in keywords, and highlight them if there are.

Use the edit distance algorithm to compare the keywords in the code with Python keywords. If the edit distance < 2, highlight with a wavy underline.

4. **Run Code and Display Results**：Able to run the code on the web end and display the results.

Run the code on the server side, redirect the output and error streams, capture the program output, and return it to the webpage.

5. **Flowchart Generation**：Generate a flowchart based on the execution process of Python code.

Use the pyflowchart package to analyze the code, generate flowchart text in markdown format, and then use external code flowchart.jsto generate the flowchart on the webpage.
## Project Description

Python package requirements:

```
flask
pyflowchart
json
sqlite3
```

**main.py**：Flask main program

**user_login.py**：Code controlling user login functionalities

**run_code.py**：Code controlling functionalities related to running and editing code

**FLowChart.py**：Code related to generating flowcharts

**DBdebug.py**：Database debugging code



**users.db**：Database storing user data

**work/**：Directory storing the workspaces of all users



**static/editor.html**：Main interface of the editor

**static/register_success.html**：Registration success page

**static/repeat_login.html**：Duplicate login display page



**static/element.css**：Styles for editor elements

**static/layout.css**：Layout styles

**static/login.css**：Login and registration interface styles



**static/python-hint.js**：JavaScript code for Python auto-completion

Other files in the static folder are files from third-party packages



**templates/flowchart.html**：Flowchart display template

**templates/index.html**：Login interface

**templates/register.html**：Registration interface


## Project Operation Manual

Command to run the server

```
python main.py
```

Enter localhost in the browser to access the webpage.

For the first login, you need to register an account, or use a test account:

```
user: Alice           passwprd : 12345
```

On the editor page, the left side is the file selection list, and the right side is the code editing area.

The top has buttons for "New", "Delete", "Run", "Save", "Generate Flowchart".

Functions like running and generating flowcharts must be performed after saving the code.

The program output is displayed at the bottom.

### Test Data

Test accounts:

```
user: Alice           pwd : 12345
```

Test code:

The user CaptainChen has a file named prime.py which outputs prime numbers from 1 to 100.

You can run this code and generate its flowchart, as shown below:

<img src="doc/prime_run.png" alt="prime_run" style="zoom:40%;" />        

  <img src="doc/FinalFlowChart.png" alt="prime_flowchart" style="zoom:80%;" />



Test code Dijkstra.py, runs the shortest path algorithm.

Test code add.py, can display error messages:

```
3
1
Traceback (most recent call last):
  File ".\add.py", line 5, in <module>
    print(1/0)
ZeroDivisionError: division by zero
```



# Graphical User Interface for IEX Cloud REST API

#### Eric Stevens


## A note to the grader

One of the main concepts I was drawn towards in the course was the power of PyCharm. I took it to heart and have begun using it for all my projects. That being said. This is the first project I have ever done using the PyCharm project environment and I am still learning the organization of projects and how the virtual environment aspect of projects work. 

## Running the GUI

### Running in PyCharm
The easiest way to run the application is to open the project in a PyCharm environment, ensure that the interpreter you are using has access to the required libraries and run the `MainGUI.py` script which can be found in the `ui_files` project sub-directory. If the proper libraries are accessible, the user interface should pop up. **I have left my user tokens in the login page. Feel free to use them. You can see the allowances on upon login.**

### Running outside of PyCharm
I do not recommend running the project outside of the PyCharm environment. If you choose to you will have to add the project directory to the `PYTHONPATH` environment variable. This can be done on Unix systems by navigating to the project directory and executing the line export `PYTHONPATH=.`. 


## Required Packages

In order to run the GUI the following packages must be accessible from the interpreter you choose to use.

```
numpy
matplotlib
json
datetime
requests
pyqt5
```


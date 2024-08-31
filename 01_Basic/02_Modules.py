'''
Topic :- Module and Pip

Modules - A Module is a file containing code written by someone else(which) can be imported and used in our programs
Types of Modules - a).Builtin Modues(Preinstalled in python)
                   b).External Modules(need to installl using pip)

PIP  - Pip is a package manager for python . you can use pip to instal a module onn your system
Eg :Pip install pyjokes

REPL - (Read Evaluate print loop) It give or print Direct Answer in CMD or shell
'''

# Module 1 - it generates Different Jokes
'''
import pyjokes

joke = pyjokes.get_joke()
print(joke)
'''

# Module 2 - we can create Our own voice Assistant

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Dhanush, I am Jarvis ")
engine.runAndWait()


# Module 3 -
'''
import os
directory_path = '/Desktop'
contents = os.listdir(directory_path)
for item in contents:
    print(item)
'''
# diffsh

A Python2.7 REPL shell that extends diff functionality to compare file outputs given the same arguments or the same inputs piped to it. Useful for output comparison with compiled executables. 

## Usage

Starting the shell is as simple as executing the Python file by typing `python diffsh.py`. If this does not work, try `python2.7 diffsh.py` — some of the features in this shell do not work for Python3, as the files I wanted to compare initially were on a system incompatible with Python3. 

### Commands

*Usage:*
First, you are prompted to pass in two executables to compare.

* `help` prints out a help screen.
* `args` pass in the following string as arguments to both executables
* `pipe` pipe the output of the next string, interpreted as a program, to the executables
* `progs` reprompts user for a different pair of programs to compare.

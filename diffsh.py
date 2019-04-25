#!/usr/bin/env python

import sys
import signal
import os
import subprocess
import itertools

def prompt_exit():
    exit = raw_input("Confirm exit? (Y/N) ")
    if exit == "Y" or exit == 'y':
        sys.exit(0)
    sys.stdout.write("Exit not confirmed\n")

def signal_handler(sig, frame):
    if (sig == signal.SIGINT):
        prompt_exit()
        os.kill(os.getpid(), signal.SIGCONT)
        sys.stdout.write("diffsh>>> ")
    

def repl(prog1, prog2):
    sys.stdout.write("Creating diff evaluation shell...\n")
    while True:
        sys.stdout.write("diffsh>>> ")
        line = sys.stdin.readline().strip()
        if not line:
            prompt_exit()
            continue
        cmdAndArgs = line.split(None, 1)
        cmd, line = cmdAndArgs[0], cmdAndArgs[1:]

        if cmd == 'help':
            print "Usage: <command> [args]"
            print ""
            print "Commands:"
            print '\n'.join(_cmd + '\t\t' + _desc for _cmd, _desc in [
                ('help', 'View this help screen'),
                ('args', 'Pass in the following string as arguments'),
                ('pipe', 'Treating next string as executable, pipe output to programs'),
                ('progs','Prints out currently compared programs and prompts changing the programs')
            ])
            print ""
            print "Enter empty line to quit"
        elif cmd == 'args':
            if not len(line):
                print "Usage: args <arguments-to-prog1-prog2>"
                continue
            print prog1, ' '.join(line) 
            print prog2, ' '.join(line)
            print subprocess.check_output(list(itertools.chain.from_iterable([prog1, line])))
            print subprocess.check_output(list(itertools.chain.from_iterable([prog2, line])))
        elif cmd == 'pipe':
            if not len(line):
                print "Usage: pipe <progam-piped-to-prog1-prog2>"
            print "Piping output of", "\"" + line + "\"", "to", prog1, "and", prog2
        elif cmd == 'progs':
            print "Diff-ing these programs:", prog1, prog2
        else:
            print "Command not recognized/supported:", cmd

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    prog1 = ""
    prog2 = ""
    if (len(sys.argv) > 2):
        prog1 = argv[1]
        prog2 = argv[2]
    else:
        prog1 = raw_input("Please enter the name of executable 1: ")
        prog2 = raw_input("Please enter the name of executable 2: ")
    repl(prog1, prog2)


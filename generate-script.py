#!/usr/bin/python
from betterPrompt import promptWithDefault as prompt
import subprocess
import os
import shlex
import time

print "enter 'end-record' to finish recording and existing script"

recipee = ''
while True:

    command = prompt('$')
    command = shlex.split(command)

    if 'end-record' == command[0]:
        break

    if 'cd' == command[0]:
        os.chdir(command[1])
        continue

    try:

        subprocess.check_call(command)

    except Exception as e:
        print 'command failed:', e

        continue

    keepCommand = prompt('Keep last command ?', 'y')
    if ('y' == keepCommand ):
        recipee += ' '.join(command) + '\n'


f = open(str(time.time()) + 'record.sh', 'w')
f.write(recipee)
f.close

print 'recipee saved'

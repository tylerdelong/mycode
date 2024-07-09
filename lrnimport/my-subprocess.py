#!/usr/bin/env python3

import os
from subprocess import call


directory = os.path.expanduser('~/mycode')

call(["ip", "link", "show", "up"])
call(["ls", "-l", directory])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])


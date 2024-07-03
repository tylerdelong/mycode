#!/usr/bin/env python3

import shutil

import os

os.chdir("/home/student/mycode/")

shutil.copy("5g-research/sdnnetwork.txt", "5g-research/sdn_network.txt.copy")

shutil.copytree("5g-research/", "5g-research_backup/")


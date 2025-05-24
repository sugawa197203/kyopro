#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
contest = input("contest name: ")

def abc(id:int ):
	if not os.path.exists(f"abc{id}"):
		os.makedirs(f"abc{id}")
	
	os.system(f"cp -r ./template/abc/* ./abc{id}")
	os.chdir(f"abc{id}")
	while (command := input(f"abc{id}>")) != "exit":
		if command.startswith("r"):
			if len(command) == 2:
				probrem = command[1]
				os.system(f"python3 {probrem}.py < {probrem}in 2>&1 | tee {probrem}out")
			continue
		if command.startswith("i"):
			os.system("bash")
			continue


if contest.startswith("abc"):
	contest = contest[3:]
	abc(int(contest))

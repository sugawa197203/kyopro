#!/usr/bin/python
import os
import subprocess

contest = input("input contest name>")

if not os.path.exists(contest):
    result = subprocess.run(["acc", "new", contest])
    if result.returncode != 0:
        print("Error creating contest")
        exit(1)

os.chdir(contest)

while True:
    submittion = input("problem>").split()
    if submittion[0] == "exit":
        print("bye")
        break

    problem = submittion[0]
    lang = "py"
    if len(submittion) == 2:
        lang = submittion[1]
    
    os.chdir(problem)
    langcode = {
        "py": "5078",
        "cpp": "5028",
    }[lang]
    stdinput = "pra1"
    
    result = subprocess.run(["acc", "s", "--", f"main.{lang}", "--language", langcode], input=stdinput.encode())
    if result.returncode != 0:
        print("Error submitting")
        exit(1)
    os.chdir("..")

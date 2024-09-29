#!/usr/bin/python
import os
import subprocess

# check acc and oj login
result = subprocess.run(["acc", "session"])
if result.returncode != 0:
    print("Please login to acc")
    exit(1)

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

    if not os.path.exists("test"):
        result = subprocess.run(["oj", "d", f"https://atcoder.jp/contests/{contest}/tasks/{contest}_{submittion[0]}"])
        if result.returncode != 0:
            print("Error downloading problem")
            exit(1)
        print("Downloaded problem")

    problem = submittion[0]
    lang = "py"
    if len(submittion) == 2:
        lang = submittion[1]

    os.chdir(problem)
    print("Testing...")
    
    result = subprocess.run(["oj", "t", "-c", f"python main.py"])
    if result.returncode != 0:
        print("!!! Error testing !!!")
        continue
    langcode = {
        "py": "5078",
        "cpp": "5028",
    }[lang]
    stdinput = "y"

    print("Submitting...")
    
    result = subprocess.run(["acc", "s", "--", f"main.{lang}", "--language", langcode], input=stdinput.encode())
    if result.returncode != 0:
        print("Error submitting")
        exit(1)
    print("### Submitted ###")

    os.chdir("..")

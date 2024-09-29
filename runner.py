#!/usr/bin/python
import os
import subprocess

# check acc and oj login
result = subprocess.run(["acc", "session"])
if result.returncode != 0:
    print("Please login to acc")
    exit(1)

def test(lang:str, reactive:bool=False, interactive:bool=False):
    langcommand = {
        "py": "python main.py",
        "cpp": "./a.out",
    }[lang]
    if interactive:
        result = subprocess.run(langcommand.split())
        if result.returncode != 0:
            print("!!! Error interactive !!!")
            return False
        return True
    
    result = subprocess.run(["oj", "t" if not reactive else "t/r", "-c", langcommand, "-d", "tests"])
    if result.returncode != 0:
        print("!!! Error testing !!!")
        return False
    return True

def interactive(lang:str):
    langcommand = {
        "py": "python main.py",
        "cpp": "./a.out",
    }[lang]

    

contest = input("input contest name>")

if not os.path.exists(contest):
    result = subprocess.run(["acc", "new", contest])
    if result.returncode != 0:
        print("Error creating contest")
        exit(1)

os.chdir(contest)

while True:
    try:
        submittion = input(f"({contest}) problem>").split()
        if submittion[0] == "exit":
            print("bye")
            break

        problem = submittion[0]
        os.chdir(problem)
        lang = "py"
        isForce = False
        isinteractive = False
        isreactive = False
        testonly = False
        submittiononly = False
        if len(submittion) >= 2:
            for command in submittion[1:]:
                if command[0] == "-":
                    for mode in command[1:]:
                        if mode == "f":
                            isForce = True
                        if mode == "i":
                            isinteractive = True
                        if mode == "r":
                            isreactive = True
                        if mode == "t":
                            testonly = True
                        if mode == "s":
                            submittiononly = True
                else:
                    lang = command
            
        if len(submittion) >= 4:
            print("invalid input")
            continue


        if not submittiononly:
            print("Testing...")
            if not test(lang, isreactive, isinteractive):
                print("### Test failed ###")
                if not isForce:
                    os.chdir("..")
                    continue
                print("### Force submittion ###")
        else:
            print("### Skip testing ###")
        
        if testonly:
            print("### Test only ###")
            os.chdir("..")
            continue
            
        langcode = {
            "py": "5078",
            "cpp": "5028",
        }[lang]

        print("Submitting...")
        
        result = subprocess.run(["acc", "s", "--", f"main.{lang}", "--language", langcode, "-y"])
        if result.returncode != 0:
            print("Error submitting")
            exit(1)
        print("### Submitted ###")

        os.chdir("..")
    except Exception as e:
        print(e)
        print("### Error ###")
        os.chdir("..")
        continue

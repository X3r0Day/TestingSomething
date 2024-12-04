import os
import subprocess

# Updating the framework

def update_fm():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_dir)
    
    print("Fetching updates from GitHub...")
    fetch_processs = subprocess.run(["git", "fetch", "origin"],text=True, capture_output=True)
    status_process = subprocess.run(["git", "status", "-uno"],text=True, capture_output=True)

    if "Your branch is up to date" in status_process.stdout:
        print("Program is up to date!")
    else:
        print("Update found! Updating your repository")
        pull_process = subprocess.run(["git", "pull", "origin", "main"],text=True, capture_output=True)
        
        if pull_process.returncode == 0:
            print("Update successful!")
        else:
            print("Failed to update the repo.")
            print(pull_process.stderr)

while True:
    print("X3r0Day Toolkit");print();print()
    print("1 = Check for update")
    print("2 = Enter framework")
    print("99 = Exit")
    opt = int(input("> "))
    if opt == 1:
        print("Checking for updates...")
        update_fm()

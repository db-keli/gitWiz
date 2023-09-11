#!usr/bin/env python3
import subprocess
import sys
import re

def addFileAndCommit(args):
    if any(arg == '-f' for arg in args):
        index = args.index('-f')
        if index + 2 < len(args):
            file_to_add = args[index+1]
            commit_message = args[index+2]
            command = ['git', 'add', file_to_add]
            commit = ['git', 'commit', '-m', commit_message, f'--{file_to_add}']
            try:
                subprocess.run(command, check=True)
                print(f"Successfully added {file_to_add}! ")
                subprocess.run(commit, check=True)
                print(f"Committed {file_to_add}")

            except subprocess.CalledProcessError as error:
                print(f"{error}")
    else:
        print("No argument found")

# def add_file(args):
#     if any(arg == '-f' for arg in args):
#         index = args.index('-f')
#         file_to_add = args[index + 1]
#         command = ['git', 'add', file_to_add]
#         try:
#             subprocess.run(command, check=True)
#             print(f"""
#                   Successfully added {file_to_add}!
#                   Use squash -cp <commit-message> to commit and push all files
#                   """)
#         except subprocess.CalledProcessError as error:
#             print(f"{error}")
#     else:
#         print("No argument found")


def addAllAndCommit(args):
    if any(arg == '-a' for arg in args):
        index = args.index('-a')
        message = args[index +1]
        command1 = ['git', 'add', '.']
        command2 = ['git', 'commit',  '-m', f'{message}']
        try:
            subprocess.run(command1, check=True)
            subprocess.run(command2, check=True)
            print(f"Successfully added and committed all files")
        except subprocess.CalledProcessError as error:
            print(f"{error}")

def push(args):
    if any(arg == '-p' for arg in args):
        command = ['git', 'push']
        try:
            subprocess.run(command, check=True)
            print(f"Successfully pushed your codes to github")
        except subprocess.CalledProcessError as error:
            print(f"{error}")

  
if __name__ == "__main__":
    for i in sys.argv:
        i = i.rstrip()
        match = re.search('-p', i)
        print(match)
        

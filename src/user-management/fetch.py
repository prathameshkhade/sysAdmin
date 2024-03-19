#!usr/bin/python3

"""
    This will save the user information into json file
"""

import json
from subprocess import PIPE, Popen


def get_user() -> None:
    """
        Get the user information stored in the /etc/passwd file
    """
    cmd = "cat /etc/passwd | egrep -v 'nolgin$|false$' 2>&1"

    # Execute the cmd
    run = Popen(
        cmd,
        shell=True,
        text=True,
        stdout=PIPE,
        stderr=PIPE
    )

    try:
        stdout, stderr = run.communicate()
        if run.returncode == 0:
            stdout = stdout.split("\n")
            save(stdout)

    except Exception as e:
        print(f"Error: {e}")
    
def save(lst: list):
    """
        Saves the information of the users in the json file
    """

    with open("tmp/users.json", "w") as file:
        for line in lst:
            user = line.split(":")
            # user = user[:-1]

            # Create a structure of json file
            data = {
                f"{user[0]}": {
                    "isPass": True if user[1] == "x" else False,
                    "uid": int(user[2]),
                    "gid": int(user[3]),
                    "info": str(user[4]),
                    "homeDir": str(user[-2]),
                    "shell": str(user[-1])
                }
            }

            # Save the json file 
            data.dump(data, file)
            data.write(",\n")


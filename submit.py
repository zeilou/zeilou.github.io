import subprocess
subprocess.call(["git", "pull"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit","-m","updated"])
subprocess.call(["git", "push","origin","master"])

import subprocess
subprocess.call(["git", "pull"])
subprocess.call(["git", "add", "-A"])
subprocess.call(["git", "commit","-m","updated"])
subprocess.call(["git", "push","origin","master"])

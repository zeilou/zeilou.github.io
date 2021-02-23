import subprocess
subprocess.call(["git", "pull"])
#subprocess.call(["cp", "-rf",".vuepress/dist/*","."])
subprocess.call(["git", "add", "-A"])
subprocess.call(["git", "commit","-m","updated"])
subprocess.call(["git", "push","origin","master"])

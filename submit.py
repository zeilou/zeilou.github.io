import subprocess
subprocess.call(["git", "pull","origin","master"])
#subprocess.call(["cp", "-rf",".vuepress/dist/*","."])
subprocess.call(["git", "add", "-A"])
subprocess.call(["git", "commit","-m","updated"])
subprocess.call(["git", "push","origin","master"])

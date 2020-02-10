import subprocess
with open("log.txt", "w") as f:
    subprocess.run("ls -al", stdout=f, shell=True)

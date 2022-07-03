import subprocess, sys

def run(cmd):
    process = subprocess.Popen(["powershell", "-Command", cmd], stdout=sys.stdout)
    process.communicate()
    return process
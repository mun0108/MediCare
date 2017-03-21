import subprocess

class Operations():
    def runProcess(self,command):
        subprocess.call(command, shell=True)
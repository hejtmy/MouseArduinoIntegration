import subprocess
from time import sleep
import psutil

print subprocess.check_output("dir", shell=True)


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.get_children(recursive=True):
        proc.kill()
    process.kill()

while(True):
    proc = subprocess.Popen("mspaint circle.jpg", shell=True)
    sleep(3)
    try:
        kill(proc.pid)
    except Exception:
        print "nothing to close"

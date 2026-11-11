# Author Mason N, 2026, This program is free under the General Public License

import random
import os #OS is unneeded, comment if you'd like.
import signal
import time
import platform

roll = random.randint(1, 20)
print(roll)

if roll < 10:
    print("Bad roll...")
    time.sleep(2)
    parent_pid = os.getppid()
    if platform.system() == "Windows":
        os.kill(parent_pid, signal.SIGTERM) #Windows only, code below works for POSIX.
    else:
        os.kill(parent_pid, signal.SIGHUP) #Meant to work for MacOS and Linux, BSD is a maybe.

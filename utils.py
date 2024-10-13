import datetime
print(datetime.datetime.today())

import os
print(os.system('date'))



cmd = "git --version"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)

import subprocess

cmd = "git --version"

returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('returned value:', returned_value)
